from tienda import Tienda
from producto import Producto

tienda = Tienda() #instansacion de la clase
while(True): #menu
    print("\n sistema local")
    print("1. ver productos")
    print("2. vender producto")
    print("3. agregar stock de producto")
    print("4. agregar producto")
    print("5. salir")
    
    opcion = int(input("digite el numero de la opcion: "))
    #condicionales
    if(opcion ==1):
        tienda.verProducto()
    elif(opcion ==2):
        nombre = input("ingrese el nombre del producto a vender: ")
        cantidad = int(input("cantidad a vender: "))
        tienda.venderProducto(nombre, cantidad)
    elif(opcion ==3):
        nombre = input("ingrese el nombre del producto a modificar: ")
        cantidad = int(input("cantidad a introducir: "))
        tienda.agregarCantidad(nombre, cantidad)
    elif(opcion == 4):
        nombre = input("ingrese el nombre del producto a ingresar: ")
        cantidad = int(input("cantidad del nuevo producto:  "))
        precio = float(input("introduce el precio del nuevo producto: "))
        tienda.agregar(Producto(nombre, cantidad, precio))
        print("producto agregado correctamente")
    elif(opcion ==5):
        print("gracias por usar nuestro sistema")
        break
    else:
        print("opcion no valida")
    