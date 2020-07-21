1.
num = int(input())
while num != 0:
    last_digit = num % 10
    num = num // 10
    print(last_digit)


2.
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


3.
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


4.
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


5.
num = int(input())
second_digit = 0
while num > 9:
    second_digit = num % 10
    num = num // 10
print(second_digit)


6.
num = int(input())
is_same_digits = True
last_digit = num % 10
while num != 0:
    if num % 10 != last_digit:
        is_same_digits = False
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


7.
num = int(input())
is_ordered = True
while num > 9:
    second_digit_right = num // 10 % 10
    first_digit_on_right = num % 10
    if first_digit_on_right > second_digit_right:
        is_ordered = False
    num = num // 10
print("YES" if is_ordered else "NO")