
# Одной строкой (и одним выражением) удалите элемент '2x' из прошлого списка и напечатайте его.

lst1 = [str(i) + 'x' for i in range(1,5)]
print(lst1)

lst1.pop(1)
print(lst1)


