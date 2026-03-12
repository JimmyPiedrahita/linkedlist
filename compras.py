import os

# ==========================================
# CAPA 1: ESTRUCTURAS BASE (Lógica Pura)
# ==========================================

class Nodo:
    def __init__(self, nombre_producto, precio=0.0):
        self.nombre = nombre_producto
        self.precio = precio
        self.siguiente = None

class ColaCompras:
    def __init__(self):
        self.frente = None
        self.final = None

    def encolar(self, nombre_producto):
        nuevo_nodo = Nodo(nombre_producto)
        if self.final is None:
            self.frente = self.final = nuevo_nodo
            return
        self.final.siguiente = nuevo_nodo
        self.final = nuevo_nodo

    def desencolar(self):
        if self.frente is None:
            return None
        nodo_extraido = self.frente
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        return nodo_extraido

class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def agregar(self, nombre_producto, precio):
        nuevo_nodo = Nodo(nombre_producto, precio)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def buscar_precio(self, nombre_producto):
        actual = self.cabeza
        while actual is not None:
            if actual.nombre.lower() == nombre_producto.lower():
                return actual.precio
            actual = actual.siguiente
        return float('inf') 

    # Modificación Arquitectónica: Ya no imprime, ahora retorna una lista nativa 
    # solo para que la Interfaz pueda iterar y mostrar los datos.
    def obtener_datos(self):
        datos = []
        actual = self.cabeza
        while actual:
            datos.append(f"[{actual.nombre.capitalize()} : ${actual.precio}]")
            actual = actual.siguiente
        return datos

# ==========================================
# CAPA 2: LÓGICA CENTRAL (El Motor)
# ==========================================

def motor_de_comparacion(cola_usuario, alm1, alm2, alm3):
    lista_salida_1 = ListaSimple()
    lista_salida_2 = ListaSimple()
    lista_salida_3 = ListaSimple()
    no_encontrados = []

    while True:
        item = cola_usuario.desencolar()
        if item is None:
            break

        p1 = alm1.buscar_precio(item.nombre)
        p2 = alm2.buscar_precio(item.nombre)
        p3 = alm3.buscar_precio(item.nombre)

        menor_precio = min(p1, p2, p3)

        if menor_precio == float('inf'):
            no_encontrados.append(item.nombre)
            continue

        if menor_precio == p1:
            lista_salida_1.agregar(item.nombre, p1)
        elif menor_precio == p2:
            lista_salida_2.agregar(item.nombre, p2)
        else:
            lista_salida_3.agregar(item.nombre, p3)

    return lista_salida_1, lista_salida_2, lista_salida_3, no_encontrados

# ==========================================
# CAPA 3: INTERFAZ DE USUARIO (CLI Interactiva)
# ==========================================

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_lista_en_ui(nombre_almacen, lista):
    datos = lista.obtener_datos()
    if not datos:
        print(f"  -> {nombre_almacen}: [Vacío]")
    else:
        print(f"  -> {nombre_almacen}: " + " -> ".join(datos))

def iniciar_interfaz():
    # Instancias en memoria
    almacen1 = ListaSimple()
    almacen2 = ListaSimple()
    almacen3 = ListaSimple()
    mi_carrito = ColaCompras()

    while True:
        print("\n" + "="*40)
        print("  SISTEMA DE ASISTENCIA DE COMPRAS  ")
        print("="*40)
        print("--- Módulo de Administración ---")
        print("1. Ingresar producto a Almacén 1")
        print("2. Ingresar producto a Almacén 2")
        print("3. Ingresar producto a Almacén 3")
        print("\n--- Módulo del Usuario ---")
        print("4. Agregar producto al Carrito (Cola)")
        print("5. PROCESAR Y OPTIMIZAR RUTAS")
        print("6. Salir")
        print("="*40)
        
        opcion = input("Seleccione una opción: ")

        if opcion in ['1', '2', '3']:
            prod = input("Nombre del producto: ")
            try:
                precio = float(input(f"Precio de '{prod}': $"))
                if opcion == '1': almacen1.agregar(prod, precio)
                elif opcion == '2': almacen2.agregar(prod, precio)
                elif opcion == '3': almacen3.agregar(prod, precio)
                print("✅ Producto registrado exitosamente en el catálogo.")
            except ValueError:
                print("❌ Error: Ingrese un precio numérico válido.")

        elif opcion == '4':
            prod = input("¿Qué producto necesita comprar?: ")
            mi_carrito.encolar(prod)
            print(f"✅ '{prod}' añadido a la cola de compras.")

        elif opcion == '5':
            print("\n⚙️ Procesando solicitud...")
            out1, out2, out3, perdidos = motor_de_comparacion(mi_carrito, almacen1, almacen2, almacen3)
            
            print("\n" + "*"*40)
            print("       RUTAS OPTIMIZADAS (SALIDA)      ")
            print("*"*40)
            mostrar_lista_en_ui("Comprar en Almacén 1", out1)
            mostrar_lista_en_ui("Comprar en Almacén 2", out2)
            mostrar_lista_en_ui("Comprar en Almacén 3", out3)
            
            if perdidos:
                print("\n⚠️ Productos no encontrados en ningún almacén:")
                for p in perdidos:
                    print(f"  - {p}")
            
            print("*"*40)
            input("\nPresione Enter para continuar y limpiar el carrito...")
            # Al continuar, la cola ya está vacía por el desencolado, el ciclo puede reiniciar.

        elif opcion == '6':
            print("Saliendo del sistema...")
            break
        else:
            print("❌ Opción no válida.")

# Arrancar el programa
if __name__ == "__main__":
    iniciar_interfaz()