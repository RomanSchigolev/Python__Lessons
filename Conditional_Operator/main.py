# 1. При регистрации на сайтах требуется вводить пароль дважды.
# Это сделано для безопасности, поскольку такой подход уменьшает возможность неверного ввода пароля.

# Напишите программу, которая сравнивает пароль и его подтверждение.
# Если они совпадают, то программа выводит: «Пароль принят», иначе: «Пароль не принят».

# Формат входных данных
# На вход программе подаются две строки.

# Формат выходных данных
# Программа должна вывести одну строку в соответствии с условием задачи.

str1, str2 = [input() for _ in range(2)]

if str1 == str2:
    print("Пароль принят")
else:
    print("Пароль не принят")


# 2. Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение:
# сумма первой и последней цифр равна разности второй и третьей цифр.

# Формат входных данных
# На вход программе подаётся одно целое положительное четырёхзначное число.

# Формат выходных данных
# Программа должна вывести «ДА», если соотношение выполняется, и «НЕТ» — если не выполняется.

number = int(input())

units = number % 10
tens = number // 10 % 10
hundreds = number // 100 % 10
thousands = number // 1000

if thousands + units == hundreds - tens:
    print("ДА")
else:
    print("НЕТ")


# 3. Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке)
# последовательными членами арифметической прогрессии.

# Формат входных данных
# На вход программе подаются три числа, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести «YES» или «NO» (без кавычек) в соответствии с условием задачи.

a1, a2, a3 = [int(input()) for _ in range(3)]

if a2 - a1 == a3 - a2:
    print("Yes")
else:
    print("No")


# 3. Напишите программу, которая определяет наименьшее из двух чисел.
#
# Формат входных данных
# На вход программе подаётся два различных целых числа.
#
# Формат выходных данных
# Программа должна вывести наименьшее из двух чисел.

num1, num2 = [int(input()) for _ in range(2)]
print(num1 if num1 < num2 else num2)

# or

if num1 < num2:
    print(num1)
else:
    print(num2)


# 4. Напишите программу, которая определяет наименьшее из четырёх чисел.
#
# Формат входных данных
# На вход программе подаётся четыре целых числа.
#
# Формат выходных данных
# Программа должна вывести наименьшее из четырёх чисел.

a, b, c, d = [int(input()) for _ in range(4)]
ab = a if a < b else b
cd = c if c < d else d
print(ab if ab < cd else cd)

# or
print(min(a, b, c, d))


# 5. Напишите программу, которая по введённому возрасту пользователя сообщает, к какой возрастной группе он относится:

# до 13 включительно – детство;
# от 14 до 24 – молодость;
# от 25 до 59 – зрелость;
# от 60 – старость.

# Формат входных данных
# На вход программе подаётся одно целое число – возраст пользователя.

# Формат выходных данных
# Программа должна вывести название возрастной группы.

age = int(input())

if age <= 13:
    print("детство")
elif age < 24:
    print("молодость")
elif age < 59:
    print("зрелость")
else:
    print("старость")


# 6. Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.

# Формат входных данных
# На вход программе подаются три целых числа.

# Формат выходных данных
# Программа должна вывести одно число – сумму положительных чисел.

# Примечание. Если положительных чисел нет, то следует вывести 0.

num1, num2, num3 = [int(input()) for _ in range(3)]
total = 0

if num1 >= 0:
    total = total + num1
if num2 >= 0:
    total = total + num2
if num3 >= 0:
    total = total + num3

print(total)


# 7. Напишите программу, которая определяет, является ли заданное натуральное число трёхзначным.

num = int(input())

if 100 <= num <= 999:  # num >= 100 and num <= 999
    print("трехзначное")
else:
    print("не трехзначное")


# 8. Напишите программу, которая проверяет, что все три цифры натурального трёхзначного числа различны.

num = int(input())

units = num % 10
tens = num // 10 % 10
hundreds = num // 100

if units != tens and units != hundreds and tens != hundreds:
    print("различны")
else:
    print("не различны")


# 9. Напишите программу, которая по координатам точки, не лежащей на осях координат,
# определяет номер координатной четверти, в которой она находится.

x, y = [int(input()) for _ in range(2)]

