/*
Este código foi digitado por Gustavo Di Risio | github.com/gustavorisio | linkedin.com/in/gustavorisio
*/
/*

   Acredito que os operadores binários para adição, subtração, multiplicação, divisão e concatenação de Strings não necessitam maiores explicações.
   O operador de módulo (%) retorna o resto da divisão entre dois operandos inteiros. 
   Os operadores &, | e ^ implementam operações orientada para bits, operações que atuam sobre os bits individuais dos operandos. 
   O operador & realiza a operação lógica E entre cada bit individual dos operandos.
   O operador | realiza a operação lógica OU entre cada bit individual dos operandos.
   O operador ^ realiza a operação lógica XOU (ou exclusivo) entre cada bit individual dos operandos.
   Os operadores <<, >> e >>> implementam operações de deslocamento de bits. 
   Os bits do operando à esquerda serão deslocados o número de posições especificadas pelo operando à direita. 
   Os bits que saem dos limites do campo são perdidos e a variável é preenchida com zeros no lado oposto ao deslocamento.  
   O operador << realiza a operação de deslocamento de bits a esquerda. 
   Os operadores >> e >>> realizam a operação de deslocamento de bits a direita. A diferença entre o operador >> e o >>> é que o primeiro não desloca o bit de mais alta ordem usado para indicar números negativos. 
   
   O programa abaixo mostra o uso desses operadores:
 */

public class ex_3_binarios {
  public static void main(String args[]) {
    int x = 7, y = -7;
    System.out.println("x = " + x);
    System.out.println("y = " + y);
    System.out.println("x << 1= " + (x << 1));
    System.out.println("x >> 2= " + (x >> 2));
    System.out.println("y >> 2= " + (y >> 2));
    System.out.println("y >>> 31= " + (y >>> 31));
  }
}