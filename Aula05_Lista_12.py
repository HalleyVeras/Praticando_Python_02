#A ordenação por bolhas - versão interativa

#No editor, você pode ver um programa completo, enriquecido por uma conversa com o usuário, 
#e permitindo que ele insira e imprima elementos da lista: A classificação de bolha - 
#versão interativa final.

my_list = []
swapped = True
num = int(input("Quantos elementos você deseja embaralhar? "))

for i in range(num):
    val = float(input("Entre com a lista de elementos:"))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)

#Como você pode ver, todas as listas têm um método chamado sort(), que as classifica 
# o mais rápido possível. Você já aprendeu sobre alguns dos métodos de lista antes e 
# em breve aprenderá mais sobre outros.
