# Manipulação de Strings em Python:
# Exemplos de utilização das aspas:

minhaString = 'Olá'
print(minhaString)

minhaString = "Olá"
print(minhaString)

minhaString = '''Olá'''
print(minhaString)

# 3 aspas duplas para suportar textos com múltiplas linhas

print("----------Exercício 1-------------")

minhaString = """Olá, bem-vindo
            ao mundo do Python"""
print(minhaString)

# É possível acessar CARACTERES específicos em uma String:

print("----------Exercício 2-------------")

minhaString = "São Paulo"
print(minhaString[1])

# Concatenando em Python:

print("----------Exercício 3-------------")

minhaString = "São Paulo" + " é um estado" + " do Brasil"
print(minhaString)

# Também é possível identificar um caractere específico ou
# uma sequência de caracteres contida em uma String:

print("----------Exercício 4-------------")

minhaString = "São Paulo" + " é um estado" + " do Brasil"

if "São Paulo" in minhaString:
    print("Sequência encontrada")
else:
    print("Sequência não encontrada")
