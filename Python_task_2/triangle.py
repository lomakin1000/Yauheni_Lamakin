
a, b, c = int(input("Enter the first side ")), int(input("Enter the second side ")), int(input("Enter the last side "))

halfP = (a + b + c) / 2  # полупериметр

S = (halfP * (halfP - a) * (halfP - b) * (halfP - c)) ** 0.5  # степень 0.5 вместо корня

if a <= 0 or b <= 0 or c <= 0:
    print('Wrong input data')
elif a + b > c and a + c > b and b + c > a:
    print("square =", S)
else:
    print('Wrong input')





