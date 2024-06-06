from flask import Flask, request


backend = Flask('applicazioneBE')

@backend.route('/ciao', methods=['POST','GET'])
def rottaCiao():

    come = request.method

    return f'hai chiamato la rotta ciao  con metodo {come}'



if (__name__ == '__main__'):
    backend.run(host = '0.0.0.0',port = 80)