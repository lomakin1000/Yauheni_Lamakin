# список lst1

lst1 = ['1', '2', '3']
print(type(lst1))
print(lst1)

# в кортеж
tpl1 = tuple(lst1)
print(type(tpl1))
print(tpl1)

# и обратно в список
lst2 = list(tpl1)
print(type(lst2))
print(lst2)
