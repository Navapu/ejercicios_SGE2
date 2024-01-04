def cargar_alumnos():
    alumnos = {}
    for _ in range(3):
        dni = input("Ingrese el DNI del alumno: ")
        materias_notas = cargar_materias_notas()
        alumnos[dni] = materias_notas
    return alumnos

def cargar_materias_notas():
    materias_notas = []
    for _ in range(3):
        materia = input("Ingrese el nombre de la materia: ")
        nota = float(input(f"Ingrese la nota de {materia}: "))
        materias_notas.append((materia, nota))
    return materias_notas

def listar_alumnos(alumnos):
    print("Listado de todos los alumnos con sus notas:")
    for dni, materias_notas in alumnos.items():
        print(f"DNI: {dni}")
        for materia, nota in materias_notas:
            print(f"{materia}: {nota}")

def consultar_alumno(alumnos, dni_consulta):
    if dni_consulta in alumnos:
        materias_notas = alumnos[dni_consulta]
        print(f"Alumno con DNI {dni_consulta} cursa las siguientes materias:")
        for materia, nota in materias_notas:
            print(f"{materia}: {nota}")
    else:
        print(f"No se encontró ningún alumno con DNI {dni_consulta}.")

# Paso 1: Cargar alumnos
alumnos_cargados = cargar_alumnos()

# Paso 2: Listar todos los alumnos con sus notas
listar_alumnos(alumnos_cargados)

# Paso 3: Consultar un alumno por su DNI
dni_a_consultar = input("Ingrese el DNI del alumno a consultar: ")
consultar_alumno(alumnos_cargados, dni_a_consultar)
