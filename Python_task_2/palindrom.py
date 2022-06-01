



num = int(input("Please enter a four digit number "))

dig1 = num // 1000
dig2 = num // 100 % 10
dig3 = num // 10 % 10
dig4 = num % 10
# print(a)  для проверки
# print(b)  для проверки
# print(c)  для проверки
# print(d)  для проверки

if dig1 == dig4 and dig2 == dig3:
    print("YES")
else:
    print("NO")


