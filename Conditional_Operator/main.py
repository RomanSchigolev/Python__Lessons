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

# or

if x > 0:
    if y > 0:
        print("first")
    else:
        print("fourth")
else:
    if y > 0:
        print("second")
    else:
        print("third")

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
        if (row1 - row2 == 1) or (row2 - row1 == 1) or row1 != row2:
            if (col1 - col2 == 1) or (col2 - col1 == 1) or col1 != col2:
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

# 18. Даны три целых числа. Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел: 3(если все совпадают), 2(если два совпадает) или 0(если все числа различны).

a, b, c = [int(input()) for _ in range(3)]

if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)

# 19. Зум бросил вызов Флэшу и предложил ему честный поединок в виде гонки вокруг магнетара.
# В случае проигрыша эта нейтронная звезда зарядится и уничтожит мир,
# поэтому Флэш решил не рисковать без причины, и узнать у своего друга Циско Рамона есть ли смысл принимать вызов.
# Циско получил данные, что скорость Зума равна n, а скорость Флэша равна k.

# Напишите программу, которая должна вывести ответ Циско на вопрос Флэша.

# Формат входных данных
# На вход программе подаётся два целых числа n и k, скорость Зума и Флэша.

# Формат выходных данных
# Если Зум быстрее Флэша нужно вывести NO, если Флэш быстрее Зума нужно вывести YES,
# если их скорости равны нужно вывести Don't know.

speed_of_zoom, speed_of_flesh = int(input()), int(input())

if speed_of_zoom > speed_of_flesh:
    print("NO")
elif speed_of_flesh > speed_of_zoom:
    print("YES")
else:
    print("Don't know")

# 20. Напишите программу, которая принимает три положительных числа и определяет вид треугольника, длины сторон которого равны введенным числам.

# Формат входных данных
# На вход программе подаются три числа – длины сторон существующего треугольника.

# Формат выходных данных
# Программа должна вывести на экран текст – вид треугольника («Равносторонний», «Равнобедренный» или «Разносторонний»).

a, b, c = [int(input()) for _ in range(3)]

if a == b == c:
    print("Равносторонний")
elif a == b or a == c or b == c:
    print("Равнобедренный")
else:
    print("Разносторонний")

# 21. Даны три различных целых числа. Напишите программу, которая находит среднее по величине число.

# Формат входных данных
# На вход программе подаётся три различных целых числа, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести среднее число.

# Примечание. Средним называется число, которое будет вторым, если три числа отсортировать в порядке возрастания.

a, b, c = [int(input()) for _ in range(3)]

if a < b < c or c < b < a:
    print(b)
elif c < a < b or b < a < c:
    print(a)
else:
    print(c)

# or

print(a + b + c - max(a, b, c) - min(a, b, c))  # только для трёх чисел

# or

print(sorted([int(input()) for _ in range(3)])[1])  # только для трёх чисел

# 22. Дан порядковый номер месяца (1, 2, ..., 12).
# Напишите программу, которая выводит на экран количество дней в этом месяце. Принять, что год является невисокосным.

# Примечание. Постарайтесь написать программу, так чтобы в ней было не более трех условий.

# Формат входных данных
# На вход программе подаётся одно целое число – порядковый номер месяца.

# Формат выходных данных
# Программа должна вывести количество дней в этом месяце.

# 1, 3, 5, 7, 8, 10, 12 - 31 день
# 4, 6, 9, 11 - 30
# 2 - 28

number_of_month = int(input())
months_in_31_days = [1, 3, 5, 7, 8, 10, 12]
months_in_30_days = [4, 6, 9, 11]

if number_of_month in months_in_31_days:
    print(31)
elif number_of_month in months_in_30_days:
    print(30)
else:
    print(28)

# 23. Известен вес боксера-любителя (целое число).
# Известно, что вес таков, что боксер может быть отнесён к одной из трех весовых категорий:

# Легкий вес – до 60 кг;
# Первый полусредний вес – до 64 кг;
# Полусредний вес – до 69 кг.
# Напишите программу, определяющую, в какой категории будет выступать данный боксер.

# Формат входных данных
# На вход программе подаётся одно целое число.

# Формат выходных данных
# Программа должна вывести текст – название весовой категории.

weight = int(input())

if weight < 60:
    print("Легкий вес")
elif weight < 64:
    print("Первый полусредний вес")
else:
    print("Полусредний вес")

