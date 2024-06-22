import requests

url = "http://127.0.0.1:80/login"

# Dati di login
payload = {
    "username": "Costel",
    "password": "Camerana2024"
}

# Invio della richiesta POST
response = requests.post(url, json=payload)

# Gestione della risposta
if response.status_code == 200:
    print("Login effettuato con successo")
    print("Token:", response.json().get('token'))
else:
    print("Errore nel login:", response.json().get('message'))