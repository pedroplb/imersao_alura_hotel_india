import requests

def buscar_taxa_cambio(moeda_origem, moeda_destino):

    # Faça uma solicitação GET para a API para obter as taxas de câmbio mais recentes
    url = f'https://economia.awesomeapi.com.br/json/last/{moeda_origem}-{moeda_destino}'
    response = requests.get(url)
    data = response.json()

    # Verifique se a solicitação foi bem-sucedida
    if response.status_code == 200:
        return float(data['INRBRL']['high'])
    else:
        return f'Erro ao buscar taxa de cambio - retorno: {response.status_code}'

