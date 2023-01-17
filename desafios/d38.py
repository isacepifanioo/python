num = int(input('Digite um numero: '))
print('''escolha uma opção
[1] binario
[2] octal
[3] hexadecimal''')
opc = int(input('Sua opção: '))
if opc == 1:
    print('{} convertido para binario e igual {}'.format(num, bin(num)[2:]))
elif opc == 2:
    print('{} convertido para binario e igual {}'.format(num, oct(num)[2:]))
elif opc == 3:
    print('{} convertido para binario e igual {}'.format(num, hex(num)[2:]))
else:
    print('Numero invalido')