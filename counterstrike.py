import math

testCase = int(input())

for t in range(testCase):
    n,m,d = list(map(int, input().split()))
    sloc = []
    tar = []
    for i in range(n):
        (x,y) = list(map(int, input().split()))
        sloc.append((x,y))
    for i in range(m):
        (x,y) =  list(map(int, input().split()))
        tar.append((x,y))
    for i in range(n):
        x1, y1 = sloc[i]
        hits = 0
        for j in range(m):
            x2, y2 = tar[j]
            dis = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
            if dis <= d:
                hits+=1
        print(hits)
        if(m//2 <= hits):
            print('YES')
            break
        
            
