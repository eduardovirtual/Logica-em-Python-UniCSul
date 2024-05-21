# Tratamento de Exceções em Python com Listas:
# Na lista a seguir é feito uma tentativa de remoção de
# "maria", porém, como não existe na lista, ele trata essa exceção...

print("----------Exercício 1-------------")

minhaLista3 = ["João","Maria","Anna","Silva"]
try:
    minhaLista3.remove("maria")
    print(minhaLista3)
except:
    print("O valor não existe na lista")

print("----------Exercício 2-------------")

try:
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))

    resultado = a / b
    print("Resultado da divisão:", resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except ValueError:
    print("Erro: Digite apenas números válidos para a e b.")
