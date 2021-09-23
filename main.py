# # todo Создать переменную типа String
# name = 'Nataliia.'
# word = 'My name is '
# print(word + name, type(name))
#
# # todo Создать переменную типа Integer
# age = 28
# print('I am', age, 'years old.', type(age))
#
# # todo Создать переменную типа Float
# weight = 57.7
# print('My weight', weight, 'kg.', type(weight))
#
# # todo Создать переменную типа Bytes
# message = 'I like sweet'
# byte_message = bytes(message, 'utf-8')
# print(byte_message)
#
# # todo Создать переменную типа List
# my_list = ['biscuits', 'candy', 'cake']  # Python Lists
# print(my_list, type(my_list))
#
# my_list_1 = ['biscuits', 'candy', 'cake']        # Access List Items-получение доступа указав номер индекса
# print(my_list_1[1])
#
# my_list_2 = ['biscuits', 'candy', 'cake']        # Change List Items - изменить значение определённого элемента
# my_list_2[2] = "pancake"
# print(my_list_2)
#
# my_list_3 = ['biscuits', 'candy', 'cake']        # Add List Items - добавить значение в список
# my_list_3.append('pancake')
# print(my_list_3)
#
# # todo Создать переменную типа Tuple
# my_tuple = ('biscuits', 'candy', 'cake')
# print(my_tuple)
#
# my_tuple_1 = tuple('biscuits it very yammy')  # написание каждой букві отдельно
# print(my_tuple_1)
#
# my_tuple = ('biscuits_1', 'candy_2', 'cake_3', 'biscuits_1', 'candy_2')  # вывод повторяющихся значений
# print(my_tuple)
#
# my_tuple = ('biscuits_11', 'candy_22', 'cake_33')  # вывод количества элементов в кортеже
# print(len(my_tuple))
#
# # todo Создать переменную типа Set (изменяемый тип данных)
# my_set = {'biscuits1', 'candy2', 'cake3'}  # каждый раз появляются в новом порядке
# print(my_set)
#
# my_set = ('biscuits_11', 'candy_22', 'cake_33')  # вывод количества элементов в колекции
# print(len(my_set))
#
# # todo Создать переменную типа Frozen set (не изменяемый тип данных)
# my_list_4 = ['biscuits_01', 'candy_02', 'cake_03']
# x = frozenset(my_list_4)
# print(x, type(x))
#
# # todo Создать переменную типа Dict
# dict = {
#     'biscuits' : 1 ,
#     'candy' : 2,
#     'cake' : 3
# }
# print(dict)
#
#
# dict = {                 # доступ к елементам словаря
#     'biscuits' : 1 ,
#     'candy' : 'cherry',
#     'cake' : 3
# }
# x = dict["candy"]
# print(x)
#
# #todo Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
# print(word + name, type(name))
# print('I am', age, 'years old.', type(age))
# print('My weight', weight, 'kg.', type(weight))
# print(byte_message, type(byte_message))
# print(my_list, type(my_list))
# print(my_tuple, type(my_tuple))
# print(my_set, type(my_set))
# print(x, type(x))
# print(dict, type(dict))

# #todo Создать 2 переменные String, создать переменную в которой суммируете эти переменные. Вывести в консоль.
# word1 = 'Доброе '
# word2 = 'утро! '
# word3 = word1 +word2
# print(word3, type(word3))

#todo Создать 2 переменные Integer, создать переменную в которой суммируете эти переменные. Вывести в консоль.
int1 = 22
int2 = 7
int3 = int1 + int2
print(int3, type(int3))

#todo Создать переменную в которой Разделите эти переменные Int. Вывести в консоль.
int6 = int1 / int2
print(int6, type(int6))

#todo Создать переменную в которой Умножите эти переменные Int. Вывести в консоль.
int9 = int1 * int2
print(int9, type(int9))

#todo Создать переменную в которой Разделите без остатка эти переменные Int. Вывести в консоль.
int12 = int1 // int2
print(int12, type(int12))

#todo Создать переменную в которой надо присвоить остаток от деления этих переменные Int. Вывести в консоль.
int13 = int1 % int2
print(int13, type(int13))