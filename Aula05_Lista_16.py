#Agora, encontre a temperatura mais alta durante todo o mês - veja o código:

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# A matriz é magicamente atualizada aqui.
#

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("A maior temperatura foi:", highest)

#Nota:

#a variável day itera por todas as linhas na matriz temps;
#a variável temp itera todas as medidas feitas em um dia.