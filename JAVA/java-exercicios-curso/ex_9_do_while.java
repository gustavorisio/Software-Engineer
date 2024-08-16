/*
Este código foi digitado por Gustavo Di Risio | github.com/gustavorisio | linkedin.com/in/gustavorisio
*/
/*
    O comando do-while executa o comando enquanto condição for avaliada como true. 
    A diferença em relação ao comando while é que a condição é testada após a execução do comando.
    Este código abaixo é a soma dos 100 primeiros números inteiros com do-while. O valor de x após o loop é: 4950.
*/
public class ex_9_do_while {
    public static void main(String[] args) {
    int i = 1;
    int x = 0;
    do
    x +=i++;
    while(i<100);
    System.out.println("O valor de x após o loop é: " + x);
}
}