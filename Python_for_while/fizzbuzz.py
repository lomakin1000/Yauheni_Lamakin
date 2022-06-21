
for i in range(1,101):
    a = ''
    if (i % 3 == 0):
        a += 'Fizz'
    if (i % 5 == 0):
        a += 'Buzz'
    if not a:
        a += str(i)
    print(a)