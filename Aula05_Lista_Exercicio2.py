#Escreva um programa que reflita essas mudanças e permita praticar com o conceito de listas. Sua tarefa:

#etapa 1: criar uma lista vazia chamada beatles;
#etapa 2: use o método append() para adicionar os seguintes membros da banda à lista: John Lennon, Paul McCartney e George Harrison;
#etapa 3: Use o loop for e o método append() para solicitar que o usuário adicione os seguintes membros da banda à lista: Stu Sutcliffe e Pete Best;
#etapa 4: use a instrução del para remover Stu Sutcliffe e Pete Best da lista;
#etapa 5: Use o método insert() para adicionar Ringo Starr ao início da lista.

#A propósito, você é um fã dos Beatles? (Os Beatles são uma das bandas favoritas de Greg. Mas espere ... quem é Greg ...?)
# Etapa 1: Criar uma lista vazia chamada beatles
# Etapa 1: Criar uma lista vazia chamada beatles
beatles = []

# Etapa 2: Adicionar John Lennon, Paul McCartney e George Harrison à lista
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# Etapa 3: Usar um loop for para solicitar ao usuário adicionar Stu Sutcliffe e Pete Best à lista
for _ in range(2):
    novo_membro = input("Digite o nome de um novo membro da banda: ")
    beatles.append(novo_membro)

# Etapa 4: Usar a instrução del para remover Stu Sutcliffe e Pete Best da lista
del beatles[3:5]

# Etapa 5: Usar o método insert() para adicionar Ringo Starr ao início da lista
beatles.insert(0, "Ringo Starr")

# Imprimir a lista completa dos membros dos Beatles
print("Lista de membros dos Beatles:")
for membro in beatles:
    print(membro)

# Sim, muitas pessoas são fãs dos Beatles, eles são uma banda icônica!

