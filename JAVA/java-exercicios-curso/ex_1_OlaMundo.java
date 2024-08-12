/*
Este código foi digitado por Gustavo Di Risio | github.com/gustavorisio | linkedin.com/in/gustavorisio
*/
/*

    Este programa é composto por uma única classe que possui apenas dois métodos. 
    Isto é importante, porque não é possível fazer um programa Java sem recorrer às classes, uma vez que os procedimentos são definidos como métodos de classes.
    Se você olhar os programas “OlaMundo” mostrados em outros livros sobre Java irá notar que o programa apresentado aqui é um pouco mais complicado.
    Geralmente este programa inicial é apresentado apenas com um método: o método main(). A razão de eu ter usado uma abordagem diferente é que desejamos desenvolver um hábito saudável na programação em Java.
    
 */

public class ex_1_OlaMundo {

    public void exibeOla() {
        System.out.println("Ola, Mundo!");
    }

    public static void main(String args[]) {
        ex_1_OlaMundo obj = new ex_1_OlaMundo();
        obj.exibeOla();
    }
}
