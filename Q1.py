import random
import string

def gerar_senha_aleatoria():
   
    try:
        comprimento = int(input("Digite a quantidade de caracteres para a senha: "))

        if comprimento < 4:
            print("A senha deve ter no mínimo 4 caracteres.")
            return

        letras_maiusculas = string.ascii_uppercase
        letras_minusculas = string.ascii_lowercase
        numeros = string.digits
        caracteres_especiais = string.punctuation

  
        senha_parcial = random.choice(letras_maiusculas)
        senha_parcial += random.choice(letras_minusculas)
        senha_parcial += random.choice(numeros)
        senha_parcial += random.choice(caracteres_especiais)

        
        todos_caracteres = letras_maiusculas + letras_minusculas + numeros + caracteres_especiais
        for _ in range(comprimento - 4):
            senha_parcial += random.choice(todos_caracteres)

    
        lista_senha = list(senha_parcial)
        random.shuffle(lista_senha)
        senha_final = "".join(lista_senha)

        print(f"Senha gerada: {senha_final}")

    except ValueError:
        print("Por favor, insira um número inteiro válido para o comprimento.")


gerar_senha_aleatoria()