if x > 0 < y:
    print("first")
elif x < 0 < y:
    print("second")
elif x < 0 > y:
    print("third")
else:
    print("fourth")


# 10. Напишите программу, которая принимает целое число x и определяет, принадлежит ли данное число промежутку(-1;17).

# Формат входных данных
# На вход программе подаётся целое число x.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

x = int(input())
print("Принадлежит" if -1 < x < 17 else "Не принадлежит")


# 11. Напишите программу, которая принимает целое число x и определяет,
# принадлежит ли данное число промежуткам [-infinity; -3] or [7; +infinity].

# Формат входных данных
# На вход программе подаётся целое число x.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

x = int(input())
print("Принадлежит" if x <= -3 or x >= 7 else "Не принадлежит")


# 12. Напишите программу, которая принимает целое число x и определяет,
# принадлежит ли данное число промежуткам (-30;-2] or (7;25].

# Формат входных данных
# На вход программе подаётся целое число x.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи

x = int(input())

if -30 < x <= -2 or 7 < x <= 25:
    print("Принадлежит")
else:
    print("Не принадлежит")


# 13. Назовем число красивым, если оно является четырехзначным и делится нацело на 7 или на 17.
# Напишите программу, определяющую, является ли введённое число красивым.
# Программа должна вывести «YES», если число является красивым, или «NO» в противном случае.

# Формат входных данных
# На вход программе подаётся натуральное число.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

x = int(input())

if 1000 <= x <= 9999 and (x % 7 == 0 or x % 17 == 0):
    print("YES")
else:
    print("NO")


# 14. Напишите программу, которая принимает три положительных числа и определяет, существует ли невырожденный треугольник с такими сторонами.
#
# Формат входных данных
# На вход программе подаётся три положительных целых числа.
#
# Формат выходных данных
# Программа должна вывести «YES» или «NO» в соответствии с условием задачи.

a, b, c = [int(input()) for _ in range(3)]
print("YES" if (a + b > c) and (a + c > b) and (b + c > a) else "NO")


# 15. Напишите программу, которая определяет, является ли год с данным номером високосным.
# Если год является високосным, то выведите «YES», иначе выведите «NO».

# Год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400.

# Формат входных данных
# На вход программе подаётся натуральное число.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

x = int(input())

if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
    print("YES")
else:
    print("NO")


# 16. Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли ладья попасть с первой клетки на вторую одним ходом.
# Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
# Программа должна вывести YES, если из первой клетки ходом ладьи можно попасть во вторую, или NO в противном случае.

# Формат входных данных
# На вход программе подаётся четыре числа от 1 до 8.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# Примечание. Шахматная ладья ходит по горизонтали или вертикали.

row1, col1, row2, col2 = [int(input()) for _ in range(4)]

if 0 < row1 <= 8 and 0 < col1 <= 8:
    if 0 < row2 <= 8 and 0 < col2 <= 8:
        if row1 == row2 or col1 == col2:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")


# 17. Даны две различные клетки шахматной доски.
# Напишите программу,  которая определяет, может ли король попасть с первой клетки на вторую одним ходом.
# Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
# Программа должна вывести YES, если из первой клетки ходом короля можно попасть во вторую, или NO в противном случае.

# Формат входных данных
# На вход программе подаётся четыре числа от 1 до 8.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# Примечание. Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку.

row1, col1, row2, col2 = [int(input()) for _ in range(4)]

if 0 < row1 <= 8 and 0 < col1 <= 8:
    if 0 < row2 <= 8 and 0 < col2 <= 8:
        if (row1 - row2 == 1) or (row2 - row1 == 1) or row1 == row2:
            if (col1 - col2 == 1) or (col2 - col1 == 1) or col1 == col2:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")

# or

if 0 < row1 <= 8 and 0 < col1 <= 8:
    if 0 < row2 <= 8 and 0 < col2 <= 8:
        if (-1 <= row1 - row2 <= 1) and (-1 <= col1 - col2 <= 1):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")

# or

if 0 < row1 <= 8 and 0 < col1 <= 8:
    if 0 < row2 <= 8 and 0 < col2 <= 8:
        if (abs(row1 - row2) <= 1) and (abs(col1 - col2) <= 1):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")
