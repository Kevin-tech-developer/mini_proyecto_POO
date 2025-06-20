'''
Escribe un programa que use bucles anidados para imprimir un rectángulo de asteriscos con un ancho y alto específicos.
'''
altura = int(input("digite la altura del rectangulo en entero: "))
ancho = int(input("digite el ancho del rectangulo en entero: "))

for i in range(altura):
    for e in range(ancho):
        print("*", end="")#end= nos funciona diciendo en la duncion print que no haga ningun salto de linea
    print()#agrega un salto de linea