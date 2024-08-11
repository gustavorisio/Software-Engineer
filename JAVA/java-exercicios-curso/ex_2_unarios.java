/*
Este código foi digitado por Gustavo Di Risio | github.com/gustavorisio | linkedin.com/in/gustavorisio
*/
/*

    Operadores unários.
    Os operadores de incremento e decremento (++ e --) aumentam e decrementam variáveis de tipo inteiro de uma unidade. 
    Estes operadores podem ser usados na forma prefixa ou pósfixa. 
    Na forma prefixa o operador modifica o valor da variável antes que o valor seja usado na expressão onde está a variável.
    Na forma pósfixa o operador modifica o valor da variável depois que o valor é usado na expressão onde está a variável.
    O operador de negação unário (-) é usado para mudar o sinal de um valor inteiro. 
    O operador de Complemento de bit (~) inverte cada bit da representação binária de um inteiro.

    O programa abaixo mostra o uso de cada operador unário.

 */
public class ex_2_unarios {

    public static void main(String args[]) {
        int x = 10, y = 0;
        System.out.println("x = " + x);
        System.out.println("y = " + y);
        System.out.println("++x = " + ++x);
        System.out.println("y++ = " + y++);
        System.out.println("x = " + x);
        System.out.println("y = " + y);
        System.out.println("-x = " + -x);
        System.out.println("~y = " + ~y);
    }
}
