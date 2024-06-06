from flask import Flask
import requests

backend = Flask('applicazioneBE')

if (__name__ == '__main__'):
    backend.run(host = '0.0.0.0',port = 80)