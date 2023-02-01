import random
v = 0
while True:
    print('-' * 50)
    n1 = int(input('Digite um numero de [0 a 10]: '))
    ioup1 = str(input('Você Escolhe Par ou Impar [P/I]: ')).upper()
    n2 = random.randint(0, 10)
    soma = n1 + n2
    print('-' * 50)
    if ioup1 == 'I':
        ioup2 = 'P'
        pc = 'Par'
        eu = 'Impar'
    else:
        ioup2 = 'I'
        pc = 'Impar'
        eu = 'Par'
    print(f'Você jogou {eu} com {n1} Numeros e Eu joguei {pc} com {n2} numeros')
    if ioup1 == 'P' and soma % 2 == 0 or ioup1 == 'I' and soma % 2 == 1:
        print('Você venceu!')
        v += 1
    else:
        print('Você perdeu!')
        break
print(f'Game Over! Você venceu {v} vezes.')
print('-' * 50)