import requests
from dotenv import load_dotenv
import os

load_dotenv()

# Chave da API
api_key = os.getenv('API_KEY')


# Função para obter a taxa de câmbio
def obter_taxa_de_cambio(api_key, moeda_origem, moeda_destino):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{moeda_origem}"
    response = requests.get(url)
    dados = response.json()
    if response.status_code == 200:
        return dados['conversion_rates'][moeda_destino]
    else:
        print(f"Erro: {dados['error-type']}")
        return None


# Função para converter moeda
def converter_moeda(api_key, valor, moeda_origem, moeda_destino):
    taxa = obter_taxa_de_cambio(api_key, moeda_origem, moeda_destino)
    if taxa:
        return valor * taxa
    else:
        print("Não foi possível obter a taxa de câmbio.")
        return None


'''''# Exemplo de uso
moeda_origem = input("Digite a moeda de origem (por exemplo, USD): ").upper()
moeda_destino = input("Digite a moeda de destino (por exemplo, BRL): ").upper()
valor = float(input("Digite o valor a ser convertido: "))

valor_convertido = converter_moeda(api_key, valor, moeda_origem, moeda_destino)
if valor_convertido:
    print(f"{valor} {moeda_origem} é igual a {valor_convertido:.2f} {moeda_destino}")'''
