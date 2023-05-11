from random import choice
import string

def gerar_senha():

    tamanho_da_senha = int(input(
        """
         ==================================
        |                                  |
        |   Bem Vindo ao Gerador de Senha  |
        |                                  |
         ==================================

Informe com quantos caracteres você deseja para sua senha: 
        
        """))

    caracters = string.ascii_letters + string.punctuation + string.digits
    senha_gerada = ""

    for i in range(tamanho_da_senha):
        senha_gerada += choice(caracters)

    if tamanho_da_senha < 8:

        resposta = int(input("""
Senha com menor que 8 caracters é considerada Fraca, Gostaria de seguir?
1 - Sim
2 - Não
        """))

        if resposta == 1:
            print(f"Sua senha Gerada é: {senha_gerada}")

        elif resposta == 2:
            gerar_senha()
        
        else:
            print("Comando invalido!")
            gerar_senha()
    else:
        print(f"Sua senha Gerada é: {senha_gerada}")


gerar_senha()