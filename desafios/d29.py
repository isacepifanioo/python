import random
n1 = int(input('Escolha um numero de 1 a 9:'))
sor = random.randint(1, 9)
print('Você escolheu {}\nPc escolheu {}'.format(n1, sor))
if n1 == sor:
    print('Você ganhou!')
else:
    print('Você perdeu!')