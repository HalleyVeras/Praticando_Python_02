#Era uma vez um chapéu. O chapéu não continha coelhos, mas uma lista de cinco números: 1, 2, 3, 4 e 5.

#Sua tarefa:

#escreva uma linha de código que solicite que o usuário substitua o número do meio na lista por um número
# inteiro inserido pelo usuário (Etapa 1)

#escreva uma linha de código que remova o último elemento da lista (Etapa 2)

#escreva uma linha de código que imprima o comprimento da lista atual (Etapa 3).

hat_list = [1, 2, 3, 4, 5]

# Etapa 1: Solicitar que o usuário substitua o número do meio na lista
novo_numero = int(input("Digite um número inteiro para substituir o número do meio: "))
hat_list[2] = novo_numero

# Etapa 2: Remover o último elemento da lista
hat_list.pop()

# Etapa 3: Imprimir o comprimento da lista atual
comprimento = len(hat_list)
print("Lista atual:", hat_list)
print(f"Comprimento da lista atual: {comprimento}")