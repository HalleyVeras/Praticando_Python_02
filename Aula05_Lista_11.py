#Resolvemos esse problema da seguinte maneira: introduzimos outra variável ; 
#sua tarefa é observar se alguma troca foi feita durante a passagem ou não; 
#se não houver troca, a lista já está classificada e nada mais precisa ser feito. 
#Criamos uma variável chamada swapped e atribuímos um valor de False a ela para indicar
#que não há swaps. Caso contrário, ele será atribuído como True.



my_list = [8, 10, 6, 2, 4]  # Lista para ordenar
swapped = True  # É um pouco falso, precisamos dele para entrar no loop while.

while swapped:
    swapped = False  # nenhuma troca até agora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # uma troca ocorreu!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)
