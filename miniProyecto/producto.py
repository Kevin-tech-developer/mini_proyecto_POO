
class Producto:#creacion de una clase

    def __init__(self, nombre, cantidad, precio):#constructor de la clase
        self.nombre = nombre #inicializacion o declaracion de los atributos
        self.cantidad = cantidad
        self.precio = precio
        

    def sumar_cantidad(self, cantidad1):#funciones
        self.cantidad += cantidad1 
        
    def restar_cantidad(self, cantidad2):
        self.cantidad -= cantidad2
        
    def getNombre(self):
        return self.nombre
        
    def verProducto2(self): #funcion para mostrar el objeto de la tienda
        return f"nombre: {self.nombre}, precio: {self.precio}, cantidad: {self.cantidad}"