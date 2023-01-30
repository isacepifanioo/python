soma = 0
while True:
    n = int(input('digite um numero: '))
    if n == 999:
        break
    soma += n
print(f'A soma dos valores e {soma}')