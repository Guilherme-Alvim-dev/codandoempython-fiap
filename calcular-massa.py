'''
Calcular a densidade de um material com base em sua massa e volume. Fórmula: densidade = massa / volume

1) Obter as medidas (massa e volume)
2) Calcular a densidade com base na Fórmula acima
Restrições:
     - massa < 0 ou volume < 0 | volume != 0
3) Executar análise da densidade
    -função para execultar análise da densidade
    -executar funções dos itens 1 e 2 
    tratamento e exceções
'''

def obter_massa() -> float:
    massa = float(input(" massa do material em Kg:"))
def obter_volume() -> float:
    volume = float(input(" volume do material em m³: "))
    return obter_volume
def calcular_densidade(massa:float, volume:float) -> float:
    #Validação
    if massa < 0 or volume < 0:
        raise ValueError("[ValueError]: Massa e volume não podem ser NEGATIVOS")

    if volume == 0:
        raise ZeroDivisionError("[ZeroDivisionError: O volume do material não pode ser ZERO!]")
    densidade = massa / volume
def executar_analise_densidade() -> None:
    try:
        massa = obter_massa()
        volume = obter_volume()
        densidade = calcular_densidade(massa, volume)
    except ValueError as erro: 
        print(f"[ERRO de ENTRADA]: {erro}")
        print("DIvisão por zero impede o cálculo da densidade")
    except ZeroDivisionError as erro: 
        print(f"[ERRO FÍSICO]: {ERRO}")
        print("Divisão por zero impede o cálculo da densidade")
    else:
        print(f"\n [SUCESSO]: Densidade do material: {densidade:.2f} em kg/m³")
    finally:
        print("---Encerrando o ensaio")

#main 
while True: 
    executar_analise_densidade():
    print("\n")