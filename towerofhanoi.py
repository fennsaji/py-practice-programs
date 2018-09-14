import math
t = int(input())


for i in range(t):
    preh = math.inf
    prer = math.inf
    height = 0
    n = int(input())
    for j in range(n):
        r, h = list(map(int, input().split()))
        if r<prer and h<preh:
            print(r,prer)
            print(h,preh)
            prer = r
            preh = h
            height+=h
    print(height)
    
