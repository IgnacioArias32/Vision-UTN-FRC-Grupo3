import random

def adivina(intentos, numero):
    res= random.randint(0, 100)
    while intentos>0:
        if numero==res:
            print('Felicidades ganaste!')
        else:
            intentos=intentos-1
            print('Intentos restantes:',intentos)
            if intentos>0:
                numero = int(input('Ingrese otro entero: '))
            else:
                print('Perdiste :( \nEl número era',res)



oportunidades = int(input('Ingrese cantidad de intentos: '))
guess = int(input('Ingrese un entero: '))

adivina(oportunidades, guess)



