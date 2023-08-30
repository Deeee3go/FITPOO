from heranca import Mae, Filha, Neta

print('\ncriando objeto mae....')
mae = Mae(1)

print('\ncriando objeto mae....')
filha = Filha(1, 2)

print('\ncriando objeto mae....')
neta = Neta(1, 2, 3)


print('\nVisualizando os objetos')
print('mae', vars(mae))
print('filha', vars(filha))
print('neta', vars(neta))
