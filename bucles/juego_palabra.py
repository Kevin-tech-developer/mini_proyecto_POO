'''
Crea un juego simple donde el usuario debe adivinar una palabra secreta usando un bucle while.
'''
palabra = "sls"
while(True):
    intento = input("digite la palabra para intentar: ")
    if(intento == palabra):
        print("has encontrado la palabra")
        break