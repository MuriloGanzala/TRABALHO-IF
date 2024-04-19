import math

# Função para calcular o preço do estacionamento
def calcular_preco(chegada, partida):
    # Convertendo a chegada e partida para minutos
    minutos_chegada = chegada[0] * 60 + chegada[1]
    minutos_partida = partida[0] * 60 + partida[1]

    # Calculando o tempo de estacionamento em minutos
    tempo_estacionamento = minutos_partida - minutos_chegada

    # Calculando o número de horas a pagar arredondado por excesso
    horas_a_pagar = math.ceil(tempo_estacionamento / 60)

    # Calculando o preço com base nas tarifas
    if horas_a_pagar <= 2:
        preco = horas_a_pagar * 1.00
    elif 3 <= horas_a_pagar <= 4:
        preco = 2 * 1.00 + (horas_a_pagar - 2) * 1.40
    else:
        preco = 2 * 1.00 + 2 * 1.40 + (horas_a_pagar - 4) * 2.00

    return preco

# Entrada dos momentos de chegada e partida
chegada = tuple(map(int, input("Digite o momento de chegada (hora minuto): ").split()))
partida = tuple(map(int, input("Digite o momento de partida (hora minuto): ").split()))

# Calculando e exibindo o preço cobrado pelo estacionamento
preco_total = calcular_preco(chegada, partida)
print("O preço cobrado pelo estacionamento é R$", preco_total)
