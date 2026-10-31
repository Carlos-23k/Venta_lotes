import lotes
import ventas

def cargar_datos_prueba():
    lotes.registrar_lote("LT-001", "Los Jardines", 120, 450)
    lotes.registrar_lote("LT-002", "Las Palmeras", 90, 500)
    print("Datos de prueba obligatorios cargados.\n")

def menu():
    cargar_datos_prueba()
    while True:
        print("\n--- SISTEMA DE VENTA DE LOTES ---")
        print("1. Registrar lote")
        print("2. Listar lotes disponibles")
        print("3. Registrar venta")
        print("4. Ver resumen de ventas")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                cod = input("Código: ")
                urb = input("Urbanización: ")
                area = input("Área (m2): ")
                precio = input("Precio por m2: ")
                lotes.registrar_lote(cod, urb, area, precio)
                print("Lote registrado correctamente.")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "2":
            todos = lotes.listar_lotes()
            print("\n--- LOTES ---")
            for cod, datos in todos.items():
                print(f"{cod} | {datos['urbanizacion']} | {datos['area']}m2 | S/{datos['precio_m2']} | Estado: {datos['estado']}")

        elif opcion == "3":
            try:
                cod = input("Código del lote a comprar: ")
                nombre = input("Nombre del comprador: ")
                doc = input("Documento de identidad: ")
                venta = ventas.registrar_venta(cod, nombre, doc)
                print("\n¡Venta registrada con éxito!")
                print(f"Total: S/{venta['precio_total']} | Cuota Inicial: S/{venta['cuota_inicial']} | Saldo: S/{venta['saldo']}")
            except Exception as e:
                print(f"Error en la venta: {e}")

        elif opcion == "4":
            lista = ventas.listar_ventas()
            print("\n--- RESUMEN DE VENTAS ---")
            for v in lista:
                print(f"Lote: {v['lote']} | Comprador: {v['comprador']} | Total: S/{v['precio_total']} | Inicial: S/{v['cuota_inicial']} | Saldo: S/{v['saldo']}")

        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()