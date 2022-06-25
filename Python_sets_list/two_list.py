lst1, lst2 = list(map(int, input().split())), list(map(int, input().split()))



set1, set2 = set(lst1), set(lst2)
# print(set1, set2, sep='\n')

set1 = set1 | set2
# print(set1)

print(len(set1))



