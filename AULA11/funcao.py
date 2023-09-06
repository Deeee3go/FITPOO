def converte(tipo, seq):
    convertidos = []
    if tipo == "string":
        for item in seq:
            convertidos.append(str(item))
    elif tipo == "int":
        for item in seq:
            convertidos.append(int(item))
    elif tipo == "float":
        for item in seq:
            convertidos.append(float(item))
    else:
        raise Exception('tipo não reconhecido')

    return convertidos


def converte_2(f, seq):
    convertidos = []
    for item in seq:
        convertidos.append(f(item))
    return convertidos
