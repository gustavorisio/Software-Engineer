/*
Este código foi digitado por Gustavo Di Risio | github.com/gustavorisio | linkedin.com/in/gustavorisio
*/
/* 
   O comando switch é útil quando existem várias ações distintas que precisam ser realizadas em função do resultado da avaliação de uma expressão.
   Não é nada que não poderia ser feito com um conjunto de if-else, no entanto o uso do switch facilita codificação e a legibilidade do programa.

   O comando switch avalia a expressão Expr e compara o valor resultante com todas as constantes colocadas após a palavra a chave case. A comparação é feita na ordem de cima para baixo e a primeira constante que igualar com o valor resultante da expressão faz com que os comandos após o ‘:’ sejam executados até o fim ou até que seja encontrado o comando break. A palavra chave default é opcional e ela serve como ponto de entrada para os comandos que serão executados caso o valor da expressão não seja igual a nenhuma das constantes.

    O comando break é muito importante na composição do switch. Ele faz com que a execução sequencial dos comandos seja interrompida para ser retomada no primeiro comando após o comando switch
 */
public class ex_6_Switch_combreak {
    public static void main (String args[]) {
      char letra = 'i';
      switch(letra)
      {
      case 'i': System.out.println("inserir");
      break;
      case 'a': System.out.println("alterar");
      break;
      case 'e': System.out.println("excluir");
      break;
      default:
        System.out.println(
                 "Ação ignorada: "+letra);
      }
   }
}
 