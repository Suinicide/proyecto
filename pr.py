import os

# Constantes para los archivos de datos
ARCHIVO_ESTUDIANTES = 'estudiantesfull.txt'
ARCHIVO_ASIGNATURAS = 'asignaturas.txt'
ARCHIVO_CARRERAS = 'carreras.txt'
ARCHIVO_NOTAS = 'notas.txt'

# Función principal del menú
def menu():
    while True:
        print("\nSistema Académico")
        print("1. Cargar archivos planos de texto")
        print("2. Crear y almacenar datos en archivos planos de texto")
        print("3. Calcular la nota definitiva de un estudiante en una asignatura")
        print("4. Calcular el promedio del semestre de un estudiante")
        print("5. Calcular el promedio de los promedios del semestre para todos los estudiantes de una carrera")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            cargar_archivos()
        elif opcion == '2':
            crear_datos()
        elif opcion == '3':
            calcular_nota_definitiva()
        elif opcion == '4':
            calcular_promedio_semestre()
        elif opcion == '5':
            calcular_promedio_carrera()
        elif opcion == '6':
            break
        else:
            print("Opción no válida, intente de nuevo.")

# Función para cargar archivos planos de texto
def cargar_archivos():
    cargar_estudiantes()
    cargar_asignaturas()
    cargar_carreras()
    cargar_notas()

def cargar_estudiantes():
    if os.path.exists(ARCHIVO_ESTUDIANTES):
        with open(ARCHIVO_ESTUDIANTES, 'r') as file:
            estudiantes = file.readlines()
        print("Estudiantes cargados.")
    else:
        print("Archivo de estudiantes no encontrado.")

def cargar_asignaturas():
    if os.path.exists(ARCHIVO_ASIGNATURAS):
        with open(ARCHIVO_ASIGNATURAS, 'r') as file:
            asignaturas = file.readlines()
        print("Asignaturas cargadas.")
    else:
        print("Archivo de asignaturas no encontrado.")

def cargar_carreras():
    if os.path.exists(ARCHIVO_CARRERAS):
        with open(ARCHIVO_CARRERAS, 'r') as file:
            carreras = file.readlines()
        print("Carreras cargadas.")
    else:
        print("Archivo de carreras no encontrado.")

def cargar_notas():
    if os.path.exists(ARCHIVO_NOTAS):
        with open(ARCHIVO_NOTAS, 'r') as file:
            notas = file.readlines()
        print("Notas cargadas.")
    else:
        print("Archivo de notas no encontrado.")

