# UNIDAD 03.D20

# Tuplas

print('\n\n---[Diapo 20]---------------------')

frutas = ('manzana', 'mandarina', 'naranja')

print('Las mandarina están en la posición:', frutas.index('mandarina'))

# print('Las peras están en la posición:', frutas.index('peras'))      # Error!!


frutas = ('manzana', 'mandarina', 'naranja', 'mandarina')

print('Las mandarinas están', frutas.count('mandarina'), 'veces')
print('Las mandarinas están', frutas.count('peras'), 'veces')
