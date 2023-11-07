# Copiar a lista inteira.
list_1 = [1]
list_2 = list_1 [:]
list_1 [0] = 2
print (list_2)

# Copiando parte da lista.
my_list = [10, 8, 6, 4, 2]
new_list = my_list [1: 3]
print(new_list)


#A lista new_list terá elementos end - start (3 - 1 = 2) - aqueles com índices iguais a 1 e 2 (mas não 3).

#O resultado do fragmento é: [8, 6]

#Execute o código no editor para ver como o Python copia a lista completa e algum fragmento da lista. Sinta-se livre para experimentar!