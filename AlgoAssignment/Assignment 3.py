from itertools import combinations

total = []
character = []
bindo = []

while 1:
    johap = input().split()
    if johap[0] == "END":
        break

    total.append(johap)

best_score = len(total) // 2
if len(total) % 2 == 1:
    best_score += 1



for i in total:
    for j in i:
        if j not in character:
            character.append(j)
            bindo.append(1)
        elif j in character:
            bindo[character.index(j)] += 1

for i in range(1, len(bindo)):
    if bindo[i-1] < bindo[i]:
        bindo[i-1], bindo[i] = bindo[i], bindo[i-1]
        character[i-1], character[i] = character[i], character[i-1]


size = 1
hubo_cha = []
hubo_bin = []

for i in range(len(bindo)):
    if bindo[i] >= best_score:
        hubo_cha.append(character[i])
        hubo_bin.append(bindo[i])

next_hubo_cha = []
next_hubo_bin = []
best = []
while 1:

    size += 1
    next_hubo_cha = []
    next_hubo_bin = []

    for i in combinations(hubo_cha, size):
        next_hubo_cha.append(i)

    score = 0
    
    if len(next_hubo_cha) == 0:
        break
   
    for i in next_hubo_cha:
        score = 0
        for j in total:
            for k in i:
                if k not in j:
                    break
            else:
                score+=1
        next_hubo_bin.append(score)
    

    for i in range(len(next_hubo_bin)):
        if next_hubo_bin[i] >= best_score:
            best.append(next_hubo_cha[i])
        else: 
            del next_hubo_bin[i]
            del next_hubo_cha[i]

    hubo_cha = next_hubo_cha
    hubo_bin = next_hubo_bin


print(len(best))