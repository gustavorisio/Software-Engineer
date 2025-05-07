/*
Faça um programa para calcular o valor da viagem

Você tem 3 variaveis. Sendo elas:

1: Preço do combustivel;
2: Gasto médio do combustivel do carro em KM;
3: Distancia em KM da viagem;
*/

const precoCombustivel = 5.79;
const kmPorLitros = 12;
const distanciaEmKm = 1580;

//litros consumidos
const litrosconsumidos = distanciaEmKm / kmPorLitros;

//Valor gasto por litro
const valorGasto = litrosconsumidos * precoCombustivel;

console.log("O veiculo consumiu",litrosconsumidos.toFixed(2)," litros"); 
console.log("O valor gasto de combustivel foi de: R$",valorGasto.toFixed(2));