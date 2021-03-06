# 1. Дано предложение и количество раз которое его надо повторить.
# Напишите программу, которая повторяет данное предложение нужное количество раз.

# Формат входных данных
# В первой строке записано текстовое предложение, во второй — количество повторений.

# Формат выходных данных
# Программа должна вывести указанное текстовое предложение нужное количество раз.
# Каждое повторение должно начинаться с новой строки.

phrase, counter = input(), int(input())
for _ in range(counter):
    print(phrase)


# 2. Напишите программу, которая использует ровно три цикла for для печати следующей последовательности символов:
#
# AAA
# AAA
# AAA
# AAA
# AAA
# AAA
# BBBB
# BBBB
# BBBB
# BBBB
# BBBB
# E
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# G
# Формат входных данных
#
# Формат выходных данных
# Программа должна вывести указанную последовательность символов.

for _ in range(6):
    print("AAA")
for _ in range(5):
    print("BBBB")
print("E")
for _ in range(9):
    print("TTTTT")
print("G")


# 3. На вход программе подается натуральное число n.

# Напишите программу, которая печатает звездный прямоугольник размерами n×19.

# Формат входных данных
# На вход программе подаётся натуральное число n∈[1;20] — высота звездного прямоугольника.

# Формат выходных данных
# Программа должна вывести звездный прямоугольник размерами n×19.

# Подсказка. Для печати звездной линии используйте умножение строки на число.

n = int(input())
for _ in range(n):
    print("*" * 19)


# 4. Напишите программу, которая считывает одну строку текста и выводит 10 строк, пронумерованных от 0 до 9, каждая с указанной строкой текста.

# Формат входных данных
# На вход программе подается одна строка текста.

# Формат выходных данных
# Программа должна вывести десять строк в соответствии с условием задачи.

string = input()
for i in range(10):
    print(f"{i} {string}")


# 5. На вход программе подается натуральное число n.
# Напишите программу, которая для каждого из чисел от 0 до n (включительно) выводит фразу: «Квадрат числа [число] равен [число]» (без кавычек).
#
# Формат входных данных
# На вход программе подается натуральное число n.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

n = int(input())
for i in range(n + 1):
    print(f"Квадрат числа {i} равен {i ** 2}")


# 6. На вход программе подается натуральное число n (n≥2) – катет прямоугольного равнобедренного треугольника.

# Напишите программу, которая выводит звездный треугольник в соответствии с примером.

# Формат входных данных
# На вход программе подается одно натуральное число n (n≥2).

# Формат выходных данных
# Программа должна вывести треугольник в соответствии с условием задачи.

n = int(input())
for i in range(n):
    print("*" * (n - 1))


# 7. На вход программе подается три натуральных числа m,p,n:

# m: стартовое количество организмов;
# p: среднесуточное увеличение в %;
# n: количество дней для размножения.

# Напишите программу, которая предсказывает размер популяции организмов.
# Программа должна выводить размер популяции в каждый день, начиная с 1 и заканчивая n-м днем.

# Формат входных данных
# На вход программе подается три натуральных числа.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

m, p, n = [int(input()) for _ in range(3)]
for day in range(n):
    daily_increase = (m * p / 100)
    print(f"{day + 1} {m}")
    m += daily_increase

