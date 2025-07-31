productos = {}

cantidad = int(input("¿Cuantos productos va a ingresar?: "))

for i in range(cantidad):
    print(f"Producto {i + 1}")
    code = input("Ingresa código: ")
    if code in productos:
        while True:
            print("Codigo exitente!")
            code = input("Agregue otro codigo: ")
            if code not in productos:
                break
    name = input("Ingresa nombre: ")
    category = input("Ingrese la categoría (Hombre, Mujer o Niño): ")
    size = input("Ingresa la talla (S, M, L o XL): ")
    price = int(input("Ingresa el precio: "))
    if price <= 0:
        while price <= 0:
            print("Error, precio no válido (Debe ser mayor a 0)")
            price = int(input("Ingrese nuevamente el precio: "))
    cant = int(input("Ingrese la cantidad en stock: "))
    while cant < 0:
        print("Cantidad incorrecta (negativa)")
        cant = input("Agrega nuevamente la cantidad: ")
        if cant > 0:
            break
    productos[code] = {
        "codigo": code,
        "nombre": name,
        "categoria": category,
        "talla": size,
        "precio": price,
        "cantidad": cant
    }

def ShowAllProducts():
    for code, i in productos.items():
        print("- - -  Producto ingresado  - - -")
        print(f"Código: {i['codigo']}")
        print(f"Nombre: {i['nombre']}")
        print(f"Categoría: {i['categoria']}")
        print(f"Talla: {i['talla']}")
        print(f"Precio: {i['precio']}")
        print(f"Cantidad en stock: {i['cantidad']}")

def SpecificProduct():
    show_prodcut = input("Ingresa el codico del producto que quieres ver: ")
    print(productos[show_prodcut])

def TotalValue():
    total = 0
    for code, i in productos.items():
        total_value = i['precio'] * i['cantidad']
        print(f"El valor total de {i['nombre']} es de {total_value}")
        total += total_value
    print(f"El patrimonio del inventario es de {total}")

def ShowByCategory():
    show = input("Ingrese la categoria a mostrar: ")
    for code, i in productos.items():
        if productos[code]['categoria'] == show:
            print(f"- - -  Producto encontrado por cateogría {show} - - -")
            print(f"Código: {i['codigo']}")
            print(f"Nombre: {i['nombre']}")
            print(f"Categoría: {i['categoria']}")
            print(f"Talla: {i['talla']}")
            print(f"Precio: {i['precio']}")
            print(f"Cantidad en stock: {i['cantidad']}")

while True:
    print("\n1. Mostrar lista de productos"
          "\n2. Mostrar código por producto"
          "\n3. Calcular valor total de inventario"
          "\n4. Mostrar cuantos productos hay por categoría"
          "\n5. Salir")
    option = input("Seleccione una opcion (1-5): ")
    match option:
        case "1":
            ShowAllProducts()
        case "2":
            SpecificProduct()
        case "3":
            TotalValue()
        case "4":
            ShowByCategory()
        case "5":
            break
        case _:
            print("opcion no valida")