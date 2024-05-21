# Estruturas de decisão (if, else, elif)
print("Exercício 1:")
# Estrutura if ... (Desvio condicional simples)

a = 3
b = 4
soma = a+b

if (soma > 6):
    print("Aluno aprovado")

print("--------------------------------")

print("Exercício 2:")
# Estrutura if ... else (Desvio condicional composto)

x = 4
y = 3
soma = x+y

if (soma >= 8):
    print("Aluno aprovado")
else:
    print("Aluno reprovado")

print("--------------------------------")

print("Exercício 3:")
# Estrutura if ... elif

a = 1
b = 3
soma = a+b

if (soma > 6):
    print("Aluno aprovado")
elif (soma > 2):
    print("Aluno pode realizar prova de recuperação")

print("--------------------------------")

print("Exercício 4:")
# Estruturas de Decisão Aninhadas / Encadeadas

a = 1
b = 5
frequencia = 80

if (frequencia > 75):
    soma = a+b
    if(soma > 6):
         print("Aluno aprovado")
    elif(soma > 2):
        print("Aluno pode realizar prova de recuperação")
    else:
        print("Aluno reprovado")
# O "else" logo abaixo, refere-se ao bloco de instruções do "if" em: (frequenca > 75)
# Ou seja, se o "if" for verdadeiro, ele procede com a aplicação linha por linha,
# Se não, ele vai direto para o else abaixo, concluindo a aplicação
else:
    print("Aluno reprovado direto")

