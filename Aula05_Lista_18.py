# Uma tabela de quatro colunas/quatro linhas ‒ uma matriz bidimensional (4x4)

table = [[":(", ":)", ":(", ":)"],
            [":)", ":(", ":)", ":)"],
            [":(", ":)", ":)", ":("],
            [":)", ":)", ":)", ":("]]

print(table)
print(table[0][0])  # outputs: ':('
print(table[0][3])  # outputs: ':)'


# Cubo - uma matriz tridimensional (3x3x3)

cube = [[[':(', 'x', 'x'],
            [':)', 'x', 'x'],
            [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
        [':(', 'x', 'x'],
        [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
        [':)', 'x', 'x'],
        [':)', 'x', 'x']]]

print(cube)
print(cube[0][0][0])  # outputs: ':('
print(cube[2][2][0])  # outputs: ':)'