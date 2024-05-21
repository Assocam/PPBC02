import pandas as pd


from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor

from sklearn.model_selection import train_test_split
data=pd.read_csv('C:\\PPBC02\\PPBC02\\_personale\\outputs\\ricette.csv')
    

#print(data)

# with open('/workspaces/PPBC02/_personale/ricette.csv','r',encoding = 'utf-8')as data:
#     pipo = data.read()
#     print(pipo)



X = data["ingredienti"]
y = data["gradimento"]

model = make_pipeline(TfidfVectorizer(), Ridge())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

model.fit(X_train, y_train) #riempie il modello

score = model.score(X_test, y_test) #testa il modello

nuova_ricetta = ["farina, lievito, acqua, sale, olio EVO"]
gradimento_predetto = model.predict(nuova_ricetta)

print(f'Punteggio del modello {score}')
print(f'Puteggio predetto per {nuova_ricetta} = {gradimento_predetto}')