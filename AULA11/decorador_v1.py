def decorador(f):
    def envelope():
        print('código executado antes de chamar f')
        f()
        print('código executado após chamar f')
    return envelope


@decorador
def ola_mundo():
    print('Olá, mundo!')
