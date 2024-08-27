dic={'router':('adress or default_getaway' , 'username', 'default password')}
def A():
    with open('router.txt') as liste:
        content=liste.read()
        print(content)
def B():
    with open("router.txt") as new_file:
        count = 0
        total_length = 0

        for line in new_file:
            line = line.replace("\n", "")
            count += 1
            print("Line", count, line)
            length = len(line)
            total_length += length
            print("Total length of lines:", total_length)
def file2dic():
    global dic
    with open('router.txt') as file:
        #print(file)
        for line in file:
            line = line.strip()  # Remplacez replace("\n", "") par strip() pour supprimer les espaces blancs en début et fin de ligne
            #print('')
            #print('###################################')
            #print('the line is ', line)
            line = line.split()
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
    print('Le routeur:',key,'\n   default getaway: ',a,"\n   nom d'utilisateur: ",b, '\n   mot de passe: ',c)


def print_dic():
    global dic
    for i in dic:
        try:
            a, b, c=dic[i]
        except:
            a , b ,c = dic[i],'',''
        print('Le routeur:',i,'\n   default getaway: ',a,"\n   nom d'utilisateur: ",b, '\n   mot de passe: ',c)
def lookup_dic(key):
    if key in dic:
        if type(dic[key])==int:
            numb=int(dic[key])
            for i in range(numb):
                new_key = f"{key}{i}"
                print_tuple(new_key)
        else:
            print_tuple(key)
    else:
        print('erreur veuillez recommencer')
def __main__():
    print_dic()
    file2dic()
    #print_dic()
    print('voici les diffrents routeurs disponibles:')
    for i in dic:
        print(i,end=' , ')
    while True:
        i=input('nom de votre routeur:\n (tappez exit pour quitter)\n')
        match i:
            case 'exit':
                print('fin du programme')
                break
            case _:
                lookup_dic(i)
        
        
__main__()

