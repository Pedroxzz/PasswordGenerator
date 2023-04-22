#Version 1.5
import random
import string

def main_menu():
    while True:
        print('\033[31m1)\033[m Gerar senha')
        print('\033[32m0)\033[m Exit')
        
        opcao = input("Digite a opção: ")

        if opcao == '1':
            tamanho_senha = int(input('Digite o tamanho da senha: '))
            gerar_senha(tamanho_senha)
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")
            
def gerar_senha(tamanho):
    
    add_str = ''
    add_num = ''
    add_special = ''
    caracteres = ''
    continuar = True

    while continuar:
        add_str = input("Deseja adicionar letras à senha? (s/n): ")
        if add_str.lower() == 's':
            caracteres += string.ascii_letters
        elif add_str.lower() != 'n':
            print("Entrada inválida. Digite 's' para sim ou 'n' para não.")
            continue

        add_num = input("Deseja adicionar números à senha? (s/n): ")
        if add_num.lower() == 's':
            caracteres += string.digits
        elif add_num.lower() != 'n':
            print("Entrada inválida. Digite 's' para sim ou 'n' para não.")
            continue
        
        add_special = input("Deseja adicionar caracteres especiais à senha? (s/n): ")
        if add_special.lower() == 's':
            caracteres += string.punctuation
        elif add_special.lower() != 'n':
            print("Entrada inválida. Digite 's' para sim ou 'n' para não.")
            continue
        
        if not caracteres:
            print("Você deve selecionar pelo menos uma opção para gerar a senha.")
            continue
        continuar = False
    
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    
    print(senha)
    print('Senha gerada com sucesso !!!')


main_menu()


