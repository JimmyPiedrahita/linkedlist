public class Lista<T> {

    Nodo<T> cabeza = null;
    Nodo<T> cola = null;

    public void agregarNodoInicio(T valor) {
        Nodo<T> nodoActual = new Nodo<>(valor);
        if (cabeza == null) {
            cabeza = nodoActual;
            cola = nodoActual;
            return;
        }
        cabeza.anterior = nodoActual;
        nodoActual.siguiente = cabeza;
        cabeza = nodoActual;
    }

    public void agregarNodoFinal(T valor) {
        Nodo<T> nuevoNodo = new Nodo<>(valor);
        if (cabeza == null) {
            cabeza = nuevoNodo;
            cola = nuevoNodo;
            return;
        }
        Nodo<T> nodoActual = cabeza;
        while (nodoActual.siguiente != null) {
            nodoActual = nodoActual.siguiente;
        }
        nuevoNodo.anterior = nodoActual;
        nodoActual.siguiente = nuevoNodo;
        cola = nuevoNodo;
    }

    public void agregarNodoConPosicion(T valor, T valorRefencia) {
        Nodo<T> nuevoNodo = new Nodo<>(valor);
        Nodo<T> nodoActual = cabeza;
        while (nodoActual != null) {
            if (nodoActual.valor == valorRefencia) {
                if (nodoActual == cola) {
                    nodoActual.siguiente = nuevoNodo;
                    nuevoNodo.anterior = nodoActual;
                    cola = nuevoNodo;
                    return;
                }
                nodoActual.siguiente.anterior = nuevoNodo;
                nuevoNodo.siguiente = nodoActual.siguiente;
                nuevoNodo.anterior = nodoActual;
                nodoActual.siguiente = nuevoNodo;
                return;
            }
            nodoActual = nodoActual.siguiente;
        }
        System.out.println("No encontrado");
    }

    public void imprimirLista() {
        Nodo<T> nodoActual = cabeza;
        while (nodoActual != null) {
            System.out.println(nodoActual.toString());
            nodoActual = nodoActual.siguiente;
        }
    }

}
