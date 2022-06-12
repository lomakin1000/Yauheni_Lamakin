arr = list(map(int, input().split()))

# l_border = int(input('enter left border '))
# r_border = int(input('enter right border '))

l_border, r_border = tuple(map(int, input().split()))

print(arr[l_border:r_border])