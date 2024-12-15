from itertools import combinations

def LR(A,B,C):
    result1 = (A[0] * B[1]) + (B[0] * C[1]) + (C[0] * A[1])
    result2 = (A[1] * B[0]) + (B[1] * C[0]) + (C[1] * A[0])
    result = result1 - result2

    if result >= 0:
        return 'LS'
    elif result < 0:
        return 'R'
    


spot = [] # 입력한 점
total = [] # 점을 이은 도형
hubo = [] #넓이 구하는 후보


while 1: #사용자로부터 점 입력받기
    user_input = input().split()

    if "END" in user_input:
        break

    tmp = []
    for i in user_input:
        tmp.append(int(i))
    spot.append(tmp)

#도형에 들어와야할 최소 점 개수
least = len(spot) // 2
if len(spot) % 2 != 0:
    least += 1


# 점을 뭉친 조합 내에서 정렬이 필요해서 만든 함수들
def slope(A, B):
    if A[0] == B[0]:
        return float('inf')
    else:
        return (B[1] - A[1]) / B[0] - A[0]

def dist(A, B):
    return((B[0] - A[0]) ** 2 +(B[1] - A[1]) ** 2) ** 0.5



#일단 세개 점 뭉친 조합 다 찾기
for i in combinations(spot, 3): 
    i = list(i)
    total.append(i)

#3개가 한 선분에 있는 경우 배제
for i in total: 
    if i[0][0] == i[1][0] == i[2][0] or i[0][1] == i[1][1] == i[2][1]:
        
        del total[total.index(i)]

# 점 조합내의 점들 각각 정렬해주기
for space in total:
    i = space.index(min(space))
    space[0], space[i] = space[i], space[0]

    for j in range(0, len(space)):
        for i in range(1, len(space) - 1):
            if slope(space[0], space[i]) > slope(space[0], space[i+1]):
                space[i], space[i+1] = space[i+1], space[i]
            elif slope(space[0], space[i]) == slope(space[0], space[i+1]):
                if (dist(space[0], space[i]) > dist(space[0], space[i+1])):
                    space[i], space[i+1] = space[i+1], space[i]




size = 3 #처음엔 삼각형만 찾기
stack = [] 

while 1: #일정 후보 찾을 때까지 while문을 반복
    if size > least:
        break
    for space in total:
        stack = []

        fir = []
        sec = []

        for i in range(1, len(space)): #1부터 끝까지 fir에 넣기기
            fir.append(space[i])
        for i in range(2, len(space)): #2부터 끝까지 fir에 넣고 첫번째 요소 마지막에 삽입입
            sec.append(space[i])
        sec.append(space[0])


        for i in spot:
            if i in space: continue
            if LR(space[0], space[1], i) == 'LS':
                stack.append(i)

        
        for k in range(len(fir)):
            for i in stack:
                if i == 0: continue
                if LR(fir[k], sec[k], i) != 'LS':
                    stack[stack.index(i)] = 0
        
        
        real_stack = []
        for i in stack:
            if i != 0:
                real_stack.append(i)
        
        
        if len(real_stack) >= (least - size):
            hubo.append(space)

    #후보에 하나라도 있으면 cut
    if len(hubo) != 0:
        break
    else:
        size += 1
        new_total = []
        for i in combinations(total, 2):
            cnt = 0
            tmp = []
            for j in i[0]:
                if j in i[1]:
                    cnt += 1
                    tmp.append(j)
            if cnt == size-2:
                for j in i[0]:
                    if j not in tmp:
                        tmp.append(j)
                for j in i[1]:
                    if j not in tmp:
                        tmp.append(j)
                new_total.append(tmp)

        
        
        total = new_total
        
    
        
        for desk in total:
            i = desk.index(min(desk))
            desk[0], desk[i] = desk[i], desk[0]

            for j in range(0, len(desk)):
                for i in range(1, len(desk) - 1):
                    if slope(desk[0], desk[i]) > slope(desk[0], desk[i+1]):
                        desk[i], desk[i+1] = desk[i+1], desk[i]
                    elif slope(desk[0], desk[i]) == slope(desk[0], desk[i+1]):
                        if (dist(desk[0], desk[i]) > dist(desk[0], desk[i+1])):
                            desk[i], desk[i+1] = desk[i+1], desk[i]



def shoelace_formula(points):
   
    n = len(points)

    points.append(points[0])
    
    sum1 = sum(points[i][0] * points[i + 1][1] for i in range(n))
    sum2 = sum(points[i][1] * points[i + 1][0] for i in range(n))

    area = abs(sum1 - sum2) / 2

    return area

mess = []   
for i in hubo:
    tmp = shoelace_formula(i)
    mess.append(tmp)

print(round(min(mess),2))






    

    