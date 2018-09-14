t = int(input())

for x in range(t):
    n = int(input())
    for i in range(1, n//12):
        for j in range(1, n//10):
            sum = 12*i + 10*j
            if sum == n:
                break
    if sum == n:
        print(i+j)
        continue
    else:
        print("-1")
