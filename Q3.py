import requests

def consultar_cep():
 
    cep = input("Digite o CEP para consulta (somente números): ")

    if not cep.isdigit() or len(cep) != 8:
        print("CEP inválido. Por favor, digite 8 números.")
        return

    try:
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        response.raise_for_status()
        dados_cep = response.json()

        if "erro" in dados_cep:
            print("CEP não encontrado.")
        else:
            print("\n--- Informações do Endereço ---")
            print(f"Logradouro: {dados_cep.get('logradouro', 'Não disponível')}")
            print(f"Bairro: {dados_cep.get('bairro', 'Não disponível')}")
            print(f"Cidade: {dados_cep.get('localidade', 'Não disponível')}")
            print(f"Estado: {dados_cep.get('uf', 'Não disponível')}")

    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro ao consultar o CEP: {e}")

consultar_cep()
