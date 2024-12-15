N, M = map(int, input().split())
wantN, wantM = map(int, input().split())
num = []
for i in range(N):
    tmp = []
    for j in range(M):
        tmp.append('A')
    num.append(tmp)

k = 0
s = 0
while 1:
    if 'A' in num[k]:
        for i in range(s, M - s):
            num[k][i] = 'R'
    else: break
    if 'A' in num[s+1]:
        for i in range(s+1, N - s):
            num[i][M-1-s] = 'D'
    else: break
    if 'A' in num[N-1-s]:
        for i in range(s, M-s-1):
            num[N-1-s][i] = 'L'
    else: break
    if 'A' in num[s+1]:
        for i in range(s+1, N-1-s):
            num[i][k] = 'U'
    else: break
    k += 1
    s += 1

print(num[wantN-1][wantM-1])