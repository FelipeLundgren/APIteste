import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)
print(response)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for i in dados_json:
        nome_do_restaurante = i['Company']
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []
        
        dados_restaurante[nome_do_restaurante].append({
            'item':i['Item'],
            'price': i['price'],
            'description': i['description']
            })
else:
    print(f'O erro foi {response.status_code}')

print(dados_restaurante['McDonald’s'])