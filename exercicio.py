# funções 

def palindromo(texto):
    for i in range(len(texto)):
        if texto[i] != texto [-1-i]:
            return False
    return True

# main cod


entradas = ['arara', 'elefante', 'radar', 'banana']
palindromos = []

for palavra in entradas:
    if (palindromo(palavra)):
        palindromos.append(palavra)


print(palindromos)
