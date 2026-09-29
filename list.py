'''
lista = [3, 10, 7, 8, 1, 9, 8, 5, 8]

menor_numero = lista[0]
maior_numero = lista[0]
for i in lista:
    if i < menor_numero:
        menor_numero = i
    if i > maior_numero:
        maior_numero = i
print(menor_numero)
print(maior_numero)
lista = [3, 10, 7, 8, 1, 9, 8, 5, 8]
soma = 0
for i in lista:
    soma += i
print(soma)
'''
lista = [1, 3, 10, 8, 7, 9, 5, 8]
for i in range(len(lista)):
    for j in range (len(lista)):
        if lista[i] < lista[j]:
            x = lista[i]
            lista[i] = lista[j]
            lista [j] = x
print(lista)

