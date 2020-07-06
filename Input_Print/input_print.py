# print(input(), "- чемпион!")

# 1. Напишите программу, которая считывает три строки по очереди,
# а затем выводит их в той же последовательности, каждую на отдельной строчке.

# Формат входных данных
# На вход программе подаются три строки, каждая на отдельной строке.

# Формат выходных данных
# Программа должна вывести введенные строки в той же последовательности, каждую на отдельной строке.

array = []
for i in range(3):
    array.append(input())

for word in array:
    print(word, sep="\n")

# or

for i in range(3):
    print(input())

# ----------------------------------

# 2. Напишите программу, которая считывает три строки по очереди,
# а затем выводит их в обратной последовательности, каждую на отдельной строчке.

# Формат входных данных
# На вход программе подается три строки, каждая на отдельной строке.

# Формат выходных данных
# Программа должна вывести введенные строки в обратной последовательности, каждую на отдельной строке.

array = []
for i in range(3):
    array.append(input())

for word in array[::-1]:
    print(word, sep="\n")

# or

array = []
for i in range(3):
    array.append(input())

for word in reversed(array):
    print(word, sep="\n")
