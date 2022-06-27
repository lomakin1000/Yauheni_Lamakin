# Скопируйте список и добавьте в него элемент 2x так чтобы в исходном списке этого элемента не было.
import copy
lst1 = [str(i) + 'x' for i in range(1,5)]
print(lst1)

lst1.pop(1)
print(lst1)



lst2 = copy.copy(lst1)
lst2.insert(1, '2x')
print('lst1 =', lst1, '\nlst2=',  lst2)


