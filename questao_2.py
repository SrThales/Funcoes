#O algoritmo a seguir serve de exercício para o uso de funções e confirma o meu domínio do 
#assunto. Ele é bastante semelhante a um exercício presente em um outro repositório meu, onde
#devo calcular o uso de combustível de um automóvel que em consumo de 12km/L. Devo utilizar 4
#funções: ler e retornar valores, cálculo de distância, cálculo de quantidade de litros e 
#apresentação de resultado

#São fornecidas duas fórmulas:
    #cálculo de distância percorrida: DISTANCIA = TEMPO * VELOCIDADE
    #cálculo de litros de combustível utilizados: LITROS_USADOS = DISTANCIA / 12
    
#declarando variáveis:    
aux1 = 0
aux2 = 0  
aux3 = 0

def ler_valores():
    TEMPO = float(input('Defina o tempo (em minutos) gasto na viagem:'))
    VELOCIDADE = float(input('Defina a velocidade média (em kilometros) durante a viagem:'))
    return TEMPO, VELOCIDADE

valores = ler_valores()
horas = (valores[0])/60
vmed = valores[1]
print("A viagem teve duração de", horas, "hora(s) e a velocidade média foi de", vmed, "km/h")

def calc_dist(horas, vmed):
    aux1 = horas
    aux2 = vmed
    distancia = aux1*aux2
    return distancia

DISTANCIA = calc_dist(horas, vmed)

print("A distância percorrida foi de", DISTANCIA, "km")

def calc_litros(DISTANCIA):
    aux3 = DISTANCIA
    litros = aux3/12
    return litros

LITROS = calc_litros(DISTANCIA)

def resultado(LITROS):
    print("E, portanto, a quantidade de litros gastos foi de: ", LITROS)
    
resultado(LITROS)
    


    






