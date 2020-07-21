# 1. Дано натуральное число. Напишите программу, которая выводит его цифры в столбик в обратном порядке.
#
# Формат входных данных
# На вход программе подается одно натуральное число.
#
# Формат выходных данных
# Программа должна вывести цифры введенного числа в столбик в обратном порядке.

num = int(input())
while num != 0:
    last_digit = num % 10
    num = num // 10
    print(last_digit)


# 2. Дано натуральное число. Напишите программу, которая меняет порядок цифр числа на обратный.
#
# Формат входных данных
# На вход программе подается одно натуральное число.
#
# Формат выходных данных
# Программа должна вывести число записанное в обратном порядке.

num = int(input())
while num != 0:
    last_digit = num % 10
    num = num // 10
    print(last_digit, end="")

# or
num = int(input())
reversed_num = ""
while num != 0:
    last_digit = num % 10
    reversed_num += str(last_digit)
    num //= 10
print(int(reversed_num))

# or
num = int(input())
reversed_num = ""
while num != 0:
    print(num % 10, end="")
    num //= 10


# 3. Дано натуральное число n (n≥10). Напишите программу, которая определяет его максимальную и минимальную цифры.
#
# Формат входных данных
# На вход программе подается одно натуральное число.
#
# Формат выходных данных
# Программа должна вывести максимальную и минимальную цифры введенного числа (с поясняющей надписью).

num = int(input())
max_digit = num % 10
min_digit = num % 10
while num > 0:
    digit = num % 10
    num //= 10
    if digit > max_digit:
        max_digit = digit
    if digit < min_digit:
        min_digit = digit
print("Максимальная цифра равна", max_digit)
print("Минимальная цифра равна", min_digit)

# or
num = int(input())
min_digit = 9
max_digit = 0
while num != 0:
    min_digit = min(min_digit, num % 10)
    max_digit = max(max_digit, num % 10)
    num //= 10
print('Максимальная цифра равна', max_digit)
print('Минимальная цифра равна', min_digit)


# 4. Дано натуральное число. Напишите программу, которая вычисляет:
#
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.
# Формат входных данных
# На вход программе подается одно натуральное число.
#
# Формат выходных данных
# Программа должна вывести значения указанных величин в указанном порядке.

num = int(input())
duplicate_num = num
sum_of_digit = 0
multiplication_digit = 1
counter_digit = 0
arithmetic_mean = 0
while duplicate_num != 0:
    last_digit = duplicate_num % 10
    sum_of_digit = sum_of_digit + last_digit
    multiplication_digit = multiplication_digit * last_digit
    counter_digit = counter_digit + 1
    arithmetic_mean = sum_of_digit / counter_digit
    duplicate_num = duplicate_num // 10
print(sum_of_digit)
print(counter_digit)
print(multiplication_digit)
print(arithmetic_mean)
print(num // 10**(counter_digit - 1))
print(num // 10**(counter_digit - 1) + num % 10)


# 5. Дано натуральное число n (n>9). Напишите программу, которая определяет его вторую (с начала) цифру.
#
# Формат входных данных
# На вход программе подается одно натуральное число, состоящее как минимум из двух цифр.
#
# Формат выходных данных
# Программа должна вывести его вторую (с начала) цифру.

num = int(input())
second_digit = 0
while num > 9:
    second_digit = num % 10
    num = num // 10
print(second_digit)


# 6. Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
#
# Формат входных данных
# На вход программе подается одно натуральное число.
#
# Формат выходных данных
# Программа должна вывести «YES» если число состоит из одинаковых цифр и «NO» в противном случае.

num = int(input())
is_same_digits = True
last_digit = num % 10
while num != 0:
    if num % 10 != last_digit:
        is_same_digits = False
        break
    num = num // 10
print("YES" if is_same_digits else "NO")

# or
num = int(input())
last_digit = num % 10
counter = 0
while num != 0:
    digit = num % 10
    if last_digit != digit:
        counter = counter + 1
    num = num // 10
print("YES" if counter == 0 else "NO")


# 7. Дано натуральное число.
# Напишите программу, которая определяет, является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.
#
# Формат входных данных
# На вход программе подается одно натуральное число.
#
# Формат выходных данных
# Программа должна вывести «YES» если последовательность его цифр при просмотре справа налево является упорядоченной по неубыванию и «NO» в противном случае.

num = int(input())
is_ordered = True
while num > 9:
    second_digit_on_right = num // 10 % 10
    first_digit_on_right = num % 10
    if first_digit_on_right > second_digit_on_right:
        is_ordered = False
        break
    num = num // 10
print("YES" if is_ordered else "NO")