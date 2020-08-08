# 1. На вход программе подается строка текста.
# Напишите программу, которая удаляет из нее все символы, кратные 3, то есть символы с индексами 0, 3, 6, ....

# Формат входных данных
# На вход программе подается строка текста.

# Формат выходных данных
# Программа должна вывести строку текста в соответствии с условием задачи.

string = "Python"
new_string = ""
for index in range(len(string)):
    if index % 3 != 0:
        new_string = new_string + string[index]
print(new_string)


# 2. На вход программе подается строка текста.
# Напишите программу, которая заменяет все вхождения цифры 1 на слово «one».

# Формат входных данных
# На вход программе подается строка текста.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

print(input().replace("1", "one"))


# 3. На вход программе подается строка текста.
# Напишите программу, которая удаляет все вхождения символа «@».

# Формат входных данных
# На вход программе подается строка текста.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

print(input().replace("@", ""))

# print(*["a", "b", 1], sep="")  символ * -  как spread/rest оператор в js


# 4. На вход программе подается строка текста.
# Напишите программу, которая выводит индекс второго вхождения буквы «f».
# Если буква «f» встречается только один раз, выведите число -1, а если не встречается ни разу, выведите число -2.

# Формат входных данных
# На вход программе подается строка текста.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

string = input()
first_f = string.find("f")

if string.count("f") == 1:
    print(-1)
elif string.count("f") > 1:
    print(string.find("f", first_f + 1))
else:
    print(-2)


# 5. На вход программе подается строка текста в которой буква «h» встречается как минимум два раза.
# Напишите программу, которая переворачивает и выводит последовательность символов, заключенную между первым и последним вхождением буквы «h».

# Формат входных данных
# На вход программе подается строка текста.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

string = input()
first_h = string.find("h")
last_h = string.rfind("h")
new_string = string.replace(string[first_h + 1:last_h], string[last_h - 1:first_h:-1])
print(new_string)

# or
string = input()
first_h = string.find('h')
last_h = string.rfind('h')
print(string[:first_h] + string[last_h:first_h:-1] + string[last_h:])

