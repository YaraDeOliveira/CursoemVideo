# import random
# aluno1 = input('Digite o nome do aluno 1: ')
# aluno2 = input('Digite o nome do aluno 2: ')
# aluno3 = input('Digite o nome do aluno 3: ')
# aluno4 = input('Digite o nome do aluno 4: ')
# print(random.sample([aluno1, aluno2, aluno3, aluno4], k=4))

import random


sala = 'Fabio Yara Adriana Milton'.split()
random.shuffle(sala)
print(sala)

