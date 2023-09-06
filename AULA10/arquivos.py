texto = 'escrevendo a primeira frase'
with open('teste.txt', 'w') as f:
    f.write(texto)

s = ['linha 1', 'linha 2', 'linha 3', 'linha 4']
with open('teste.txt', 'a') as f:
    f.writelines(s)

texto2 = texto + '\n'
s2 = [f'{linha}\n' for linha in s]  # list comprehension
with open('teste2.txt', 'w') as f:
    f.write(texto2)
    f.writelines(s2)


#  texto = 'escrevendo a primeira frase'
s = ['linha 1', 'linha 2', 'linha 3', 'linha 4']
with open('print.txt', 'w') as f:
    print(texto, file=f)
    for linha in s:
        print(linha, file=f)
