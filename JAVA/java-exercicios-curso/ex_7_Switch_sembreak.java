/*
Este código foi digitado por Gustavo Di Risio | github.com/gustavorisio | linkedin.com/in/gustavorisio
*/
/* 
   O comando switch é útil quando existem várias ações distintas que
   precisam ser realizadas em função do resultado da avaliação de uma expressão.
   Não é nada que não poderia ser feito com um conjunto de if-else, no entanto o
   uso do switch facilita codificação e a legibilidade do programa.

   Neste código mostra as saídas de um programa com um comando switch que não faz uso do comando break. 
   Note que todos os comandos são executados, uma vez que não existe um comando break para interromper a execução.
   A omissão do comando break pode ser útil para poupar digitação naqueles casos onde mais de uma opção precisa executar a mesma sequência de comandos.
 */
public class ex_7_Switch_sembreak {
   public static void main (String args[]) {
       char letra = 'e';
       switch(letra)
       {
       case 'i': System.out.println("inserir");
       case 'a': System.out.println("alterar");
       case 'e': System.out.println("excluir");
       default: System.out.println(
               "Ação ignorada: "+letra);
       }
     }
}
