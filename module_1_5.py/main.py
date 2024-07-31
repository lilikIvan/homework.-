immutable_var = ([1, 2, 3], 1, 2, 3, False, 'Work')
print (immutable_var)
#immutable_var.remove = False
#Если попробовать убрать элемент 'False', то при выведение команды, программа начинает ругаться, т.к если написать print(type(immutable_var)), то мы увидим, что тип данных у нас tuple, то есть кортеж, а кортеж у нас неизменяемый.
#Поэтому изменить мы здесь только, то что мы добавили в кортеж - список.
immutable_var [0][2] = 23
print (immutable_var)

mutable_list = [2, 3, 'coffee', 'tea']
print(mutable_list)
mutable_list [0] = 31
mutable_list [1] = 13
mutable_list [2] = 'tea'
mutable_list [3] = 'coffee'
print(mutable_list)
mutable_list.remove('coffee')
mutable_list.append('scissors')
print(mutable_list)
