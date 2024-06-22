from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Dati di esempio per gli utenti
users = {
    "Costel": "Camerana2024"
}

@app.route('/login', methods=['PUT'])
def fare_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # Verifica delle credenziali
    if username in users and users[username] == password:
        # Creazione di una risposta di successo
        response = {
            "message": "Login effettuato con successo",
            "token": "abcdef123456"  # In una applicazione reale, questo dovrebbe essere un token generato dinamicamente
        }
        return jsonify(response), 200
    else:
        # Risposta di errore per credenziali non valide
        response = {
            "message": "Credenziali non valide"
        }
        return jsonify(response), 401

if __name__ == '__main__':
    app.run(debug=True,port = 80)

    