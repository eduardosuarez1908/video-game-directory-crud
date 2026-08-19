# Sistema de Gestión de Directorio de Videojuegos
# Proyecto académico - Desarrollo de Software y Ciberseguridad
# Autor: Eduardo Suarez

videojuegos = []


def mostrar_menu():
    print("\n=== SISTEMA DE GESTIÓN DE VIDEOJUEGOS ===")
    print("1. Registrar videojuego")
    print("2. Mostrar videojuegos")
    print("3. Buscar videojuego")
    print("4. Modificar videojuego")
    print("5. Eliminar videojuego")
    print("6. Salir")


def registrar_videojuego():
    print("\n--- Registrar videojuego ---")
    nombre = input("Nombre del videojuego: ")
    genero = input("Género: ")
    plataforma = input("Plataforma: ")
    anio = input("Año de lanzamiento: ")

    videojuego = {
        "nombre": nombre,
        "genero": genero,
        "plataforma": plataforma,
        "anio": anio
    }

    videojuegos.append(videojuego)
    print("Videojuego registrado correctamente.")


def mostrar_videojuegos():
    print("\n--- Directorio de videojuegos ---")

    if not videojuegos:
        print("No hay videojuegos registrados.")
        return

    for indice, videojuego in enumerate(videojuegos, start=1):
        print(f"\nVideojuego #{indice}")
        print(f"Nombre: {videojuego['nombre']}")
        print(f"Género: {videojuego['genero']}")
        print(f"Plataforma: {videojuego['plataforma']}")
        print(f"Año: {videojuego['anio']}")


def buscar_videojuego():
    print("\n--- Buscar videojuego ---")
    nombre_busqueda = input("Ingrese el nombre del videojuego a buscar: ").lower()

    encontrado = False

    for videojuego in videojuegos:
        if videojuego["nombre"].lower() == nombre_busqueda:
            print("\nVideojuego encontrado:")
            print(f"Nombre: {videojuego['nombre']}")
            print(f"Género: {videojuego['genero']}")
            print(f"Plataforma: {videojuego['plataforma']}")
            print(f"Año: {videojuego['anio']}")
            encontrado = True
            break

    if not encontrado:
        print("No se encontró el videojuego.")


def modificar_videojuego():
    print("\n--- Modificar videojuego ---")
    nombre_busqueda = input("Ingrese el nombre del videojuego a modificar: ").lower()

    for videojuego in videojuegos:
        if videojuego["nombre"].lower() == nombre_busqueda:
            print("Videojuego encontrado. Ingrese los nuevos datos.")

            videojuego["nombre"] = input("Nuevo nombre: ")
            videojuego["genero"] = input("Nuevo género: ")
            videojuego["plataforma"] = input("Nueva plataforma: ")
            videojuego["anio"] = input("Nuevo año de lanzamiento: ")

            print("Videojuego modificado correctamente.")
            return

    print("No se encontró el videojuego.")


def eliminar_videojuego():
    print("\n--- Eliminar videojuego ---")
    nombre_busqueda = input("Ingrese el nombre del videojuego a eliminar: ").lower()

    for videojuego in videojuegos:
        if videojuego["nombre"].lower() == nombre_busqueda:
            videojuegos.remove(videojuego)
            print("Videojuego eliminado correctamente.")
            return

    print("No se encontró el videojuego.")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_videojuego()
        elif opcion == "2":
            mostrar_videojuegos()
        elif opcion == "3":
            buscar_videojuego()
        elif opcion == "4":
            modificar_videojuego()
        elif opcion == "5":
            eliminar_videojuego()
        elif opcion == "6":
            print("Gracias por usar el sistema. Hasta luego.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
