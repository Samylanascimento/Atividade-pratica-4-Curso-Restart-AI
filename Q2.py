import requests

def gerar_perfil_usuario():

    try:
        response = requests.get("https://randomuser.me/api/")
        response.raise_for_status()  
        dados = response.json()
        usuario = dados["results"][0]

        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print("\n--- Perfil de Usuário Gerado ---")
        print(f"Nome: {nome}")
        print(f"Email: {email}")
        print(f"País: {pais}")

    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro ao tentar se comunicar com a API: {e}")

gerar_perfil_usuario()
