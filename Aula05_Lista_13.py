list_1 = [1]
list_2 = list_1
list_1 [0] = 2
print(list_2)
#O programa:

#cria uma lista de um elemento chamada list_1;
#atribui-o a uma nova lista chamada list_2;
#altera o único elemento de list_1;
#imprime a lista_2.

#A parte surpreendente é o fato de que o programa produzirá: [2], não [1], que parece ser a solução óbvia.

#As listas (e muitas outras entidades Python complexas) são armazenadas de maneiras diferentes das variáveis comuns (escalares).

#Você poderia dizer que:

#o nome de uma variável comum é o nome de seu conteúdo;
#o nome de uma lista é o nome de um local de memória onde a lista é armazenada.