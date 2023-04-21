#Version 1.4
import random
import string

def main_menu():
    while True:
        print('1) Gerar senha')
        print('0) Exit')
        
        opcao = input("Digite a opção: ")

        if opcao == '1':
            tamanho_senha = int(input('Digite o tamanho da senha: '))
            gerar_senha(tamanho_senha)
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")
            
def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    
    print(senha)
    print('Senha gerada com sucesso !!!')


main_menu()


