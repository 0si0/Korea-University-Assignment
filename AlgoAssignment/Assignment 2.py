N = int(input())

C = [1]

for i in range(1, N+1):
    new_C = 0
    k = 0
    n = i-1
    while n >= 0:
        new_C = new_C + (C[k] * C[n])
        k = k+1
        n = n-1
    C.append(new_C)

facto = 1
for i in range(1, N+1):
    facto *= i

print(facto - C[-1])