# EJEMPLO DE CARRITO DE COMPRAS

archivo_carrito = 'carrito_compras.txt'
carrito = []

try:
    with open(archivo_carrito, 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            linea.strip()
            if linea.startswith("- "):
                producto = linea[2:]
                carrito.append(producto)
        
        print("Carrito cargado desde el archivo")
except FileNotFoundError:
    print("No existe el archivo, iniciando carrito vacio ...")

# MENU PRINCIPAL
print("\n CARRITO DE COMPRAS")
print("Opciones: ")
print(" 1 .- Agregar productos")
print(" 2 .- Quitar productos")
print(" 3 .- Mostrar productos")
print(" 4 .- Salir y guardar")
print(" 5 .- Editar producto")
print("==================\n")

while True:
    opcion = input("Elige una opcion (1-4): ")

    if opcion == '1':
        producto = input("Nombre del producto a agregar: ")
        carrito.append(producto)
        print(f"-> {producto} agregado al carrito \n")

    elif opcion == '2':
        producto = input("Nombre del producto a eliminar: ")
        if producto in carrito:
            carrito.remove(producto)
            print(f"-> {producto} eliminado del carrito \n")
        else:
            print("Este producto no esta en el carrito")
    elif opcion == '3':
        print("\n====CARRITO ACTUAL")
        if len(carrito) == 0:
            print("El carrito esta vacio")
        else:
            for item in carrito:
                print(f" - {item}")
            print("\n")
    elif opcion == '4':
        with open(archivo_carrito, 'w') as archivo:
            if len(carrito) == 0:
                archivo.write("CARRITO VACIO \n")
            else:
                for item in carrito:
                    archivo.write(f"- {item}\n")
        break
    elif opcion == '5':
        productoEditar = input("Ingrese el nombre del producto a editar : ")
        if productoEditar in carrito:
            indice = carrito.index(productoEditar)
            nuevoProducto = input("Ingrese el nombre modificado : ")
            carrito[indice] = nuevoProducto
            print("Producto modificado")
        else:
            print("Producto no existe en la lista\n")
    else:
        print("Opcion no valida, intente otra vez")

print("Se ha finalizado el programa guardando el carrito")
