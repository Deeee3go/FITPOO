from paciente import Paciente, NameIsEmptyError


try:
    nome = input('Digite o nome do paciente: ')
    p = Paciente(nome)
except TypeError:
    print('O nome deve ser uma string')
except NameIsEmptyError:
    print('O nome não pode ser uma string vazia')
except Exception as e:
    print('Ocorreu um erro inesperado ao criar o objeto')
    print('informações do erro:', e)
else:
    print('se está aqui, deu tudo certo acima')
finally:
    print('sempre será executado')
