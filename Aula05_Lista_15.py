my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False
 
for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break
 
if found:
    print("Elemento encontrado no índice", i)
else:
    print("ausente")
    
#Nota:

#o valor de destino é armazenado na variável to_find;
#o status atual da pesquisa é armazenado na variável found (True/False)
#quando found se torna True, o loop for é encerrado.
#Vamos supor que você tenha escolhido os seguintes números na loteria: 3, 7, 11, 42, 34, 49.

#Os números que foram desenhados são: 5, 11, 9, 42, 3, 49.#