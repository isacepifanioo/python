import random
import time

print('\033[36mJOKENPÔ\033[m')
eu = input('Pedra, Papel, Tesoura? ')
lista = ['pedra', 'papel', 'tesoura']
pc = random.choice(lista)
print('Processando')
time.sleep(1)
print('\033[36mVocê escolheu\033[m \033[4;36m{}\033[m.\n\033[31mEu escolhi\033[m \033[4;31m{}\033[m'.format(eu, pc))
if eu == 'pedra' and pc == 'tesoura' or eu == 'tesoura' and pc == 'papel' or eu == 'papel' and pc == 'pedra':
    print('\033[36mParabens você venceu!\033[m')
elif pc == 'pedra' and eu == 'tesoura' or pc == 'tesoura' and eu == 'papel' or pc == 'papel' and eu == 'pedra':
    print('\033[31mVocê perdeu\033[m!')
else:
    print('\033[4:29mDeu empate\033[m')