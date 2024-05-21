# Dicionarios em Listas Python são utilizados para:
# mapear CHAVES únicas para VALORES correspondentes e são amplamente 
# utilizados para representar dados estruturados de forma flexível e eficiente
# Possuem uma sequência não ordenada de elementos e são mutáveis
# Exemplo de sintaxe:

meuDicionario = {"nome": "Eduardo Santos", "idade":22}

# Acessando elementos em um Dicionário:

print("----------Exercício 1-------------")

meuDicionario = {"nome": "Eduardo Santos", "idade":22}
print(meuDicionario["nome"])

# Atualizando um elemento no Dicionário:

print("----------Exercício 2-------------")

meuDicionario = {"nome": "Eduardo Santos", "idade":22}
meuDicionario["idade"] = 38

print(meuDicionario["idade"])

# Adicionando um elemento no Dicionário:

print("----------Exercício 3-------------")

meuDicionario = {"nome": "Eduardo Santos", "idade":22}

meuDicionario["email"] = "eduardosantos@gmail.com"
print(meuDicionario)

# Removendo um elemento no Dicionário:

print("----------Exercício 4-------------")

meuDicionario = {"nome": "Eduardo Santos", "idade":22, "email": "eduardosantos@gmail.com"}
meuDicionario.popitem()
print(meuDicionario)

# Removendo um elemento específico:

print("----------Exercício 5-------------")

meuDicionario = {"nome": "Eduardo Santos", "idade":22, "email": "eduardosantos@gmail.com"}
meuDicionario.pop("nome")
print(meuDicionario)
# Para excluir todos os elementos do dicionário, basta descrever a cláusula "del"

print("----------Exercício X-------------")

# Definindo um dicionário de mapeamento de nomes para idades
mapeamento_idades = {
    "Alice": 25,
    "Bob": 30,
    "Carol": 28,
    "David": 35
}

# Acessando valores no dicionário
print("Idade de Alice:", mapeamento_idades["Alice"])  # Saída: Idade de Alice: 25
print("Idade de Bob:", mapeamento_idades["Bob"])      # Saída: Idade de Bob: 30

# Adicionando um novo par chave-valor ao dicionário
mapeamento_idades["Eva"] = 22

# Imprimindo o dicionário atualizado
print("Dicionário de idades atualizado:", mapeamento_idades)

print("----------Exercício Y-------------")

# Definindo uma lista de palavras
lista_palavras = ["apple", "banana", "apple", "orange", "banana", "apple"]

# Inicializando um dicionário vazio para contar as ocorrências de cada palavra
contagem_palavras = {}

# Contando as ocorrências de cada palavra na lista
for palavra in lista_palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

# Imprimindo a contagem de palavras
print("Contagem de palavras:", contagem_palavras)


