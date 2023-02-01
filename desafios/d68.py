while True:
    print('-'*50)
    n1 = int(input('Qual valor que você que ver na tabuada: '))
    if n1 < 0:
        break
    s = 0
    while s != 10:
        res = n1 * s
        print(f'{n1} x {s} = {res}')
        s += 1
