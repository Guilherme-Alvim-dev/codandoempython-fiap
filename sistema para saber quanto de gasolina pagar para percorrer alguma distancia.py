distancia = float(input("Digite quantos km foi percorrido com o carro: "))
litro = float(input("Digite quantos litros de gasolina foi consumido pelo carro: "))
preço_gasolina = float(input("Quanto está a gasolina: "))
km_desejada = int(input("Quantos km você deseja percorrer?: "))
consumo = distancia / litro
print(consumo)
km_por_real = preço_gasolina / consumo
print(km_por_real)
fazer_km = km_por_real * km_desejada
print(fazer_km)
print(f'Para percorrer {km_desejada}, você terá que pagar {fazer_km:.2f} ')