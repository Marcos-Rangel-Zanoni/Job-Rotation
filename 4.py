# As variáveis de velocidade dos veículos em km/h
velocidade_carro = 110
velocidade_caminhao = 80

# A distância entre as duas cidades em km
distancia_total = 100

# Calcula a distância até o ponto onde os veículos se cruzam
distancia_cruzamento = distancia_total / 2

# Calcula o tempo que cada veículo leva para chegar ao ponto de cruzamento
tempo_carro = distancia_cruzamento / velocidade_carro
tempo_caminhao = distancia_cruzamento / velocidade_caminhao + 0.1/60 * 2 # 0,1 min em horas x 2 para ambos pedágios

# Calcula a distância percorrida por cada veículo até o ponto de cruzamento
distancia_carro = velocidade_carro * tempo_carro
distancia_caminhao = velocidade_caminhao * tempo_caminhao

# Imprime a distância percorrida por cada veículo
print("Distância percorrida pelo carro:", distancia_carro, "km")
print("Distância percorrida pelo caminhão:", distancia_caminhao, "km")

# Verifica se ambos os veículos percorreram a mesma distância até o ponto de cruzamento
if distancia_carro == distancia_caminhao:
    print("O carro e o caminhão estarão equidistantes das duas cidades quando se encontrarem.")
else:
    print("Não é possível determinar qual veículo estará mais próximo de Ribeirão Preto quando eles se encontrarem.")
