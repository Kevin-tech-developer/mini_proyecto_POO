'''
Crea un programa que busque un tesoro en una lista de ubicaciones y se detenga cuando lo encuentre usando break.
'''
isla = "piedra negra"
tesoroEncontrado = False
while(tesoroEncontrado == False):
    print("\n islas disponibles para buscar el tesoro")
    print("1. arena blanca")
    print("2. palmas altas")
    print("3. marea baja")
    print("4. piedra negra")
    opcion = int(input("digite el numero de la opcion de la isla a la cual vamos a buscar el tesoro 🏴‍☠️ 🪙 : "))
    if(opcion == 4):
        while(True):
            print("\n opciones de direcciones a buscar el tesoro")
            print("1. sur ⬇️")
            print("2. norte ⬆️")
            print("3. este ➡️")
            print("4. oeste ⬅️")
            direccion = int(input(f"digite la direccion a la cual nos dirigiremos a bucar en la isla {isla}: "))
            if(direccion == 2):
                print("has encontrado el tesoro 🪙🪙🪙")
                tesoroEncontrado = True
                break
            else:
                print("en esta direccion no hay tesoro")
    else:
        print("en esta isla no hay tesoros")
    