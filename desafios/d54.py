nome = str(input('digite um frase: ')).upper().strip()
frase = nome.split()
fs = ''.join(frase)
for letras in range(len(fs) -1, -1, -1):
    print(fs[letras], end='')