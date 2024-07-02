from pprint import pprint
import requests
from bs4 import BeautifulSoup

# Lista di URL da esaminare
url_list = [
    'https://www.subito.it/annunci-italia/vendita/usato/?q=spectrum+sinclair&o=1',
    'https://www.subito.it/annunci-italia/vendita/usato/?q=spectrum+sinclair&o=2'
]

# Effettua una richiesta GET al primo URL nella lista
result = requests.get(url_list[0])

# Controlla se la richiesta ha avuto successo (status code 200)
if result.status_code == 200:
    # Parsing del contenuto HTML della pagina utilizzando BeautifulSoup
    soup = BeautifulSoup(result.content, 'html.parser')

    # Seleziona gli elementi HTML corrispondenti ai prodotti desiderati
    # products = soup.select('div.items__item.item-card')
    products = soup.select('div[class*=SmallCard-module_card__]')
    # pprint(products)  # Stampa la lista di prodotti (opzionale)

    # Lista per memorizzare gli oggetti di interesse
    items = []


    # # Itera sui prodotti trovati
    for adv in products:
    #     # Estrae i dati di interesse dal prodotto corrente
        data = {
            'name': adv.select('h2[class*=ItemTitle-module_item-title__]'),  # Nome del prodotto
            'price': adv.select("p[class*=SmallCard-module_price__]"),  # Prezzo del prodotto
            'town': adv.select('span[class*=index-module_town__]'),  # Città del venditore
            'province': adv.select('span.city'),
        }   

        # for key in data:
        #     value = data[key]

        for key, value in data.items():
            if value:
                data[key] = value[0].get_text()
            else:
                data[key] = None
            
        # print(type(data['price']))
        if data['price'] is not None:
            data['price'] = data['price'].replace('\xa0',' ').replace('Spedizione disponibile', '')

        items.append(data)

    # # Stampa i dati estratti
    pprint(items)