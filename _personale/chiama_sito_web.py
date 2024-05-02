import requests
from flask import Flask, request
risposta = requests.get("https://3bmeteo.com")
print(risposta)
print(risposta.text)