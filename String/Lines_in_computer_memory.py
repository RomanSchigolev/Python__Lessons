# Функция ord позволяет определить код некоторого символа в таблице символов Unicode.
# Аргументом данной функции является одиночный символ.

num1 = ord('A')
num2 = ord('B')
num3 = ord('a')
print(num1, num2, num3)  # 65 66 97

num = ord('Abc')
print(num)  # TypeError: ord() expected a character, but string of length 3 found


# Функция chr позволяет определить по коду символа сам символ.
# Аргументом данной функции является численный код.

chr1 = chr(65)
chr2 = chr(75)
chr3 = chr(110)
print(chr1, chr2, chr3)  # A K n


# вывода всех заглавных букв английского алфавита
for i in range(26):
    print(chr(ord('A') + i))


# 1. На вход программе подаются два числа a и b.
# Напишите программу, которая для каждого кодового значения в диапазоне от a до b (включительно),
# выводит соответствующий ему символ из таблицы символов Unicode.

# Формат входных данных
# На вход программе подается два натуральных числа, каждое на отдельное строке.

# Формат выходных данных
# Программа должна вывести текст в соотвествии с условием задачи

a, b = [int(input()) for _ in range(2)]
for code in range(a, b + 1):
    print(chr(code), end=" ")


# 2. На вход программе подается строка текста.
# Напишите программу, которая переводит каждый ее символ в соответствующий ему код из таблицы символов Unicode.

# Формат входных данных
# На вход программе подается строка текста.

# Формат выходных данных
# Программа должна вывести кодовые значения символов строки разделенных одним символом пробела.

string = input()
for symbol in string:
    print(ord(symbol), end=" ")

# or
[print(ord(symbol), end=" ") for symbol in input()]


# 3.Легион Цезаря, созданный в 23 веке на основе Римской Империи не изменяет древним традициям и использует шифр Цезаря.
# Это их и подвело, ведь данный шифр очень простой.
# Однако в постапокалипсисе люди плохо знают все тонкости довоенного мира,
# поэтому ученые из НКР не могут понять как именно нужно декодировать данные сообщения.
# Напишите программу для декодирования этого шифра.

# Формат входных данных
# В первой строке дается число n(1≤ n ≤ 25) – сдвиг,
# во второй строке даётся закодированное сообщение в виде строки со строчными латинскими буквами.

# Формат выходных данных
# Программа должна вывести одну строку – декодированное сообщение.
# Обратите внимание, что нужно декодировать сообщение, а не закодировать.

shift_to_left = int(input())
coded_message = input()
decoded_message = ""
lower_alpha_list = [chr(code) for code in range(97, 123)]

for symbol in coded_message:
    decoded_message = decoded_message + lower_alpha_list[lower_alpha_list.index(symbol) - shift_to_left]
print(decoded_message)

# or
shift_to_left = int(input())
coded_message = input()

for symbol in coded_message:
    new_code = ord(symbol) - shift_to_left
    if new_code < 97:
        new_code = 122 - (96 - new_code)
    else:
        print(chr(new_code), end="")
