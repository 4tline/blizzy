from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def selenium_login(username, password):
    # Initialiser le navigateur (ici, Chrome, mais vous pouvez utiliser un autre navigateur)
    driver = webdriver.Chrome()

    # Accéder à l'URL de la page de connexion
    driver.get("http://192.168.100.1")  # Remplacez par l'URL réelle

    # Trouver les champs de texte pour le nom d'utilisateur et le mot de passe
    username_field = driver.find_element(By.ID, "txt_Username")
    password_field = driver.find_element(By.ID, "txt_Password")

    # Remplir les champs
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Trouver et cliquer sur le bouton de soumission
    login_button = driver.find_element(By.ID, "button")
    login_button.click()

    # Vous pouvez maintenant vérifier la page résultante pour voir si la connexion a réussi
    if "incorrect" in driver.page_source.lower():
        print("Nom d'utilisateur ou mot de passe incorrect.")
    else:
        print("Connexion réussie.")

    # Fermer le navigateur
    driver.quit()

# Entrée des informations utilisateur
user = input('Nom d\'utilisateur : ')
password = input('Mot de passe : ')

# Soumettre le formulaire avec Selenium
selenium_login(user, password)
