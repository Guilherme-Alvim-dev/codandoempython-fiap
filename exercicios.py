'''
#saber se o número é impar ou par
saber_numero = int(input("digite um número para saber se é impar ou par: "))
processo = (saber_numero % 2)
if processo == 0:
    print("seu número é par")
else:
    print("seu número é impar")

print("teste para saber se você tem desconto no seu ingresso")
idade = int(input("digite sua idade: "))

estudante = (input("Você é estudante? Responda sim ou não: "))
if idade >= 60 or estudante == "sim":
    print("Você tem direito a desconto")
else:
    print("Você não tem desconto")

salario_mensal = float(input('Insira seu salário_mensal: '))
horas_de_trabalho = 225
cal = (salario_mensal / horas_de_trabalho)
print(f"O valor da sua hora é: R${cal:.0f}")


digito_1 = int(input("Digite um número: "))
digito_2 = int(input("Digire outro número: "))
if digito_1 > digito_2:
    print(f"o número {digito_1} é o maior valor")
else:
    print(f"o número {digito_2} é o maior valor")

#Estruturas Condicionais py- exercícios
#exercício num_1
number = int(input("Digite um número: "))
if number > 0:
    print(f'O seu número foi automáticamente alterado pela metade: {number / 2:.0f}')
else:
    print(f'O seu número foi automáticamente alterado ao quadrado: {number ** 2}')
#exercício num_2
num_1 = int(input("Digite um número: "))
num_2 = int(input("Digite outro número: "))
if num_1 > num_2:
    diferenca = num_1 - num_2
    print(f'O número maior é {num_1}, com a diferença de {diferenca} a mais que o segundo número!  ')
else:
    diferenca = num_2 - num_1
    print(f'O número maior é {num_2}, com a diferença de {diferenca} a mais que o primeiro número!  ')
#exercício num_3
nota_1 = float(input("Insira a primeira nota: "))
nota_2 = float(input("Insira a segunda nota: "))
media = (nota_1 + nota_2) / 2
if media >= 0.0 and media <= 10.0:
    print(f'Sua média é {media:.2f}')
else:
    print("Nota inválida")

#exercício num_6
salario = float(input("Digite seu salário: "))
solicitacao_de_emprestimo = float(input("Digite valor da solicitação de emprestimo: "))
vinte_por_cento_do_salario = (salario) * 0.2

if vinte_por_cento_do_salario > solicitacao_de_emprestimo:
    print("Empréstimo não concebido")
else:
    print("Empréstimo concebido")
#exercício num_7
nota_1 = float(input("Insira a primeira nota: "))
nota_2 = float(input("Insira a segunda nota: "))
nota_3 = float(input("Insira a terceira nota: "))

nota_1_e_2 = (nota_1 + nota_2) * 2
media = nota_1_e_2 / 3
if media >= 6.0:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")

nota_lab = float(input("Insira a nota do Trabalho de laboratório: "))
nota_avaliacao_semestral = float(input("Insira a nota da avaliação semestral: "))
nota_exame_final = float(input("Insira a nota da Avaliação Final: "))

nota_lab_peso = (nota_lab) * 2
nota_avaliacao_semestral = (nota_avaliacao_semestral) * 3
nota_exame_final = (nota_exame_final) * 5

media = (nota_lab_peso) + (nota_avaliacao_semestral) + (nota_exame_final) /3
if media < 4.0:
    print("Aluno reprovado")
elif media >= 4.0 and media < 6:
    print("Aluno recuperação")
else:
    print("Aluno aprovado")

print("MENU")
print("1_SOMAR")
print("2_SUBTRAIR"
print("3_MULTIPLICAR")
print("4_DIVIDIR")
escolha = int(input("Qual operador deseja: "))
match escolha:
    case 1:
        num_1 = float(input("Insira o primeiro número: "))
        num_2 = float(input("Insira o segundo: "))
        cal = (num_1) + (num_2)
    print(cal)
'''
nome = (executor_electric)