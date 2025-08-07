estudiantes = {}

def addStudents():
    id_student = input("Ingrese el id del estudiante: ")
    name_student = input("Ingrese el nombre completo del estudiante: ")
    carrer_student = input("Ingrese la carrera del estudiante: ")
    print("Estudiante agregado con éxito\n")
    estudiantes[id_student] = {
         'id': id_student,
         'nombre': name_student,
         'carrera': carrer_student
     }

def addCurse():
    soli = input("Ingrese el id del estudiante: ")
    if soli in estudiantes:
        name_curse = input("Agregue el nombre del curso: ")
        note_curse = int(input("Agregue la calificacion del curso: "))
        estudiantes[soli][name_curse] = {
            'nombreCurso': name_curse,
            'notaCurso': note_curse
        }

def showStudent():
    soli = input("\nIngrese el id del estudiante: ")
    if soli in estudiantes:
        for soli, i in estudiantes.items():
            print("-- Estudiante encontrado --")
            print(f"\nId: {i['id']}")
            print(f"\nNombre: {i['nombre']}")
            print(f"\nCarrera: {i['carrera']}")
            print(f"\nNombre del curso: {i['cursos']['nombreCurso']}")
            print(f"\nNota de curso: {i['cursos']['notaCurso']}\n")

def calcPromedy():
    action = input("Ingresa el id del estudiante: ")
    if action in estudiantes:
        suma = 0
        for action, i in estudiantes.items():
            suma += i
            print(f"\nEl promedio de tus calificaciones es de {suma / i}")

while True:
    print("1. Agregar estudiante\n"
          "2. Agregar curso\n"
          "3. Mostrar información\n"
          "4. Calcular Promedio\n"
          "5. Salir\n")
    menu = input("Escoge una opción (1-5): ")
    match menu:
        case "1":
            addStudents()
        case "2":
            addCurse()
        case "3":
            showStudent()
        case "4":
            calcPromedy()
        case "5":
            break
        case _:
            print("Opcion no válida\n")

addStudents()
addCurse()
addCurse()
print(estudiantes)