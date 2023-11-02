my_list = [8, 10, 6, 2, 4]  # Lista para ordenar

for i in range(len(my_list) - 1):  # precisamos de (5 - 1) comparações
    if my_list[i] > my_list[i + 1]:  # comparar elementos adjacentes
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # Se acabarmos aqui, nós temos que trocar os elementos.
