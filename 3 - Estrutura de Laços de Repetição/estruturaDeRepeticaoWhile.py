# Estrutura de Repetição (Loop) while ...
# A variável "i" refere-se a ITERAÇÃO ou CONTADOR

print("----------Exercício 1-------------")

contador = 0
while (contador < 5):
    contador+=1
    print(contador)

print("----------------------------------")

# Código executando, enquanto não for digitado "0"

print("----------Exercício 2-------------")

nome = ""
while True:
    texto = input("Digite um nome ou '0' para encerrar o programa: ")

    if(texto == "0"):
        print("Programa finalizado")
        break
    else:
        nome = nome + texto +"\n"

print(nome)

print("----------------------------------")

# Solução diferente do código anterior, com a condição
# de continuar usando, digitando "sim ou não"

print("----------Exercício 3-------------")

nome = ""
continuar = True
while continuar:
    nome = nome + input("Digite um nome: ") + "\n"

    x = input("Deseja continuar? Digite 'Sim' ou 'Não': ")

    if(x.upper() =="SIM"):
        continuar = True
    else:
        continuar = False

print(nome)

print("----------------------------------")

print("----------Exercício 4-------------")

contador = 0

while contador < 10:
    if(contador == 1 or contador == 3):
        contador+=1
        continue

    print(contador)
    contador+=1

print("----------------------------------")

# Exercício proposto como desafio
# Escreva um programa que leia um grupo de valores (não sabemos quantos são) para calcular e visualizar a
# média desses valores e, também, determinar e visualizar o maior deles. Utilize uma estrutura de repetição
# while ou for

print("----------Exercício 5-------------")

qtdValores = int(input("Digite quantos valores serão calculados: "))
# "contador" é a variável de ITERAÇÃO
contador = 0
# "valor" é a variável que ARMAZENA os valores digitados pelo usuário
valor = 0
while contador < qtdValores:
    valor += float(input("Digite um valor: "))
    contador+=1

media = valor/ contador
print(media)


print("----------------------------------")

# Solução para o desafio utilizando a estrutura de repetição "for":

print("----------Exercício 5.1-----------")

qtdValores = int(input("Digite a quantidade de números que serão calculados: "))
valor = 0
for contador in range(qtdValores):
    valor += float(input("Digite um valor: "))
    contador +=1

media = valor / contador
print(media)

