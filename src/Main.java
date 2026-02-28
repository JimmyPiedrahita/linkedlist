public class Main {
    public static void main(String[] args) throws Exception {

        Lista<Integer> lista = new Lista<>();

        lista.agregarNodoInicio(1);
        lista.agregarNodoInicio(2);
        lista.agregarNodoInicio(3);
        lista.agregarNodoFinal(0);
        lista.agregarNodoInicio(10);

        lista.imprimirLista();
        System.out.println(lista.cola.valor);

    }
}
