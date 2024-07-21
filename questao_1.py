#O algoritmo a seguir serve como exercício e comprova mues conhecimentos a respeito do uso 
#de funções em python

#O objetivo do exercício é ler uma temperatura em graus celcius e apresentá-la em fahrenheit
#utilizando 3 funções: leitura e retorno do valor da temperatura, função para cálculo de conver-
#são e função para mostrar o resultado

#A fórmula de conversão é a seguinte: F = (9 * C + 160) / 5, onde F é ferenheit e C é celcius

def ler_temperatura():
    aux1 = int(input('Defina o valor da temperatura em graus Celcius:'))
    print('O valor da temperatura, digitada, em graus Celsius é:', aux1)
    return aux1

temperatura = ler_temperatura()

def calculo(valor):
    C = valor
    aux2 = 0
    aux2 = ((9*C)+160)/5
    return aux2

def resultado(valor_de_F):
    print('O resultado em graus Fahrenheits é:', F)
    
calculo(temperatura)
F = calculo(temperatura)
resultado(F)



