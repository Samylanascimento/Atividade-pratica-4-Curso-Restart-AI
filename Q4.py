import requests
from datetime import datetime

def consultar_cotacao_moeda():
    """
    Consulta a cotação de uma moeda estrangeira em relação ao BRL
    e exibe seu valor atual, máximo, mínimo e a data da cotação.
    """
    codigo_moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()

    try:
       
        url = f"https://api.awesomeapi.com.br/last/{codigo_moeda}-BRL"
        response = requests.get(url)
        response.raise_for_status()
        dados_cotacao = response.json()

       
        chave_moeda = f"{codigo_moeda}BRL"
        if chave_moeda in dados_cotacao:
            cotacao = dados_cotacao[chave_moeda]
            data_hora = datetime.fromtimestamp(int(cotacao['timestamp'])).strftime('%d/%m/%Y %H:%M:%S')

            print(f"\n--- Cotação de {cotacao['name']} ---")
            print(f"Valor Atual: R$ {float(cotacao['bid']):.2f}")
            print(f"Máximo do Dia: R$ {float(cotacao['high']):.2f}")
            print(f"Mínimo do Dia: R$ {float(cotacao['low']):.2f}")
            print(f"Última Atualização: {data_hora}")
        else:
            print(f"Não foi possível encontrar a cotação para a moeda '{codigo_moeda}'.")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API de cotação: {e}")

consultar_cotacao_moeda()
