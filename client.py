# import requests

# url = "http://127.0.0.1:5000/login"

# # Dati di login
# payload = {
#     "username": "utente",
#     "password": "password123"
# }

# # Invio della richiesta POST
# response = requests.post(url,json=payload)

# # Gestione della risposta
# if response.status_code == 200:
#     print("Login effettuato con successo")
#     print("Token:", response.json().get('token'))
# else:
#     print("Errore nel login:", response.json().get('message'))




import requests

# URL dell'endpoint di login
login_url = "http://127.0.0.1/login"

# Credenziali di login
login_data = {
    'username': 'username',
    'password': 'password123'
}

# Intestazioni (opzionale)
headers = {
    'Content-Type': 'application/json'
}

# Esegui la richiesta POST
response = requests.post(login_url, json=login_data, headers=headers)

# Verifica lo stato della risposta
if response.status_code == 200:
    print("Login riuscito!")
    # Ottieni e stampa il token di autenticazione
    auth_token = response.json().get('token')
    print("Token di autenticazione:", auth_token)
else:
    print("Errore nel login:", response.status_code, response.text)