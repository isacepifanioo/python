fech = ''
while fech != 'fecha':
    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))
    r = 0
    while r != 4:
        print('''        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior 
        [ 4 ] Novos núneros 
        [ 5 ] Sair do programa''')
        r = int(input('>>>>> Qual é a sua opção? '))
        if r == 1:
            res = n1 + n2
            print('A soma entre {} + {} é {}'.format(n1, n2, res))
            print('=-==' * 9)
        if r == 2:
            res = n1 * n2
            print('O resultado de {} x {} é {}'.format(n1, n2, res))
            print('=-==' * 9)
        if r == 3:
            maior = n1
            if n2 > maior:
                maior = n2
                print('=-==' * 9)
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
        if r == 5:
            fech = 'fecha'
            r = 4
            print('=-==' * 9)
        if r > 5:
            print('Opção invalida. Tente novamente')

