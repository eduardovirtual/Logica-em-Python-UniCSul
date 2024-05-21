# Estrutura de dados Listas com Tuplas ()... (Também conhecidas como Vetores ou Arrays)
# As Tuplas possuem valores IMUTÁVEIS (Não podem ser atualizados ou excluídos)
# No exemplo a seguir, veremos a sintaxe das Tuplas em Python 

minhaTupla = (1,2,3,4,5)

# Acessando elementos em uma Tupla:

print("----------Exercício 1-------------")

minhaTupla = ("João","Anna","Silva")
print(minhaTupla[1])

# Outra forma de acessar e visualizar elementos de uma tupla:

print("----------Exercício 2-------------")

minhaTupla = ("João","Anna","Silva")

for elemento in minhaTupla:
    print(elemento)

# Não há meios de atualizar ou mesmo excluir Tuplas por serem imutáveis
# Porém existe um meio de exclusão completa para uma Tupla a seguir:

print("----------Exercício 3-------------")

minhaTupla1 = ("João","Anna","Silva")
del minhaTupla1
# Fazendo isso, o código irá executar com erro, pois a Tupla foi deletada:
print(minhaTupla1) 
