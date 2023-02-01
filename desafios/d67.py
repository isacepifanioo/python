c = soma = 0
while c != 999:
    n1 = int(input('Digite um numero: '))
    if n1 == 999:
        break
    c += 1
    soma += n1
print(f'Você digitou {c} vezes. E a soma dos valores e {soma}')