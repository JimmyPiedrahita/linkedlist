public class Nodo<T> {
    T valor;
    Nodo<T> siguiente;
    Nodo<T> anterior;

    public Nodo(T valor) {
        this.valor = valor;
        this.siguiente = null;
        this.anterior = null;
    }

    @Override
    public String toString() {
        return "Nodo(" + valor + ")";
    }
}
