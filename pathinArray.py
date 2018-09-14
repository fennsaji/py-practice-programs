def checkAdjacentOne(arr, i, j, n):
    if arr[i][j]
    
    
def checkAdjacentTwo(arr, i , j, n):
    


N = int(input())
arr=[]
oneCon = False
twoCon = False

for i in range(N):
    subArr = list(map(int, input().split()))
    arr.append(subArr)

for i in range(N):
    for j in range(N):
        if arr[0][j] == 1:
            x = 0 
            y = j
            while True:
                x,y = checkAdjacentOne(arr, x, y, n)
                if not ind:
                    break
                if y == N-1:
                    oneCon = True
        if arr[i][0] == 2:
            x = i
            y = 0
            while True:
                x,y = checkAdjacentTwo(arr, x, y, n)
                if not ind:
                    break
                if y == N-1:
                    twoCon = True


if oneCon and twoCon:
    print("AMBIGUOS")
elif oneCon:
    print("1")
elif twoCon:
    print("2")
else
    print("0")