# 24. Напишите программу, которая считывает с клавиатуры два целых числа и строку.
# Если эта строка является обозначением одной из четырёх математических операций (+, -, *, /),
# то выведите результат применения этой операции к введённым ранее числам, в противном случае выведите «Неверная операция».
# Если пользователь захочет поделить на ноль, выведите текст «На ноль делить нельзя!».

# Формат входных данных
# На вход программе подаются два целых числа, каждое на отдельной строке, и строка.

# Формат выходных данных
# Программа должна вывести результат применения операции к введенным числам или соответствующий текст,
# если операция неверная либо если происходит деление на ноль.

num1, num2 = [int(input()) for _ in range(2)]
operator = input()

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if num2 == 0:
        print("На ноль делить нельзя!")
    else:
        print(num1 / num2)
else:
    print("Неверная операция")

# чей-то код. нужно в нем разобраться
# num1 = int(input())
# num2 = int(input())
# op = input()
#
# operators = {
#   '+': lambda x, y: x + y,
#   '-': lambda x, y: x - y,
#   '/': lambda x, y: x / y,
#   '*': lambda x, y: x * y,
#   'mod': lambda x, y: x % y,
#   'pow': lambda x, y: x ** y,
#   'div': lambda x, y: x // y,
# }
#
# try:
#   print(operators[op](num1, num2))
# except ZeroDivisionError:
#   print('На ноль делить нельзя!')
# except KeyError:
#     print('Неверная операция')


# 25. Красный, синий и желтый называются основными цветами, потому что их нельзя получить путем смешения других цветов.
# При смешивании двух основных цветов получается вторичный цвет:

# если смешать красный и синий, то получится фиолетовый;
# если смешать красный и желтый, то получится оранжевый;
# если смешать синий и желтый, то получится зеленый.
# Напишите программу, которая считывает названия двух основных цветов для смешивания.
# Если пользователь вводит что-нибудь помимо названий «красный», «синий» или «желтый», то программа должна вывести сообщение об ошибке.
# В противном случае программа должна вывести название вторичного цвета, который получится в результате.

# Формат входных данных
# На вход программе подаются две строки, каждая на отдельной строке.

# Формат выходных данных
# Программа должна вывести полученный цвет смешения либо сообщение «ошибка цвета», если введён был не цвет.

# Примечание 1. Если смешать красный и красный, то получится красный и т.д.

color1, color2 = input(), input()
main_colors = ["красный", "синий", "желтый"]

if color1 in main_colors and color2 in main_colors:
    if color1 == "красный" and color2 == "синий" or color1 == "синий" and color2 == "красный":
        print("фиолетовый")
    elif color1 == "красный" and color2 == "желтый" or color1 == "желтый" and color2 == "красный":
        print("оранжевый")
    elif color1 == "синий" and color2 == "желтый" or color1 == "желтый" and color2 == "синий":
        print("зеленый")
    elif color1 == color2 == "красный":
        print(color1)
    elif color1 == color2 == "синий":
        print(color1)
    elif color1 == color2 == "желтый":
        print(color1)
else:
    print("ошибка цвета")

# 26. На колесе рулетки карманы пронумерованы от 0 до 36. Ниже приведены цвета карманов:

# карман 0 зеленый;
# для карманов с 1 по 10 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный;
# для карманов с 11 по 18 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный;
# для карманов с 19 по 28 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный;
# для карманов с 29 по 36 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный.
# Напишите программу, которая считывает номер кармана и показывает, является ли этот карман зеленым, красным или черным.
# Программа должна вывести сообщение об ошибке, если пользователь вводит число, которое лежит вне диапазона от 0 до 36.

# Формат входных данных
# На вход программе подаётся одно целое число.

# Формат выходных данных
# Программа должна вывести цвет кармана либо сообщение «ошибка ввода», если введённое число лежит вне диапазона от 0 до 36.

number = int(input())

if 0 <= number <= 36:
    if number == 0:
        print("зеленый")
    elif 1 <= number <= 10 or 19 <= number <= 28:
        if number % 2 == 0:
            print("черный")
        else:
            print("красный")
    elif 11 <= number <= 18 or 29 <= number <= 36:
        if number % 2 == 0:
            print("красный")
        else:
            print("черный")
else:
    print("ошибка ввода")

# or

if number == 0:
    print('зеленый')
elif number > 36 or number < 0:
    print('ошибка ввода')
elif 11 > a > 0 or 29 > number > 18:
    if number % 2 == 0:
        print('черный')
    else:
        print('красный')
else:
    if number % 2 == 0:
        print('красный')
    else:
        print('черный')

