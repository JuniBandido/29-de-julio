propietarios = {}

def AddOwner():
    for i in range(int(input("Ingrese cuantos propietarios desea agregar: "))):
        print(f"Propietario #{i + 1}")
        nit = input("Ingresa su nit: ")
        full_name = input("Ingrese su nombre completo: ")
        phone = input("Ingrese su número de teléfono: ")
        cant_vehicles = input("Ingrese la cantidad de vehículos: ")
        for x in range(int(cant_vehicles)):
            print(f"Vehículo {x + 1}")
            plate = input("Ingrese el número de placa del vechículo: ")
            brand = input("Ingrese la marca del vehículo: ")
            model = input("Ingrese el modelo del vehículo: ")
            year = input("Ingresa el año del modelo: ")
            tax = input("¿Ya pagó impuesto? (si - no): ")
            propietarios[nit] = {
                'nombre': full_name,
                'telefono': phone,
                'vehiculos': {
                    'placa': {
                        'marca': brand,
                        'modelo': model,
                        'año': year,
                        'impuesto': tax
                        }
                    }
                }

def ShowOwnersAndVehicles():
    for nit, i in propietarios.items():
        print(f"Propietario encontrado")
        print(f"Nit: {nit}")
        print(f"Nombre: {i['nombre']}")
        print(f"Teléfono: {i['telefono']}")
        for cant_vehicles, x in propietarios['vehiculos'].items():
            print(f"Vehiculos entrados a nombre de {i['nombre']}")
            print(f"Marca: {cant_vehicles}")


AddOwner()
print(propietarios)
ShowOwnersAndVehicles()