fs = input('digite uma frase: ').upper().strip()
print('A letra A aparece {} vezes nessa frase'.format(fs.count('A')))
print('A letra a aparece na primeira vez na posição {}'.format(fs.find('A') + 1))
print('A letra a aparece pela ultima vez na posição {}'.format(fs.rfind('A')))

