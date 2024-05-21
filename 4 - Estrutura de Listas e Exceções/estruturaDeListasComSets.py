# Sets em Listas Python servem para: remover duplicatas de uma lista ou
# verificar a presença de elementos em comum entre diferentes conjuntos (interseção)

print("----------Exercício 1-------------")

# Definindo uma lista com elementos duplicados
lista_com_duplicatas = [1, 2, 3, 1, 2, 4, 5, 3, 6]

# Convertendo a lista para um conjunto para remover as duplicatas
conjunto_sem_duplicatas = set(lista_com_duplicatas)

# Convertendo de volta para lista (opcional)
lista_sem_duplicatas = list(conjunto_sem_duplicatas)

# Imprimindo os resultados
print("Lista original:", lista_com_duplicatas)
print("Lista sem duplicatas:", lista_sem_duplicatas)

print("----------Exercício 2-------------")

# Definindo dois conjuntos
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

# Verificando a interseção entre os conjuntos
intersecao = conjunto1.intersection(conjunto2)

# Imprimindo o resultado
print("Interseção entre os conjuntos:", intersecao)

