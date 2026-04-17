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

def ver_gastos():
    """Muestra todos los gastos registrados."""
    gastos = cargar_gastos()
    
    if not gastos:
        print("\n📭 No hay gastos registrados aún.")
        return
    
    print("\n--- TODOS TUS GASTOS ---")
    for i, g in enumerate(gastos, 1):
        print(f"{i}. [{g['fecha']}] {g['descripcion']} "
              f"- ${g['monto']:.2f} ({g['categoria']})")


def ver_total():
    """Muestra el total gastado y desglose por categoría."""
    gastos = cargar_gastos()
    
    if not gastos:
        print("\n📭 No hay gastos registrados.")
        return
    
    total = sum(g["monto"] for g in gastos)
    
    # Agrupar por categoría
    por_categoria = {}
    for g in gastos:
        cat = g["categoria"]
        por_categoria[cat] = por_categoria.get(cat, 0) + g["monto"]
    
    print(f"\n💰 TOTAL GASTADO: ${total:.2f}")
    print("\nDesglose por categoría:")
    for cat, monto in sorted(por_categoria.items(), key=lambda x: -x[1]):
        porcentaje = (monto / total) * 100
        print(f"  {cat}: ${monto:.2f} ({porcentaje:.1f}%)")

def menu():
    while True:
        print("\n====== APP DE GASTOS ======")
        print("1. Registrar gasto")
        print("2. Ver todos los gastos")
        print("3. Ver total y desglose")
        print("4. Salir")
        opcion = input("Elige una opción: ").strip()
        
        if opcion == "1":
            registrar_gasto()
        elif opcion == "2":
            ver_gastos()
        elif opcion == "3":
            ver_total()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida.")


if __name__ == "__main__":
    menu()