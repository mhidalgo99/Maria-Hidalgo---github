class Usuario:
    def __init__(self, nombre, edad, email, altura, estudiante, fecha_de_cumpleaños):
        self.nombre = nombre
        self.edad = edad
        self.email = email
        self.altura = altura
        self.estudiante = estudiante
        self.fecha_de_cumpleaños = fecha_de_cumpleaños

    def __str__(self):
        estudiante_str = "Sí" if self.estudiante else "No"
        return (f"Nombre: {self.nombre}\nEmail: {self.email}\nEdad: {self.edad}\n"
                f"Altura: {self.altura}m\nEstudiante: {estudiante_str}\n"
                f"Fecha de cumpleaños: {self.fecha_de_cumpleaños}\n")

# Lista para almacenar usuarios
usuarios = [5]
Usuario("Maria Hidalgo", 25, "mhhidalgo99@gmail.com", 1.70, True, "28-01-1999"),
Usuario("Karyna Torrres", 35, "ktorres@gmail.com", 1.60, False, "01-12-1989"),
Usuario("Marco Fernández", 25, "marco9905@gmail.com", 1.75, True, "05-08-1999"),
Usuario("Pablo Sánchez", 34, "pablocampo@gmail.com", 1.75, False, "16-02-1990"),
Usuario("Luisana Rojo", 24, "luisarojo@gmail.com", 1.55, True, "22-04-2000"),

# Función para imprimir todos los usuarios
def imprimir_usuarios():
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        for i, usuario in enumerate(usuarios, start=1):
            print(f"Usuario {i}:\n{usuario}")

# Función para imprimir usuarios ordenados por edad
def imprimir_usuarios_ordenados():
    if not usuarios:
        print("No hay usuarios registrados.")
        return

    orden = input("¿Desea ordenarlos por edad en orden ascendente o descendente? (asc/desc): ").strip().lower()
    if orden not in ["asc", "desc"]:
        print("Opción no válida. Mostrando en orden descendente por defecto.")
        orden = "desc"

    usuarios_ordenados = sorted(usuarios, key=lambda x: x.edad, reverse=(orden == "desc"))
    for usuario in usuarios_ordenados:
        print(usuario)

# Función para buscar un usuario por email
def buscar_usuario_por_email():
    if not usuarios:
        print("No hay usuarios registrados.")
        return

    email = input("Ingrese el email del usuario que desea buscar: ").strip()
    for usuario in usuarios:
        if usuario.email == email:
            print("Usuario encontrado:")
            print(usuario)
            return
    print("No se encontró un usuario con ese email.")

# Función para agregar un nuevo usuario
def agregar_usuario():
    try:
        nombre = input("Ingrese el nombre del usuario: ").strip()
        email = input("Ingrese el email del usuario: ").strip()
        edad = int(input("Ingrese la edad del usuario: ").strip())
        altura = float(input("Ingrese la altura del usuario (en metros): ").strip())
        estudiante_input = input("¿Es estudiante? (sí/no): ").strip().lower()
        estudiante = estudiante_input in ["sí", "si", "s"]
        fecha_de_cumpleaños = input("Ingrese la fecha de cumpleaños (formato YYYY-MM-DD): ").strip()

        # Validar el formato de la fecha
        from datetime import datetime
        try:
            datetime.strptime(fecha_de_cumpleaños, "%Y-%m-%d")
        except ValueError:
            print("Error: Formato de fecha no válido. Use el formato YYYY-MM-DD.")
            return

        nuevo_usuario = Usuario(nombre, edad, email, altura, estudiante, fecha_de_cumpleaños)
        usuarios.append(nuevo_usuario)
        print("Usuario agregado correctamente.")
    except ValueError:
        print("Error: Por favor, ingrese datos válidos.")

# Función para actualizar un usuario por email
def actualizar_usuario():
    if not usuarios:
        print("No hay usuarios registrados.")
        return

    email = input("Ingrese el email del usuario que desea actualizar: ").strip()
    for usuario in usuarios:
        if usuario.email == email:
            print("Usuario encontrado. Ingrese los nuevos datos (deje en blanco para mantener el valor actual):")
            nombre = input(f"Nombre ({usuario.nombre}): ").strip() or usuario.nombre
            try:
                edad = input(f"Edad ({usuario.edad}): ").strip()
                edad = int(edad) if edad else usuario.edad

                altura = input(f"Altura ({usuario.altura}): ").strip()
                altura = float(altura) if altura else usuario.altura

                estudiante_input = input(f"Estudiante (Sí/No, actual: {'Sí' if usuario.estudiante else 'No'}): ").strip().lower()
                estudiante = estudiante_input in ["sí", "si", "s"] if estudiante_input else usuario.estudiante

                fecha_de_cumpleaños = input(f"Fecha de cumpleaños ({usuario.fecha_de_cumpleaños}): ").strip() or usuario.fecha_de_cumpleaños

                # Validar el formato de la fecha
                from datetime import datetime
                try:
                    datetime.strptime(fecha_de_cumpleaños, "%Y-%m-%d")
                except ValueError:
                    print("Error: Formato de fecha no válido. Use el formato YYYY-MM-DD.")
                    return

                usuario.nombre = nombre
                usuario.edad = edad
                usuario.altura = altura
                usuario.estudiante = estudiante
                usuario.fecha_de_cumpleaños = fecha_de_cumpleaños

                print("Usuario actualizado con éxito.")
                return
            except ValueError:
                print("Error: Datos inválidos. No se realizaron cambios.")
                return
    print("No se encontró un usuario con ese email.")

# Función para borrar un usuario por email
def borrar_usuario_por_email():
    if not usuarios:
        print("No hay usuarios registrados.")
        return

    email = input("Ingrese el email del usuario que desea borrar: ").strip()
    for usuario in usuarios:
        if usuario.email == email:
            usuarios.remove(usuario)
            print("Usuario eliminado con éxito.")
            return
    print("No se encontró un usuario con ese email.")

# Función para borrar todos los usuarios
def borrar_todos_los_usuarios():
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        usuarios.clear()
        print("Todos los usuarios han sido eliminados.")

# Menú principal
def menu():
    while True:
        print("\n--- Menú de Opciones ---")
        print("1. Imprimir todos los usuarios")
        print("2. Imprimir usuarios ordenados por edad")
        print("3. Buscar un usuario por email")
        print("4. Agregar un nuevo usuario")
        print("5. Actualizar un usuario existente")
        print("6. Borrar un usuario por email")
        print("7. Borrar todos los usuarios")
        print("8. Salir")

        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            imprimir_usuarios()
        elif opcion == "2":
            imprimir_usuarios_ordenados()
        elif opcion == "3":
            buscar_usuario_por_email()
        elif opcion == "4":
            agregar_usuario()
        elif opcion == "5":
            actualizar_usuario()
        elif opcion == "6":
            borrar_usuario_por_email()
        elif opcion == "7":
            borrar_todos_los_usuarios()
        elif opcion == "8":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor intente nuevamente.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()