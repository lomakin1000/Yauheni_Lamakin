

n = int(input('Please enter a number'))
m = n
digits = 0
count_equals = 0
while n > 0:
    digits += 1
    n //= 10
number_of_digits = digits
while digits > 1:
    last_digit = m % 10
    first_digit = m // 10 ** (digits - 1)
    if last_digit == first_digit:
        count_equals += 1
    m = (m - first_digit * (10 ** (digits - 1))) // 10
    digits -= 2
if count_equals == number_of_digits // 2:
    print("The number is palindrom")
else:
    print("The namber is not palindrom")
