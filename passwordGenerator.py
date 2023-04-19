#Version 1.2
import random

letras_minusculas = chr(random.randint(97,122))
letras_maiusculas = chr(random.randint(65,90))
char_especial =chr(random.randint(33,64))
lista_numeros = []
senha_lista = []

for i in range(6):
    numeros = random.randrange(9)
    lista_numeros.append(numeros)

random.shuffle(lista_numeros)
senha_lista = letras_maiusculas, letras_minusculas,char_especial
senha_lista = list(senha_lista)
senha_lista.extend(lista_numeros)
random.shuffle(senha_lista)

senha_lista = str(senha_lista).strip('[]')
senha_lista = senha_lista.replace(',','')

print(senha_lista)