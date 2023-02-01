print('=' * 30)
print('          BANCO DEV')
print('=' * 30)
c50 = v20 = d10 = r1 = 0
valor = float(input('Que valor você quer sacar? R$'))
res = valor
while True:
    if valor >= 50:
        valor //= 50
        if valor * 50 == res:
            c50 = valor
            break
        else:
            c50 = valor
            valor *= 50
            valor = res - valor
    elif valor >= 20:
        res = valor
        valor //= 20
        if valor * 20 == res:
            v20 = valor
            break
        else:
            v20 = valor
            valor *= 20
            valor = res - valor
    elif valor >= 10:
        res = valor
        valor //= 10
        d10 = valor
        if valor * 10 == res:
            break
        else:
            valor *= 10
            valor = res - valor
    elif valor <= 9:
        res = valor
        valor /= 1
        r1 = valor
        break
print('=' * 30)
print(f'Você vai receber {c50:.0f} notas de R$50')
print(f'Você vai receber {v20:.0f} notas de R$20')
print(f'Você vai receber {d10:.0f} notas de R$10')
print(f'Você vai receber {r1:.0f} notas de R$1')

# cedulas de {R$50} {R$20} {R$10} R$1