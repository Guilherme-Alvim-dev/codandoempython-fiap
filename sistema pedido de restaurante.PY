'''
print("MENU")
print("1_COMIDA")
print("2_BEBIDA")
print("3_SAIR")
opc = int(input("O que você deseja do menu?: "))
valor = 0
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
    case _:
        print("Opção inválida")
if valor > 0:
    print(f'O valor total do seu pedido é {valor:.2f}')
'''

# listas principais
alunos = []
notas_alunos = []


# cadastrar alunos
def cadastrar_aluno():

    while True:

        nome = input("Digite o nome do aluno ou 'sair': ")

        if nome == "sair":
            break

        else:
            alunos.append(nome)
            notas_alunos.append([])
            print("Aluno cadastrado com sucesso!")


# registrar notas
def registrar_notas():

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    for i in range(len(alunos)):

        print(f"\nRegistrando notas de {alunos[i]}")

        while True:

            nota = input("Digite a nota ou 'fim': ")

            if nota == "fim":
                break

            else:
                notas_alunos[i].append(float(nota))


# calcular média
def calcular_media(notas):

    if len(notas) == 0:
        return 0

    soma = 0

    for nota in notas:
        soma += nota

    media = soma / len(notas)

    return media


# exibir média
def exibir_media():

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    nome = input("Digite o nome do aluno: ")

    encontrou = False

    for i in range(len(alunos)):

        if alunos[i] == nome:

            media = calcular_media(notas_alunos[i])

            print(f"Média de {nome}: {media:.2f}")

            if media >= 6:
                print("Aprovado")

            elif media >= 4:
                print("Exame")

            else:
                print("Reprovado")

            encontrou = True
            break

    if encontrou == False:
        print("Aluno não encontrado.")


# menu principal
def menu():

    while True:

        print("\n===== MENU =====")
        print("1 - Cadastrar aluno")
        print("2 - Registrar notas")
        print("3 - Calcular média")
        print("4 - Sair")

        opcao = int(input("Escolha uma opção: "))

        match opcao:

            case 1:
                cadastrar_aluno()

            case 2:
                registrar_notas()

            case 3:
                exibir_media()

            case 4:
                print("Programa encerrado.")
                break

            case _:
                print("Opção inválida")


# iniciar programa
menu()