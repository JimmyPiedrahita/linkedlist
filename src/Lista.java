public class Lista<T> {

    Nodo<T> cabeza = null;

    public void agregarNodoInicio(T valor) {
        Nodo<T> nodoActual = new Nodo<>(valor);
        if (cabeza == null) {
            cabeza = nodoActual;
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
            return;
        }
        Nodo<T> nodoActual = cabeza;
        while (nodoActual.siguiente != null) {
            nodoActual = nodoActual.siguiente;
        }
        nuevoNodo.anterior = nodoActual;
        nodoActual.siguiente = nuevoNodo;
    }

    public void imprimirLista() {
        Nodo<T> nodoActual = cabeza;
        while (nodoActual != null) {
            System.out.println(nodoActual.toString());
            nodoActual = nodoActual.siguiente;
        }
    }

}
