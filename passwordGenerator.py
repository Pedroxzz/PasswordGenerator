#Version 1.3
import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    
    return senha

tamanho_senha = int(input('Digite o tamanho da senha: '))
senha = gerar_senha(tamanho_senha)
print(senha)
print('Senha gerada com sucesso !!!')
input('')