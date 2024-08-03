#O código a seguir calcula o preço de ida e volta da viagem com base no valor atual da gasolina
#em sua cidade

preco_gasolina = float(input('Insira o valor da gasolina:'))
distancia = float(input('Insira a kilometragem até o destino:'))

litros = distancia/13
valor = round(litros*preco_gasolina*2)

print('O valor investido na viagem (ida e volta) é de', valor, 'reais')