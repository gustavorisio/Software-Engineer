/*
Este código foi digitado por Gustavo Di Risio | github.com/gustavorisio | linkedin.com/in/gustavorisio
*/
/*

    Os operadores booleanos atuam sobre valores booleanos e retornam um valor booleano.
    E                   { & }
    OU                  { | }
    OU Exclusivo        { ^ }
    E Curto circuito    { && } 
    OU Curto circuito   { || }
    Negação             { ! }
    Igualdade           { == }
    Condicional         { ?: }

    O operador condicional atua sobre três operandos: uma expressão condicional e duas outras expressões quaisquer. A forma geral do operador é
    <condição> ? <expressão 1> : <expressão 2>.
    Se <condição> for avaliada como true, então o resultado da aplicação do operador condicional será o retorno da avaliação da <expressão 1>. Caso
    contrário o resultado da avaliação da <expressão 2> será retornado. O programa abaixo ilustra o uso deste operador:
    
 */
public class ex_5_booleanos {
    public static void main(String args[]) {
        int x = 5;
        boolean par = (x % 2 == 0) ? true : false;
        System.out.println("x = " + x);
        System.out.println("É par = " + par);
    }
}
