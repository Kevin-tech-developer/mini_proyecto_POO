'''
Un parque de diversiones quiere permitir el acceso a su nueva montaña rusa solo a personas que
midan 1.50 metros o más y que además
tengan 16 años o más. Crea un programa que determine si una persona puede subir o no.
'''
while(True):
    altura = float(input("ingrese su altura: "))
    if(altura >=1.50):
        edad=int(input("ingrese su edad: "))
        if(edad >=16):
            print("bienvenido a la montaña rusa")
        else:
            print("no tienes la edad suficiente")
    else:
        print("no tienes la edad suficiente")