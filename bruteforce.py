username = 'admin'
user_password = 'password2023'

# Lire les utilisateurs de user.txt
with open('user.txt') as user_list:
    users = [user.strip() for user in user_list]

# Lire les mots de passe de passwords.txt
with open('passwords.txt') as password_list:
    passwords = [password.strip() for password in password_list]

# Lancer l'attaque brute force
found = False
for user in users:
    for password in passwords:
        if user == username and password == user_password:
            print(f'Le mot de passe est "{password}", et l\'utilisateur est "{user}"')
            found = True
            break
        else:
            print(f'Test echoue pour l\'utilisateur "{user}" mot de passe "{password}"')
    if found:
        break

if not found:
    print("Aucune correspondance trouvee.")
