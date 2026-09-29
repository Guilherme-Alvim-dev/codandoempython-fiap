print("1_Estudante")
print("2_TRABALHADOR")
print("3_IDOSO")
print("4_COMUM")

tipo = int(input("Você é: "))
tarifa = 2.50

if 1 <= tipo <= 4:
    km_percorrido = float(input("Escrava quantos km percorrido: "))
    valor = tarifa * km_percorrido
    match valor:
        case 1:
            if tipo == 1:
                total = tarifa * 0.5
        case 2:
            if tipo == 2:
                total = tarifa * 0.2
        case 3:
            if tipo == 3:
                total = tarifa * 0.0
        case 4:
            if tipo == 4:
                total = tarifa * 1
    if valor > 0:
        print(f"Total a pagar é {valor:.2f}")
else:
    print("Opção inválida")

