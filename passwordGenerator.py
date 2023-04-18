import random

letras_minusculas = chr(random.randint(97,122))
letras_maiusculas = chr(random.randint(65,90))
char_especial =chr(random.randint(33,64))
lista_numeros = []

for i in range(6):
    numeros = random.randrange(9)
    lista_numeros.append(numeros)

random.shuffle(lista_numeros)
lista_numeros = str(lista_numeros).strip('[]')
lista_numeros = lista_numeros.replace(',','')

print(letras_maiusculas, letras_minusculas, lista_numeros, char_especial)