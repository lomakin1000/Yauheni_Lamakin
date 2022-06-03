line_1 = input('please enter the line ')

line2 = line_1.split("+")
part1 = line2[0]
part2 = line2[1]
if 'y' in part1:
    if 'x' in part1:
        k = part1[2:part1.find('x')]
        b = int(part2)
        print('k =', k, "b =", b)
    elif 'x' in part2:
        k = part2[0:part2.find('x')]
        b = part1[2:]
        print('k =', k, "b =", b)
elif 'y' in part2:
    if "x" in part1:
        k = part1[0:part1.find('x')]
        b = part2[0:part2.find('=')]
        print('k =', k, "b =", b)
    elif 'x' in part2:
        k = part2[0:part2.find('x')]
        b = part1[0:]
        print('k =', k, "b =", b)