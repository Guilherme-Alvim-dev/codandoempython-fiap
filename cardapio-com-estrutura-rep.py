resp = "sim"
valor = 0
cont = 1
while resp == "sim":
    print("MENU")
    print("1_COMIDA")
    print("2_BEBIDA")
    print("3_SAIR")
    opc = int(input("O que você deseja do menu?: "))

    match opc:
        case 1:
            comida = int(input("Digite:1 para selecionar cachorro quente (R$15.00) Digite:2 para selecionar batata frita: (10.00R$): "))
            if comida == 1 or comida == 2:
                quantidade = int(input("Quantos vai querer: "))
                if comida == 1:
                    valor += 15 * quantidade
                else:
                    valor += 10 * quantidade
            else:
                print("Opção invalida")
        case 2:
            bebida = int(input("Digite:1 para Refri em lata R$12.00 Digite:2 para selecionar suco R$4.00: "))
            if bebida == 1 or bebida == 2:
                quantidade = int(input("Quantos vai querer: "))
                if bebida == 1:
                    valor += 12 * quantidade
                else:
                    valor += 6 * quantidade
            else:
                print("Opção invalida")
        case 3:
            print("Obrigado, volte sempre!")
            break
        case _:
            print("Opção inválida")
    if valor > 0:
        resp = input("deseja mais alguma coisa? sim ou não: ")
    resp == "sim"
print(f'O valor total do seu pedido é {valor:.2f}')
