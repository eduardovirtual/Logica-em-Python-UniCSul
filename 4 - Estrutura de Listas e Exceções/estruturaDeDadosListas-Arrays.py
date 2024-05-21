# Estrutura de dados Listas []... (Também conhecidas como Vetores ou Arrays)
# No exemplo a seguir, veremos a sintaxe da Listas em Python

minhaLista = [1,2,3,4,5]


# É possível adicionar diferentes tipos de dados dentro de
# Uma única lista em Python, como no exemplo a seguir:

minhaLista2 = [1, "Santos", 4.5]

# Utilizamos ".append" para adicionar elementos
# dentro de uma lista

listaNomes = []
listaNomes.append("João")
listaNomes.append("Maria")
listaNomes.append("Ana")
listaNomes.append("Clara")

print("----------Exercício 1-------------")

listaNomes = []

while True:
    nome = input("Digite um nome: ")
    listaNomes.append(nome)

    continuar = input("Deseja continuar? Digite Sim ou Não: ")
    if(continuar=="Não" or continuar=="NÃO"):
        break

print(listaNomes)

# Acessando elementos dentro de uma lista:

print("----------Exercício 2-------------")

minhaLista = [1,2]
print(minhaLista[0])

# Mostrando os elementos de forma ordenada

print("----------Exercício 3-------------")

minhaLista3 = ["João","Maria","Anna","Silva"]

for elementos in minhaLista3:
    print(elementos)

# Atualizando elementos de uma Lista:

print("----------Exercício 4-------------")

minhaLista4 = [1, "Santos", 4.5]
minhaLista4[0] = 2
minhaLista4[1] = "Eduardo"
print(minhaLista4)

# Removendo elementos de uma Lista:
# O uso do ".pop" deleta o último elemento da lista

print("----------Exercício 5-------------")

minhaLista5 = ["Carlos","Júlio","Telma","Roberto"]
minhaLista5.pop()
print(minhaLista5)

# O uso constante do ".pop", faz com que delete
# sempre o último elemento de uma lista

print("----------Exercício 6-------------")

minhaLista6 = ["Luana","Rayssa","Luan","Ronaldo"]
minhaLista6.pop()
minhaLista6.pop()
minhaLista6.pop()
print(minhaLista6)

# O uso da função "remove()", pode deletar um
# elemento específico de uma Lista

print("----------Exercício 7-------------")

minhaLista7 = ["Reginaldo","Andréia","Pedro","Alves"]
minhaLista7.remove("Pedro")
print(minhaLista7)

# Funções de listas podem ser executadas diversas vezes:

print("----------Exercício 8-------------")

minhaLista8 = ["André","Rogério","John","Virginia"]
minhaLista8.pop()
minhaLista8.pop()
minhaLista8.append("Fernanda")
print(minhaLista8)

