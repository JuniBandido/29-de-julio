students = float(input("Cuantos estudiantes desea ingresar: "))
while True:
    try:
        students
    except ValueError:
        print("Error, número no valido")

    except TypeError:
        print("Error, caracter no válido")

    except Exception as e:
        print("Se produjo un error: ")

    else:
        print(f"Numero {students} ingresado con éxito")
        break

for x in range(students):
    name = input("Ingrese su nombre: ")
    many_notes = int(input("Ingrese la cantidad de notas: "))
    note = 0
    for y in range(many_notes):
        notes = int(input(f"Ingrese el punteo {y + 1}: "))
        note += notes
    print(f"\nNombre: {name}"
          f"\nPromedio: {(note) / many_notes}\n ")

