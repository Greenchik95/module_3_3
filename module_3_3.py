def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params()  # Вывод значений параметров
print()

print('-------- 1. Функция с параметрами по умолчанию ---------')
print_params(2, 'столбец', False)
print_params(3, 'None')
print_params(a='один', b='два', c='три')
print_params(a='один', b='два')
print_params(b='два', c='три')
print_params(a='один', c='три')
print_params(a='один')
print_params(b='два')
print_params(c='три')
print_params()  # Вывод функции без аргументов
print()

print('--------------- 2. Распаковка параметров ---------------')
# 2. Распаковка параметров:
# Создаем список values_list с тремя элементами разных типов.
values_list = [2.1, 'main', True]
# Создаем словарь values_dict с тремя ключами, соответствующими
# параметрам функции print_params, и значениями разных типов.
values_dict = {'a': 'all', 'b': False, 'c': 5}
# Передаем values_list и values_dict в функцию print_params,
# используя распаковку параметров (* для списка и ** для словаря).
print_params(*values_list)
print_params(**values_dict)
print()

print('--------- 3. Распаковка + отдельные параметры ----------')

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)