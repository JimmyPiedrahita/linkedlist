public class Lista<T> {

    private Nodo<T> cabeza = null;
    private Nodo<T> cola = null;

    public Nodo<T> getCabeza() {
        return cabeza;
    }

    public void setCabeza(Nodo<T> cabeza) {
        this.cabeza = cabeza;
    }

    public Nodo<T> getCola() {
        return cola;
    }

    public void setCola(Nodo<T> cola) {
        this.cola = cola;
    }

    public void agregarNodoInicio(T valor) {
        Nodo<T> nodoActual = new Nodo<>(valor);
        if (cabeza == null) {
            cabeza = nodoActual;
            cola = nodoActual;
            return;
        }
        cabeza.setAnterior(nodoActual);
        nodoActual.setSiguiente(cabeza);
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
        while (nodoActual.getSiguiente() != null) {
            nodoActual = nodoActual.getSiguiente();
        }
        nuevoNodo.setAnterior(nodoActual);
        nodoActual.setSiguiente(nuevoNodo);
        cola = nuevoNodo;
    }

    public void agregarNodoConPosicion(T valor, T valorRefencia) {
        Nodo<T> nuevoNodo = new Nodo<>(valor);
        if (cabeza == null) {
            cabeza = nuevoNodo;
            cola = nuevoNodo;
            return;
        }
        Nodo<T> nodoActual = cabeza;
        while (nodoActual != null) {
            if (nodoActual.getValor() == valorRefencia) {
                if (nodoActual == cola) {
                    nodoActual.setSiguiente(nuevoNodo);
                    nuevoNodo.setAnterior(nodoActual);
                    cola = nuevoNodo;
                    return;
                }
                nodoActual.getSiguiente().setAnterior(nuevoNodo);
                nuevoNodo.setSiguiente(nodoActual.getSiguiente());
                nuevoNodo.setAnterior(nodoActual);
                nodoActual.setSiguiente(nuevoNodo);
                return;
            }
            nodoActual = nodoActual.getSiguiente();
        }
        System.out.println("No encontrado");
    }

    public void eliminarNodo(T valorReferencia) {
        if (cabeza == null) return;
        Nodo<T> nodoActual = cabeza;
        while (nodoActual != null) {
            if (nodoActual.getValor() == valorReferencia) {
                if (nodoActual == cabeza) {
                    if (nodoActual.getSiguiente() == null) {
                        cabeza = null;
                        return;
                    }
                    cabeza = nodoActual.getSiguiente();
                    cabeza.setAnterior(null);
                    return;
                }
                if (nodoActual == cola) {
                    cola = nodoActual.getAnterior();
                    cola.setSiguiente(null);
                    return;
                }
                nodoActual.getAnterior().setSiguiente(nodoActual.getSiguiente());
                nodoActual.getSiguiente().setAnterior(nodoActual.getAnterior());
                return;
            }
            nodoActual = nodoActual.getSiguiente();
        }
        System.out.println("No encontrado");
    }

    public void imprimirLista() {
        Nodo<T> nodoActual = cabeza;
        while (nodoActual != null) {
            System.out.println(nodoActual.toString());
            nodoActual = nodoActual.getSiguiente();
        }
    }
}
