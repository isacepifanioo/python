print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
num = int(input('dgite quantos termos você que mostrar: '))
cont = 1
n1 = 0
n2 = 0
n3 = 0
while cont <= num:
    print(n3, ' 👉 ', end='')
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    cont += 1
    if n3 == 0:
        n2 = 1
print('Fim ✅')
print('-'*30)