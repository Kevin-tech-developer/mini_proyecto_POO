'''
Una tienda online ofrece envío gratis si el día es sábado o
si el cliente tiene un cupón de envío gratis. Escribe un programa que 
le diga al usuario si su envío es gratis o no.
'''
clave = [1234, 3459, 9643]
while(True):
    dia=input("digite que dia de la semana es: ")
    print("tienes un cupon de envio gratis - 1.yes/ 2.Not")
    opcion = int(input("digite la opcion: "))
    verdad = False
    if(opcion ==1):
        cupon= int(input("digite los numeros del cupon: "))
        for i in clave:
            if(i == cupon):
                verdad = True
                break
        if(verdad):
            print("cupon valido")
        else:
            print("cupon no valido")
    
    if(dia == "sabado" or verdad == True):
        print("tienes envio gratis")
    else:
        print("no tienes envio gratis")