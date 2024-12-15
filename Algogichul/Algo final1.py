import math

x = list(map(int, input().split()))
y = list(map(int, input().split()))

spot = []
for i in range(len(x)):
    spot.append([])


for i in range(len(x)):
    spot[i].append(x[i])
    spot[i].append(y[i])

def slope(A, B):
    if(A[0] == B[0]):
        return float('inf')
    else:
        return (B[1] - A[1] / B[0] - A[0])
    
def dist(A, B):
    return((B[0] - A[0]) ** 2 +(B[1] - A[1]) ** 2) ** 0.5

i = spot.index(min(spot))
spot[0], spot[i] = spot[i] , spot[0]

for j in range(0, len(spot)):
    for i in range(1, len(spot) - 1):
        if slope(spot[0], spot[i]) > slope(spot[0], spot[i+1]):
            spot[i], spot[i+1] = spot[i+1], spot[i]
        elif slope(spot[0], spot[i]) == slope(spot[0], spot[i+1]):
            if (dist(spot[0], spot[i])) > (dist(spot[0], spot[i+1])):
                spot[i], spot[i+1] = spot[i+1], spot[i] 

mass = 0


for i in range(len(spot) - 2):
    a = dist(spot[0], spot[1])
    b = dist(spot[1], spot[2])
    c = dist(spot[2], spot[0])

    s = (a+b+c) / 2
    S = math.sqrt(s*(s-a)*(s-b)*(s-c))

    mass += S

    del spot[1]

mass = round(mass)

print(mass)

