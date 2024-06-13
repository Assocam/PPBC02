
import json
datij = datirichiesta


risposta = requests.post('http://10.10.21.10/datijson',json = datij)

codice = risposta.status_code
