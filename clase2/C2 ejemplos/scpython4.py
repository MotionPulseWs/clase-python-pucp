# EJEMPLO DE GESTION DE PRODUCTOS
import pickle
import os

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = float(precio)
        self.cantidad = cantidad
    
    def subtotal(self):
        return self.precio*self.cantidad
    
    def __str__(self):
        return f"{self.nombre} - S./ {self.precio:.2f}"
    

def guardar_binario(lista_productos,archivo):
    with open(archivo,'wb') as archivo:
        pickle.dump(lista_productos, archivo)
    print("Productos guardados correctamente")

def cargar_binario(archivo):
    try:
        with open(archivo, 'rb') as archivo:
            data = pickle.load(archivo)
        print("Archivo cargado correctamente")
        return data
    except FileNotFoundError:
        print("No existe el archivo ...")
        return []


nombre_archivo = 'productos_tienda.bin'
productos = []


# MENU PRINCIPAL
print("\n Gestion de productos")
print("Opciones: ")
print(" 1 .- Agregar productos")
print(" 2 .- Mostrar productos")
print(" 3 .- Eliminar productos")
print(" 4 .- Guardar")
print(" 5 .- Cargar")
print(" 6 .- Salir")
print("==================\n")

while True:
    opcion = input("Elige una opcion (1-4): ")

    if opcion == '1':
        try:
            nombre = input("Nombre del producto a agregar : ")
            precio = float(input("Ingrese el precio del producto : "))
            cantidad = int(input("Ingrese la cantidad de productos : "))
            flag_creacion = 1
        except ValueError:
            flag_creacion = 0
            print("Valores ingresados incorrectamente, volver a crear el producto")
        
        if flag_creacion == 1:
            producto = Producto(nombre, precio, cantidad)
            productos.append(producto)
            print("Producto agregado")
    elif opcion == '2':
        if len(productos) == 0:
            print("No hay productos \n")
        else:
            for prod in productos:
                print(f"{prod} - Subtotal : {prod.subtotal():.2f}")
    
    elif opcion == '3':
        nombre = input("Nombre del producto a eliminar: ")
        for prod in productos:
            if prod.nombre == nombre:
                productos.remove(prod)
                eliminado = True
                break
        if eliminado:
            print("Producto eliminado")
        else:
            print("No existe producto con ese nombre")
    elif opcion == '4':
        guardar_binario(productos,nombre_archivo)
    elif opcion == '5':
        productos = cargar_binario(nombre_archivo)
    elif opcion == '6':
        guardar_binario(productos,nombre_archivo)
        print("Programa finalizado")
        break
    else:
        print("Opcion no valida, intente otra vez")

print("Se ha finalizado el programa guardando el carrito")
