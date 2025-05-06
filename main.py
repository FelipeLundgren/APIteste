from fastapi import FastAPI,Query
import requests
app = FastAPI()

@app.get('/api/hello')

def hello_world():
    '''
    Endpoint de testes
    '''
    return {'Hello': 'World'}

@app.get('/api/restaurantes/')

def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para cardapios dos restaurantes
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}
        
        dados_restaurante = []
        for i in dados_json:
            if i['Company'] == restaurante:
                dados_restaurante.append({
                    'item':i['Item'],
                    'price': i['price'],
                    'description': i['description']
                    })
        return{'Restaurante':restaurante,'Cardapio':dados_restaurante}
    else:
        return {'Erro':f'{response.status_code} - {response.text}'}