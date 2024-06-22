immutable_var = 12, "строка"
print(immutable_var)
#immutable_var [0] = 30 кортеж не поддерживает изменение элементов
#Единственные доступные операции конкатенацию и умножение.
#immutable_var = (12, 'строка') + (35, 'банан')
#immutable_var = (12, 'строка') * 2


mutable_list = ['raccoon', 'squirrel', 'car']
mutable_list.extend([24, 35])
mutable_list [0] = 'whael'
mutable_list [1] = 'cheese'
print(mutable_list)