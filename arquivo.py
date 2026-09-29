'''
with open("clientes.txt", "r") as arquivo:
    cli = {}
    for linha in arquivo:
        dados = linha.split(",")
        cod = dados[0]
        nome = dados[1]
        compras = [float(dados[2]), float(dados[3])]
        cli[cod] = {"nome":nome, "compras":compras}
    print(cli)
'''

