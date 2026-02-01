import os

def cargar_productos(nombre_archivo):
    productos = {}
    if os.path.exists(nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as f:
                for linea in f:
                    try:
                        codigo, nombre = linea.strip().split(':', 1)
                        productos[codigo] = nombre
                    except ValueError:
                        print(f"Error al procesar la línea: '{linea.strip()}'. Formato incorrecto.  Debe ser 'codigo:nombre'")
        except IOError:
            print(f"Error al leer el archivo: {nombre_archivo}")
    return productos

def guardar_productos(nombre_archivo, productos):
    try:
        with open(nombre_archivo, 'w') as f:
            for codigo, nombre in productos.items():
                f.write(f"{codigo}:{nombre}\n")
    except IOError:
        print(f"Error al escribir en el archivo: {nombre_archivo}")

def mostrar_productos(productos):
    if not productos:
        print("No hay productos en el sistema.")
        return
    for codigo, nombre in productos.items():
        print(f"{codigo}: {nombre}")

def alta_producto(productos):
    codigo = input("Introduce el código del producto: ")
    if codigo in productos:
        print("El producto ya existe.")
        return
    nombre = input("Introduce el nombre del producto: ")
    productos[codigo] = nombre
    print("Producto añadido correctamente.")

def borrar_producto(productos):
    nombre_a_borrar = input("Introduce el nombre del producto a borrar: ")
    codigo_a_borrar = None
    for codigo, nombre in productos.items():
        if nombre == nombre_a_borrar:
            codigo_a_borrar = codigo
            break
    if codigo_a_borrar:
        del productos[codigo_a_borrar]
        print("Producto borrado correctamente.")
    else:
        print("El producto no existe.")

def main():
    nombre_archivo = "productes.txt"
    productos = cargar_productos(nombre_archivo)

    while True:
        print("Opciones:")
        print("0 - Salir del programa")
        print("1 - Mostrar productos existentes")
        print("2 - Añadir nuevo producto")
        print("3 - Borrar producto existente")

        opcion = input("Elige una opción: ")

        if opcion == '0':
            guardar_productos(nombre_archivo, productos)
            print("Saliendo del programa.")
            break
        elif opcion == '1':
            mostrar_productos(productos)
        elif opcion == '2':
            alta_producto(productos)
            guardar_productos(nombre_archivo, productos)
        elif opcion == '3':
            borrar_producto(productos)
            guardar_productos(nombre_archivo, productos)
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()