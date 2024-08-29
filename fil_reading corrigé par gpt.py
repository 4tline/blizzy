dic = {}  # Initialisation du dictionnaire global

def file2dic():
    global dic
    with open('router.txt') as file:
        for line in file:
            line = line.strip()
            line = line.split(';')
            word = line[0]
            try:
                tup = (line[2], line[3], line[4])
            except IndexError:  # Utiliser IndexError pour capturer l'erreur spécifique
                tup = int(line[2])
            dic[word] = tup


def print_tuple(key):
    a, b, c = dic[key]
    print(f'Le routeur: {key}\n   default getaway: {a}\n   nom d\'utilisateur: {b}\n   mot de passe: {c}')

def print_dic():
    global dic
    for i in dic:
        if isinstance(dic[i], tuple):
            a, b, c = dic[i]
        else:
            a, b, c = dic[i], '', ''
        print(f'Le routeur: {i}\n   default getaway: {a}\n   nom d\'utilisateur: {b}\n   mot de passe: {c}')

def lookup_dic(key):
    if key in dic:
        if isinstance(dic[key], int):
            numb = dic[key]
            for i in range(numb):
                new_key = f"{key}{i}"
                if new_key in dic:
                    print_tuple(new_key)
                else:
                    print(f'{new_key} not found in dictionary')
        else:
            print_tuple(key)
    else:
        print('erreur veuillez recommencer')

def __main__():
    file2dic()
    print('voici les différents routeurs disponibles:')
    print_dic()  # Afficher les routeurs après avoir rempli le dictionnaire
    for i in dic:
        print(i, end=' , ')
    while True:
        i = input('nom de votre routeur:\n (tappez exit pour quitter)\n')
        if i == 'exit':
            print('fin du programme')
            break
        else:
            lookup_dic(i)

__main__()

