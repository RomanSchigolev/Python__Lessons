s = 'aabbAA111ccDDaa'
print(s.isalnum())  # True
print(s.isalpha())  # False
print(s.isdigit())  # False

s = 'aabb!@#$11cc'
print(s.islower())  # True

s = 'AAb!@#$11CC'
print(s.isupper())  # False

s = '    abbc    '
print(s.isspace())  # False

age = 21
name = 'Roman'
txt = 'My name is {}, I am {}.'.format(name, age)
print(txt)

age = 21
name = 'Roman'
txt = 'My name is {0}, I am {1}.'.format(name, age)
print(txt)

first_name = 'Roman'
last_name = 'Schigolev'
age = 21
print(f'Hello, {first_name} {last_name}. You are {age}.')


# 1. Дополните приведенный код, используя форматирование строк с помощью метода format, так чтобы он вывел текст:
# «In 2010, someone paid 10k Bitcoin for two pizzas.» (без кавычек).

s = 'In {0}, someone paid {1} {2} for two pizzas.'
print(s.format(2010, "10k", "Bitcoin"))


# 2. Дополните приведенный код, используя форматирование строк с помощью f-строк, так чтобы он вывел текст:
# «In 2010, someone paid 10K Bitcoin for two pizzas.» (без кавычек).

year = 2010
amount = '10K'
currency = 'Bitcoin'
print(f'In {year}, someone paid {amount} {currency} for two pizzas.')
