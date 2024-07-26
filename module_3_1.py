calls = 0
def count_calls ():    # функция для подсчёта вызовов остальных функций
    global calls
    calls+=1
def string_info (string):     # Создаём функцию string_info с параметром string
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains (string, list_to_search):  # проверяем находится ли строка в этом списке
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]
# Вывод результата
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic'])) # No matches
print(calls)
