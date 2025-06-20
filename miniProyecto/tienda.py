from producto import Producto

class Tienda: #creacion de una clase
    def __init__(self): #self: significa this
        #inicializacion de una lista para el objeto tienda
        self.inventario = []#creacion o declaracion de los atributos de la clase
        self.inventario.append(Producto("leche", 20, 4000))
        self.inventario.append(Producto("pan", 30, 2000))
        self.inventario.append(Producto("huevos", 40, 700))
        
    def agregar(self, producto):
        #la funcion isinstance(objeto, clase a comparar): sirve para saber que lo que se va a trabajar si es de la clase 
        #que necesitamos
        if isinstance(producto, Producto):
            self.inventario.append(producto)
        else:
            print("lo que quieres agregar no cumple con los parametros permitidos")
            
    def verProducto(self): #funciones de la clase
        for i in self.inventario:
            print(i.verProducto2())
            
    def venderProducto(self, nombre, cantidad):
        for i in self.inventario:
            if(nombre == i.getNombre()):
                i.restar_cantidad(cantidad)
                print("se actualizo correctamente el inventario")
                return
        print("producto no encontrado")
        
    def agregarCantidad(self, nombre, cantidad):
        for i in self.inventario:
            if(nombre == i.getNombre()):
                i.sumar_cantidad(cantidad)
                print("se agrego correctamente al stock")
                return
        print("elemento no encontrado")

    
