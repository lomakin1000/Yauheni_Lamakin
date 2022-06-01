
# версия 1
num = int(input("Please enter an integer "))
num1 = abs(num)
dig1 = num1 // 100
dig2 = num1 // 10 % 10
dig3 = num1 % 10
sum_dig = dig1 + dig2 + dig3
# print(dig1)   для проверки каждой цифры
# print(dig2)   для проверки каждой цифры
# print(dig3)   для проверки каждой цифры
print("Sum of the digits =", sum_dig)


# версия 2
# num = int(input("Please enter an integer "))
# num1 = abs(num)
# print("Sum of the digits =", (num1 // 100) + (num1 // 10 % 10) + (num1 % 10))


