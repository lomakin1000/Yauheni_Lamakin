# Используйте генератор списков чтобы получить следующий: ['xy', 'xz', 'xv', 'yy', 'yz', 'yv'].


lst = [i + j for i in 'xy' for j in 'yzv']
print(lst)
