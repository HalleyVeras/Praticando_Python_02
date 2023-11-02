#Será uma sequência de números inteiros consecutivos de 1 
#(você adiciona um a todos os valores acrescentados) a 5.
my_list = [] # Criando uma lista vazia.

for i in range(5):
    my_list.append (i + 1)

print (my_list)
################################################################

#você deve obter a mesma sequência, mas em ordem inversa (este é o mérito de usar o método insert()).
my_list = []  # Criando uma lista vazia.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)
