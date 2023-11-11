#TESTE DA SEÇÃO
#Pergunta 1: Qual é a saída do trecho de código?


list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[0]

print(list_3)

#Resposta ['C']

#Pergunta 2: Qual é a saída do trecho de código?
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2

print(list_3)
#Resposta ['B', 'C']

#Pergunta 3: Qual é a saída do trecho de código?
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[:]

print(list_3)
#Resposta []

#Pergunta 4: Qual é a saída do trecho de código?


list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2[0]

print(list_3)

#Resposta ['A', 'B', 'C']

#Pergunta 5: Insira in ou not in ao invés de ??? para que o código produz o resultado esperado.


my_list = [1, 2, "in", True, "ABC"]

print(1 ??? my_list)  # outputs True
print("A" ??? my_list)  # outputs True
print(3 ??? my_list)  # outputs True
print(False ??? my_list)  # outputs False 

#Resposta my_list = [1, 2, "in", True, "ABC"] print(1 in my_list) # outputs True print("A" not in my_list) # outputs True print(3 not in my_list) # outputs True print(False in my_list) # outputs False