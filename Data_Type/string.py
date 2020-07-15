# 1. Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу:

# «Hello [введенное имя] [введенная фамилия]! You just delved into Python».

# Формат входных данных
# На вход программе подаётся две строки (имя и фамилия), каждая на отдельной строке.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

firstname, lastname = [input() for _ in range(2)]
print(f"Hello {firstname} {lastname}! You just delved into Python")


# 2. Напишите программу, которая считывает с клавиатуры название футбольной команды и выводит фразу:

# «Футбольная команда [введённая строка] имеет длину [длина введённой строки] символов».

# Формат входных данных
# На вход программе подаётся строка – название футбольной команды.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

team = input()
print(f"Футбольная команда {team} имеет длину {len(team)} символов")


# 3. Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.

# Формат входных данных
# На вход программе подаётся названия трех городов, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.

# Примечание. Гарантируется, что длины названий всех трех городов различны.

city1, city2, city3 = [input() for _ in range(3)]

length1 = len(city1)
length2 = len(city2)
length3 = len(city3)

most = max(length1, length2, length3)
least = min(length1, length2, length3)

if most == length1:
    longest = city1
elif most == length2:
    longest = city2
else:
    longest = city3

if least == length1:
    shortest = city1
elif least == length2:
    shortest = city2
else:
    shortest = city3

print(shortest, longest, sep="\n")

# or. чей-то код.
a = [input() for i in range(3)]  # Считываем 3 строки и добавляем их в список
a.sort(key=lambda s: len(s))  # Сортируем список по ключу len
print(a[0], a[-1], sep='\n')  # Выводим первый и последний элемент нашего списка


# 4. Вводятся 3 строки в случайном порядке.
# Напишите программу, которая выясняет можно ли из длин этих строк построить возрастающую арифметическую прогрессию.

# Формат входных данных
# На вход программе подаются три строки, каждая на отдельной строке.

# Формат выходных данных
# Программа должна вывести строку «YES», если из длин введенных слов можно построить арифметическую прогрессию, «NO» в ином случае.

a, b, c = [len(input()) for _ in range(3)]

if (2 * b - c - a) * (2 * c - b - a) * (2 * a - b - c) == 0:
    print("YES")
else:
    print("NO")


# 5. Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введенной строке есть подстрока «синий» и «NO» в противном случае.

# Формат входных данных
# На вход программе подается одна строка.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

string = input()
substring = "синий"
print("YES" if substring in string else "NO")
