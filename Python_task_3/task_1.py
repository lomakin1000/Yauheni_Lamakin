

line_1 = input('please enter the line ')

counter_lower = 0
counter_upper = 0


for i in line_1:
    if 97 <= ord(i) <= 122:
        counter_lower += 1

    elif 65 <= ord(i) <= 90:
        counter_upper += 1
print(" upper case letters =", counter_upper)

print(" lower case letters =", counter_lower)