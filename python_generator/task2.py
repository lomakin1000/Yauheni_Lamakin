# Используйте на предыдущий список slice чтобы получить следующий: ['xy', 'xv', 'yz'].


lst = [i + j for i in 'xy' for j in 'yzv']
print(lst)




a = lst[0: 5: 2]
print(a)
