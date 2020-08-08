# 1. На вход программе подается одно число n.
# Напишите программу, которая выводит список [1, 2, 3, ..., n].

# Формат входных данных
# На вход программе подается одно натуральное число.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

n = int(input())
print(list(range(1, n + 1)))

# or
print(list(range(1, int(input()) + 1)))


# 2. На вход программе подается одно число n.
# Напишите программу, которая выводит список, состоящий из n букв английского алфавита ['a', 'b', 'c', ...] в нижнем регистре.

# Формат входных данных
# На вход программе подается натуральное число n, n≤26.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

print(list(chr(code) for code in range(97, 97 + int(input()))))
