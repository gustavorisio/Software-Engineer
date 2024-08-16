/*
Este código foi digitado por Gustavo Di Risio | github.com/gustavorisio | linkedin.com/in/gustavorisio
*/
/*
    Os comandos de repetição, ou de iteração, executam um comando ou um bloco de comandos várias vezes. É uma das formas para executar repetidamente um comando. 
    A outra é a recursão que é a chamada direta ou indireta de um método durante a execução do próprio método. Em Java existem três formas de comandos de repetição: 
    o while; o do-while; e o for.
    Este código abaixo é a soma dos 100 primeiros números inteiros. O valor de x após o loop é: 5050.
*/
public class ex_08_while {
    public static void main(String[] args) {
        int i = 1;
        int x = 0;
        /* Se for necessário executar mais de um comando deve-se agrupá-los por meio de delimitadores de bloco */
        while (i <= 100)
            x += i++;
            
        System.out.println("O valor de x após o loop é: " + x);
    }
    
}
