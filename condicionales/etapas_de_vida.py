'''
Escribe un programa que, dada una edad, imprima la etapa de la vida de una persona. Usa las siguientes reglas:

0-12 años: "Eres un(a) niño(a)."
13-17 años: "Eres un(a) adolescente."
18-64 años: "Eres un(a) adulto(a)."
65 años o más: "Eres un(a) adulto(a) mayor."
'''
while(True):
    edad = int(input("ingrese la edad a evaluar: "))
    if(edad >0 and edad <=12):
        print("eres un(a) niño(a)")
    elif(edad >=13 and edad <=17):
        print("Eres un(a) adolescente")
    elif(edad >=18 and edad <=64):
        print("Eres un(a) adulto(a)")
    elif(edad >=65):
        print("Eres un(a) adulto(a) mayor")
    else:
        print("edad incorrecta")
