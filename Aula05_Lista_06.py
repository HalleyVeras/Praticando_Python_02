#Veja o código no editor. Veja como usamos os métodos append() e insert(). 
#Preste atenção no que acontece depois de usar insert(): 
#o primeiro primeiro elemento agora é o segundo, o segundo o terceiro e assim por diante.

numbers = [111, 7, 2, 1]

print(len(numbers))

print(numbers)


###


numbers.append (4)


print(len(numbers))

print(numbers)

###

numbers.insert (0, 222)

print(len (numbers))
print(numbers)

#numbers.insert(1, 333)
#
