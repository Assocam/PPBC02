import requests

url = "http://127.0.0.1:5000/login"

# Dati di login
payload = {
    "username": "utente",
    "password": "password123"
}

# Invio della richiesta POST
response = requests.post(url, json=payload)

# Gestione della risposta
if response.status_code == 200:
    print("Login effettuato con successo")
    print("Token:", response.json().get('token'))
else:
    print("Errore nel login:", response.json().get('message'))