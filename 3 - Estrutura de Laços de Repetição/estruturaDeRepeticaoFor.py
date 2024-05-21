# Estrutura de Repetição (Loop) for ...
# A variável "i" refere-se a ITERAÇÃO ou CONTADOR

print("----------Exercício 1-------------")

soma = 0
for i in (0,1,2,3,4):
    soma = soma + 3
    print(soma)

print("----------------------------------")

print("----------Exercício 2-------------")

for i in (2,5,9,56,4,58):
    print(i)

print("----------------------------------")

# Fazendo uma sequência finita com a função "range":

print("----------Exercício 3-------------")

for i in range(5):
    print(i)

print("----------------------------------")

print("----------Exercício 4-------------")

for i in range(10):
    print("Valor de i: " +str(i))

print("----------------------------------")

# A função "range" possui o seguinte comportamento:
# range(início,limite,passo) - referindo-se a números

print("----------Exercício 5-------------")

for i in range(0,15,2):
    print(i)

print("----------------------------------")

print("----------Exercício 6-------------")

for i in range(0,10,2):
    print("Valor de i: " +str(i))

print("----------------------------------")

# Utilizando o mesmo esquema de antes, porém em ordem decrescente

print("----------Exercício 7-------------")

for i in range(10,0,-2):
    print("Valor de i: " +str(i))

print("----------------------------------")

# Verificando números que são múltiplos/divisíveis por 3 em uma
# sequência numérica progressiva (de 0 a 30)

print("----------Exercício 8-------------")

qtdMultiplos = 0
for i in range(1,30):
    if(i%3==0):
        qtdMultiplos+=1
        print(i)

print("A quantidade de números divisíveis por 3 na sequência de 1 a 30 é: ",qtdMultiplos)

print("----------------------------------")

# É possível percorrer todos os caracteres contidos em uma
# variável com o valor do tipo String.

print("----------Exercício 9-------------")

minhaString = "ABCDEFGH"

for x in minhaString:
    print(x)

print("----------------------------------")

