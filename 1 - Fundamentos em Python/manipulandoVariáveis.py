nome = "Eduardo dos Santos"
idade = 21
email = "eduardo.scosta@gmail.com"
print ("nome: " + nome, " idade ", idade)

sobrenome,anoNasc,endereco = "Costa",2002,"Rua: Fulano de tal, n°45"
print ("Sobrenome: " + sobrenome, ", ano de nascimento: ", anoNasc,
       ", endereco: ", endereco)

print ("---------------------------------------------------------------")

a = 5
b = 6
c = a

print (a)
print (c)

print ("---------------------------------------------------------------")

a = 5
b = 6
c = a
a = 1
print (a, "Python lê linha por linha, por isso o valor de (A) se tornou 1")
print (c, "E como ele lê por linhas, o valor de (C) permanece 5")

print ("---------------------------------------------------------------")

a = 5
b = 6
c = a
print ("variável a antes de ter um novo valor atribuido ", a)
a = "(Isso é um texto)"
print ("valor atribuido para a variável c ", c)
print ("variável a DEPOIS de ter um novo valor atribuido: ", a)


