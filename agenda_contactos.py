# ======================================================
# Tarea: Colecciones de Datos
# Estudiante: Heidy Guamán
# Fecha: 27 de septiembre de 2026
# Descripción: Programa que gestiona contactos usando
# lista, conjunto y diccionario en Python
# ======================================================

# -------------------
# 1. CREAR ESTRUCTURAS
# -------------------

# Lista para ordenar los nombres
lista_nombres = []

# Conjunto para evitar nombres repetidos
conjunto_nombres = set()

# Diccionario principal: Nombre → Teléfono
agenda = {}

# -------------------
# 2. FUNCIÓN: AGREGAR CONTACTO
# -------------------
def agregar_contacto(nombre, telefono):
    if nombre in conjunto_nombres:
        print(f"⚠️ El nombre '{nombre}' ya está registrado. No se repite.")
        return False
    else:
        conjunto_nombres.add(nombre)
        lista_nombres.append(nombre)
        agenda[nombre] = telefono
        print(f"✅ Contacto agregado: {nombre} → {telefono}")
        return True

# -------------------
# 3. FUNCIÓN: MOSTRAR TODOS
# -------------------
def mostrar_agenda():
    print("\n" + "="*40)
    print("📋 AGENDA DE CONTACTOS")
    print("="*40)
    if not agenda:
        print("La agenda está vacía.")
    else:
        for nombre in lista_nombres:
            print(f"👤 {nombre:15} → 📞 {agenda[nombre]}")
    print(f"\nTotal de contactos: {len(agenda)}")
    print("="*40 + "\n")

# -------------------
# 4. FUNCIÓN: BUSCAR CONTACTO
# -------------------
def buscar_contacto(nombre):
    if nombre in agenda:
        print(f"🔍 Encontrado: {nombre} → 📞 {agenda[nombre]}")
        return agenda[nombre]
    else:
        print(f"❌ '{nombre}' NO está en la agenda.")
        return None

# -------------------
# 5. FUNCIÓN: ELIMINAR CONTACTO
# -------------------
def eliminar_contacto(nombre):
    if nombre in agenda:
        del agenda[nombre]
        lista_nombres.remove(nombre)
        conjunto_nombres.remove(nombre)
        print(f"🗑️ Contacto '{nombre}' eliminado correctamente.")
        return True
    else:
        print(f"❌ No se puede eliminar: '{nombre}' no existe.")
        return False

# -------------------
# 6. PROGRAMA PRINCIPAL — PRUEBAS
# -------------------
if __name__ == "__main__":
    print("=== PROGRAMA DE GESTIÓN DE AGENDA ===")
    
    # Agregar contactos de ejemplo
    agregar_contacto("Maria", "0987654321")
    agregar_contacto("Juan", "0991234567")
    agregar_contacto("Luis", "0976543210")
    agregar_contacto("Maria", "0999999999")  # Prueba de duplicado
    
    # Mostrar todos
    mostrar_agenda()
    
    # Buscar un contacto
    buscar_contacto("Juan")
    buscar_contacto("Pedro")  # No existe
    
    # Eliminar un contacto
    eliminar_contacto("Luis")
    
    # Mostrar después de eliminar
    mostrar_agenda()