from flask import Flask , request

app = Flask('Fare il login')

@app.route('\login',methods = ['POST'])

def EvaluateLogin():

    try:
        dati = request.json
        u = dati["username"] 
        p = dati["password"]
    except:
        return{"result":"errore dati"},403

    return {'result': 'not found'},404



if __name__ =='__main__':
    app.run(host = "0.0.0.0",port = 80)


