num = int(input('digite um numero: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end='')
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')