# Función para crear y almacenar datos en archivos planos de texto
def crear_datos():
    while True:
        print("\nCrear y almacenar datos")
        print("1. Datos estudiantes")
        print("2. Datos carreras(solo las existentes en la FULL)")
        print("3. Datos asignaturas")
        print("4. Datos notas")
        print("5. Regresar al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            crear_datos_estudiantes()
        elif opcion == '2':
            crear_datos_carreras()
        elif opcion == '3':
            crear_datos_asignaturas()
        elif opcion == '4':
            crear_datos_notas()
        elif opcion == '5':
            break
        else:
            print("Opción no válida, intente de nuevo.")

def crear_datos_estudiantes():
    codigo = input("Ingrese el código del estudiante: ")
    nombre = input("Ingrese el nombre completo del estudiante: ")
    correo = input("Ingrese su correo (Se forma utilizando las iniciales de sus nombres, acompañado de su primer apellido completo, y la inicial de su segundo apellido)")
    celular = input("Ingrese el número de celular del estudiante: ")
    id_carrera = input("Ingrese el identificador de carrera del estudiante: ")

    with open(ARCHIVO_ESTUDIANTES, 'a') as file:
        file.write(f"{codigo},{nombre},{correo},{celular},{id_carrera}\n")
    print("Estudiante registrado.")

def crear_datos_carreras():
    id_carrera = input("Ingrese el identificador de la carrera: ")
    nombre = input("Ingrese el nombre de la carrera: ")
    creditos_totales = input("Ingrese los créditos totales de la carrera: ")
    modalidad = input("Ingrese la modalidad de la carrera (Virtual/Presencial): ")
    facultad = input("Ingrese el nombre de la facultad a la que pertenece: ")

    with open(ARCHIVO_CARRERAS, 'a') as file:
        file.write(f"{id_carrera},{nombre},{creditos_totales},{modalidad},{facultad}\n")
    print("Carrera registrada.")

def crear_datos_asignaturas():
    id_asignatura = input("Ingrese el identificador de la asignatura: ")
    nombre = input("Ingrese el nombre de la asignatura: ")
    creditos = input("Ingrese los créditos de la asignatura: ")
    intensidad_horaria = input("Ingrese la intensidad horaria semanal de la asignatura: ")

    with open(ARCHIVO_ASIGNATURAS, 'a') as file:
        file.write(f"{id_asignatura},{nombre},{creditos},{intensidad_horaria}\n")
    print("Asignatura registrada.")

def crear_datos_notas():
    codigo_estudiante = input("Ingrese el código del estudiante: ")
    id_asignatura = input("Ingrese el identificador de la asignatura: ")
    cantidad_notas = int(input("Ingrese la cantidad de notas: "))
    notas = [input(f"Ingrese la nota {i+1}: ") for i in range(cantidad_notas)]

    with open(ARCHIVO_NOTAS, 'a') as file:
        file.write(f"{codigo_estudiante},{id_asignatura},{cantidad_notas}," + ",".join(notas) + "\n")
    print("Notas registradas.")

# Función para calcular la nota definitiva de un estudiante en una asignatura
def calcular_nota_definitiva():
    codigo_estudiante = input("Ingrese el código del estudiante: ")
    id_asignatura = input("Ingrese el identificador de la asignatura: ")

    if os.path.exists(ARCHIVO_NOTAS):
        with open(ARCHIVO_NOTAS, 'r') as file:
            notas = file.readlines()

        for nota in notas:
            datos = nota.strip().split(',')
            if datos[0] == codigo_estudiante and datos[1] == id_asignatura:
                notas_asignatura = list(map(float, datos[3:]))
                nota_definitiva = sum(notas_asignatura) / len(notas_asignatura)
                print(f"La nota definitiva de la asignatura {id_asignatura} del estudiante {codigo_estudiante} es: {nota_definitiva:.2f}")
                return
        print("Notas no encontradas.")
    else:
        print("Archivo de notas no encontrado.")

# Función para calcular el promedio del semestre de un estudiante
def calcular_promedio_semestre():
    codigo_estudiante = input("Ingrese el código del estudiante: ")

    if os.path.exists(ARCHIVO_NOTAS) and os.path.exists(ARCHIVO_ASIGNATURAS):
        with open(ARCHIVO_NOTAS, 'r') as file_notas, open(ARCHIVO_ASIGNATURAS, 'r') as file_asignaturas:
            notas = file_notas.readlines()
            asignaturas = file_asignaturas.readlines()
        asignaturas_dict = {}
        for line in asignaturas:
            partes = line.strip().split(',')
            if len(partes) >= 3 and partes[2].isdigit():
                asignaturas_dict[partes[0]] = int(partes[2])
            else:
                print(f"Error en formato de línea de asignaturas: {line}")

        notas_estudiante = [line.strip().split(',') for line in notas if line.split(',')[0] == codigo_estudiante]
        if not notas_estudiante:
            print("No se encontraron notas para el estudiante.")
            return

        suma_ponderada = 0
        suma_creditos = 0

        for nota in notas_estudiante:
            id_asignatura = nota[1]
            if id_asignatura in asignaturas_dict:
                notas_asignatura = list(map(float, nota[3:]))
                nota_definitiva = sum(notas_asignatura) / len(notas_asignatura)
                creditos = asignaturas_dict[id_asignatura]
                suma_ponderada += nota_definitiva * creditos
                suma_creditos += creditos

        if suma_creditos > 0:
            promedio_semestre = suma_ponderada / suma_creditos
            print(f"El promedio del semestre del estudiante {codigo_estudiante} es: {promedio_semestre:.2f}")
        else:
            print("No se encontraron créditos para las asignaturas del estudiante")

# Función para calcular el promedio de los promedios del semestre para todos los estudiantes de una carrera
def calcular_promedio_carrera():
    id_carrera = input("Ingrese el identificador de la carrera: ")

    if os.path.exists(ARCHIVO_ESTUDIANTES) and os.path.exists(ARCHIVO_NOTAS) and os.path.exists(ARCHIVO_ASIGNATURAS):
        with open(ARCHIVO_ESTUDIANTES, 'r') as file_estudiantes, open(ARCHIVO_NOTAS, 'r') as file_notas, open(ARCHIVO_ASIGNATURAS, 'r') as file_asignaturas:
            estudiantes = file_estudiantes.readlines()
            notas = file_notas.readlines()
            asignaturas = file_asignaturas.readlines()

        # Debugging: Print the number of lines read from each file
        print(f"Estudiantes: {len(estudiantes)} líneas leídas.")
        print(f"Notas: {len(notas)} líneas leídas.")
        print(f"Asignaturas: {len(asignaturas)} líneas leídas.")

        asignaturas_dict = {}
        for line in asignaturas:
            partes = line.strip().split(',')
            if len(partes) >= 3 and partes[2].isdigit():
                asignaturas_dict[partes[0]] = int(partes[2])
            else:
                print(f"Error en formato de línea de asignaturas: {line}")

        print("Contenido de asignaturas_dict:")
        for key, value in asignaturas_dict.items():
            print(f"{key}: {value}")

        estudiantes_carrera = [line.strip().split(',') for line in estudiantes if len(line.split(',')) > 4 and line.split(',')[4] == id_carrera]
        if not estudiantes_carrera:
            print("No se encontraron estudiantes para la carrera.")
            return

        # Debugging: Print the students found for the career
        print("Estudiantes encontrados para la carrera:")
        for estudiante in estudiantes_carrera:
            print(estudiante)

        suma_promedios = 0
        contador_estudiantes = 0

        for estudiante in estudiantes_carrera:
            codigo_estudiante = estudiante[0]
            notas_estudiante = [line.strip().split(',') for line in notas if line.split(',')[0] == codigo_estudiante]
            if not notas_estudiante:
                continue

            suma_ponderada = 0
            suma_creditos = 0

            for nota in notas_estudiante:
                id_asignatura = nota[1]
                if id_asignatura in asignaturas_dict:
                    try:
                        notas_asignatura = list(map(float, nota[3:]))
                        nota_definitiva = sum(notas_asignatura) / len(notas_asignatura)
                        creditos = asignaturas_dict[id_asignatura]
                        suma_ponderada += nota_definitiva * creditos
                        suma_creditos += creditos
                    except ValueError:
                        print(f"Error al convertir notas a float: {nota[3:]}")
                        continue

            if suma_creditos > 0:
                promedio_semestre = suma_ponderada / suma_creditos
                suma_promedios += promedio_semestre
                contador_estudiantes += 1

        if contador_estudiantes > 0:
            promedio_carrera = suma_promedios / contador_estudiantes
            print(f"El promedio de los promedios del semestre para la carrera {id_carrera} es: {promedio_carrera:.2f}")
        else:
            print("No se encontraron notas para los estudiantes de la carrera.")
    else:
        print("Archivos de estudiantes, notas o asignaturas no encontrados.")

# Ejecutar el menú principal
if __name__ == '__main__':
    menu()
