def registrar_compra():
    print("=" * 45)
    print("   SISTEMA DE COMPRA DE ASIENTOS DE VIAJE")
    print("=" * 45)

    # 1. Nombre del comprador
    nombre = input("Ingrese el nombre del comprador: ").strip()
    
    # 2. Cantidad de asientos 
    while True:
        try:
            asientos = int(input("¿Cuántos asientos necesita?: "))
            if asientos > 0:
                break
            print("Por favor, ingrese un número mayor a 0.")
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")

    # Diccionario con los destinos y sus respectivos precios por pasaje 
    destinos = {
        1: ("Oruro - Colquiri", 20),
        2: ("La Paz - Colquiri", 60),
        3: ("Cochabamba - Colquiri", 120),
        4: ("Caracollo - Colquiri", 15),
        5: ("Colquiri - Oruro", 20),
        6: ("Colquiri - La Paz", 60),
        7: ("Colquiri - Cochabamba", 120),
        8: ("Colquiri - Caracollo", 15)
    }

    # 3. Seleccion de destino
    print("\n--- Seleccione el destino del viaje ---")
    for clave, (ruta, precio) in destinos.items():
        print(f"{clave}. {ruta} ({precio} Bs.)")

    while True:
        try:
            opcion = int(input("\nElija una opción (1-8): "))
            if opcion in destinos:
                destino_seleccionado, precio_unitario = destinos[opcion]
                break
            print("Opción fuera de rango. Seleccione un número entre 1 y 8.")
        except ValueError:
            print("Entrada inválida. Ingrese el número de la opción.")

    # 4. Calculo del monto total a pagar
    monto_total = asientos * precio_unitario

    # 5. Resumen final de la compra
    print("\n" + "=" * 45)
    print("           RESUMEN DE LA COMPRA")
    print("=" * 45)
    print(f"Comprador:            {nombre}")
    print(f"Cantidad de asientos: {asientos}")
    print(f"Destino:               {destino_seleccionado}")
    print(f"Precio por asiento:   {precio_unitario} Bs.")
    print(f"Monto total a pagar:  {monto_total} Bs.")
    print("=" * 45)
    print("¡Compra realizada con éxito!")

if __name__ == "__main__":
    registrar_compra()