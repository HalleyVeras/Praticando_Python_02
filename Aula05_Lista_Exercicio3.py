#Pergunta 1: Qual é a saída do trecho de código?
lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)

print(lst)
#Resposta [6, 2, 3, 4, 5, 1]

#Pergunta 2: Qual é a saída do trecho de código?
lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in lst:
    add += number
    lst_2.append(add)

print(lst_2)
#Resposta [1, 3, 6, 10, 15]

#Pergunta 3: Qual é a saída do trecho de código?
lst = []
del lst
print(lst)
#Resposta NameError: name 'lst' is not defined

#Pergunta 4: Qual é a saída do trecho de código?
lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))
#Resposta [2, 3]
3