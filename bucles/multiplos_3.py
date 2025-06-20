'''
Escribe un programa que imprima los números del 1 al 20, pero que se salte los múltiplos de 3 usando continue.
'''


for i in range(1,21):
    if(i %3 ==0):
        continue
    print(i)