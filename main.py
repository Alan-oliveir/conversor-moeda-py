import requests
from dotenv import load_dotenv
import os

load_dotenv()

# Chave da API
api_key = os.getenv('API_KEY')


# Função para obter a taxa de câmbio
def obter_taxa_de_cambio(api_key, moeda_origem, moeda_destino):
    try:
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{moeda_origem}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        dados = response.json()
        if 'conversion_rates' in dados and moeda_destino in dados['conversion_rates']:
            return dados['conversion_rates'][moeda_destino]
        else:
            raise ValueError("Dados de taxa de câmbio não disponíveis.")
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
        return None
    except ValueError as e:
        print(f"Erro nos dados recebidos: {e}")
        return None


def converter_moeda(api_key, valor, moeda_origem, moeda_destino):
    try:
        valor = float(valor)
        taxa = obter_taxa_de_cambio(api_key, moeda_origem, moeda_destino)
        if taxa is not None:
            return valor * taxa
        else:
            return None
    except ValueError:
        print("Valor inválido para conversão.")
        return None
