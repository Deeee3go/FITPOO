# sobrecarga

def sobrecarga(nome, numero=None):
    print('nome')
    if numero:
        print(numero)


print('primeira execução')
sobrecarga('Diego')

print('segunda execução')
sobrecarga('diego', 69)
