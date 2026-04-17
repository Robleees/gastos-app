import json
import os
from datetime import datetime

ARCHIVO = "gastos.json"


def cargar_gastos():
    """Carga los gastos desde el archivo JSON."""
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_gastos(gastos):
    """Guarda la lista de gastos en el archivo JSON."""
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(gastos, f, indent=2, ensure_ascii=False)


def registrar_gasto():
    """Pide datos al usuario y registra un nuevo gasto."""
    print("\n--- Registrar nuevo gasto ---")
    descripcion = input("Descripción: ").strip()
    
    try:
        monto = float(input("Monto: $"))
    except ValueError:
        print("❌ Monto inválido. Debe ser un número.")
        return
    
    categoria = input("Categoría (comida/transporte/ocio/otros): ").strip().lower()
    
    gasto = {
        "descripcion": descripcion,
        "monto": monto,
        "categoria": categoria,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    
    gastos = cargar_gastos()
    gastos.append(gasto)
    guardar_gastos(gastos)
    
    print(f"✅ Gasto registrado: {descripcion} - ${monto}")


def menu():
    """Muestra el menú principal."""
    while True:
        print("\n====== APP DE GASTOS ======")
        print("1. Registrar gasto")
        print("2. Salir")
        opcion = input("Elige una opción: ").strip()
        
        if opcion == "1":
            registrar_gasto()
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida.")


if __name__ == "__main__":
    menu()