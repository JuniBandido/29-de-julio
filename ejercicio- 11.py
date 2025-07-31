propietarios = {}

def AddOwner():
    for i in range(int(input("Ingrese cuantos propietarios desea agregar: "))):
        print(f"Propietario #{i + 1}")
        nit = input("Ingresa su nit: ")
        full_name = input("Ingrese su nombre completo: ")
        phone = input("Ingrese su número de teléfono: ")
        cant_vehicles = input("Ingrese la cantidad de vehículos: ")
        propietarios[nit] = {
            "nombre": full_name,
            "telefono": phone,
            "vehiculos": cant_vehicles
        }
        for x in range(int(cant_vehicles)):
            print(f"Vehículo {x + 1}")
            plate = input("Ingrese el número de placa del vechículo: ")
            brand = input("Ingrese la marca del vehículo: ")
            model = input("Ingrese el modelo del vehículo: ")
            year = input("Ingresa el año del modelo: ")
            tax = input("Ya pagó inpuesto? 1) Si. 2) No.")
            propietarios[cant_vehicles] = {
                "placa": plate,
            }
            propietarios[plate] = {
                "marca": brand,
                "modelo": model,
                "año": year,
                "impuesto": tax
            }

def ShowOownersAndVehicles():
    for nit, i in propietarios.items():
        print(f"Propietario encontrado")
        print(f"Nit: {i['nit']}")
        print(f"Nombre: {i['nombre']}")
        print(f"Teléfono: {i['telefono']}")
        print(f"Cantidad de vehículos: {i['vehiculos']}")
        for cant_vehicles, x in propietarios.items():
            print(f"Vehículos encontrados a nombre de {i['nombre']}")
            print(f"Placa: {x['placa']}")
            for plate, y in propietarios.items():
                print(f"Marca: {y['marca']}")
                print(f"Modelo: {y['modelo']}")
                print(f"Año: {y['año']}")
                print(f"Impuesto pagado? {y['impuesto']}")
