import random
import time
numb = random.randint(1, 10)
print('''Sou seu computador... Acabei de pensar em um numero entre 0 e 10.
Sera que você consegue adivinhar qual foi? ''')
sorte = 0
quant = 0
while sorte != numb:
    sorte = int(input('Digite um numero: '))
    print('\033[0;36mProcessando...\033[m')
    time.sleep(1)
    quant += 1
    if sorte < numb:
        print('Mais... Tente mais uma vez.')
    elif sorte > numb:
        print('Menos... Tente mais uma vez')
    else:
        print('Acertou na {}º tentativas. Parabêns!'.format(quant))