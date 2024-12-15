from itertools import combinations

chung = input().split()
not_chung = input().split()
K = int(input())

total = []
for i in chung:
    total.append(i)
for i in not_chung:
    total.append(i)

chung_set = set()
for i in chung:
    chung_set.add(i)

notchung_set = set()
for i in not_chung:
    notchung_set.add(i)

finalround = []

for i in combinations(total, K):
    tmp = set(i)
    if len(chung_set.intersection(tmp)) >= 1 and len(notchung_set.intersection(tmp)) >= 2:
        finalround.append(list(i))

for i in finalround:
    i.sort()
finalround = sorted(finalround)


for i in finalround:
    for j in i:
        print(j, end='')
    print()

 