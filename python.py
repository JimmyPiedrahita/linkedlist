class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

    def __str__(self):
        return f"Nodo({self.valor})"


class Lista:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregarNodoInicio(self, valor):
        nuevoNodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevoNodo
            return
        self.cabeza.anterior = nuevoNodo
        nuevoNodo.siguiente = self.cabeza
        self.cabeza = nuevoNodo

    def agregarNodoFinal(self, valor):
        nuevoNodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevoNodo
            return
        self.cola.siguiente = nuevoNodo
        nuevoNodo.anterior = self.cola
        self.cola = nuevoNodo

    def agregarNodoConPosicion(self, valor, valorReferencia):
        nuevoNodo = Nodo(valor)
        if self.cabeza is None:
            print("Lista vacia")
            return
        nodoActual = self.cabeza
        while nodoActual is not None:
            if nodoActual.valor == valorReferencia:
                if nodoActual == self.cola:
                    nodoActual.siguiente = nuevoNodo
                    nuevoNodo.anterior = nodoActual
                    self.cola = nuevoNodo
                    return
                nodoActual.siguiente.anterior = nuevoNodo
                nuevoNodo.siguiente = nodoActual.siguiente
                nuevoNodo.anterior = nodoActual
                nodoActual.siguiente = nuevoNodo
                return
            nodoActual = nodoActual.siguiente
        print("No encontrado")

    def eliminarNodo(self, valorReferencia):
        if self.cabeza is None:
            return
        nodoActual = self.cabeza
        while nodoActual is not None:
            if nodoActual.valor == valorReferencia:
                if nodoActual == self.cabeza and nodoActual == self.cola:
                    self.cabeza = self.cola = None
                    return
                if nodoActual == self.cabeza:
                    self.cabeza = nodoActual.siguiente
                    self.cabeza.anterior = None
                    return
                if nodoActual == self.cola:
                    self.cola = nodoActual.anterior
                    self.cola.siguiente = None
                    return
                nodoActual.anterior.siguiente = nodoActual.siguiente
                nodoActual.siguiente.anterior = nodoActual.anterior
                return
            nodoActual = nodoActual.siguiente

    def imprimirLista(self):
        nodoActual = self.cabeza
        while nodoActual is not None:
            print(nodoActual)
            nodoActual = nodoActual.siguiente

if __name__ == "__main__":
    lista = Lista()

    lista.agregarNodoInicio(1)
    lista.agregarNodoInicio(2)
    lista.agregarNodoInicio(3)
    lista.agregarNodoFinal(0)
    lista.agregarNodoInicio(10)
    lista.agregarNodoConPosicion(5, 2)
    lista.agregarNodoConPosicion(100, 0)
    lista.agregarNodoConPosicion(77, 100)
    
    lista.imprimirLista()
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

    def __str__(self):
        return f"Nodo({self.valor})"


class Lista:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregarNodoInicio(self, valor):
        nuevoNodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevoNodo
            return
        self.cabeza.anterior = nuevoNodo
        nuevoNodo.siguiente = self.cabeza
        self.cabeza = nuevoNodo

    def agregarNodoFinal(self, valor):
        nuevoNodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevoNodo
            return
        self.cola.siguiente = nuevoNodo
        nuevoNodo.anterior = self.cola
        self.cola = nuevoNodo

    def agregarNodoConPosicion(self, valor, valorReferencia):
        nuevoNodo = Nodo(valor)
        if self.cabeza is None:
            print("Lista vacia")
            return
        nodoActual = self.cabeza
        while nodoActual is not None:
            if nodoActual.valor == valorReferencia:
                if nodoActual == self.cola:
                    nodoActual.siguiente = nuevoNodo
                    nuevoNodo.anterior = nodoActual
                    self.cola = nuevoNodo
                    return
                nodoActual.siguiente.anterior = nuevoNodo
                nuevoNodo.siguiente = nodoActual.siguiente
                nuevoNodo.anterior = nodoActual
                nodoActual.siguiente = nuevoNodo
                return
            nodoActual = nodoActual.siguiente
        print("No encontrado")

    def eliminarNodo(self, valorReferencia):
        if self.cabeza is None:
            return
        nodoActual = self.cabeza
        while nodoActual is not None:
            if nodoActual.valor == valorReferencia:
                if nodoActual == self.cabeza and nodoActual == self.cola:
                    self.cabeza = self.cola = None
                    return
                if nodoActual == self.cabeza:
                    self.cabeza = nodoActual.siguiente
                    self.cabeza.anterior = None
                    return
                if nodoActual == self.cola:
                    self.cola = nodoActual.anterior
                    self.cola.siguiente = None
                    return
                nodoActual.anterior.siguiente = nodoActual.siguiente
                nodoActual.siguiente.anterior = nodoActual.anterior
                return
            nodoActual = nodoActual.siguiente

    def imprimirLista(self):
        nodoActual = self.cabeza
        while nodoActual is not None:
            print(nodoActual)
            nodoActual = nodoActual.siguiente

if __name__ == "__main__":
    lista = Lista()

    lista.agregarNodoInicio(1)
    lista.agregarNodoInicio(2)
    lista.agregarNodoInicio(3)
    lista.agregarNodoFinal(0)
    lista.agregarNodoInicio(10)
    lista.agregarNodoConPosicion(5, 2)
    lista.agregarNodoConPosicion(100, 0)
    lista.agregarNodoConPosicion(77, 100)
    
    lista.imprimirLista()