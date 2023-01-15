tex = input('escreva algo: ')
print('Qual e a clase do {}'.format(tex), type(tex))
print('A palavra so tem espaço? ', tex.isspace())
print('A palavra que você digitou so tem numeros? ', tex.isnumeric())
print('A palavra que você digitou so tem letras? ', tex.isalpha())
print('A palavra que você digitou tem numeros e letras? ', tex.isalnum())
print('A palavra esta em maiusculas? ', tex.isupper())
print('A palavra esta em minusculas? ', tex.islower())
print('A palavra esta capitalizada? ', tex.istitle())


