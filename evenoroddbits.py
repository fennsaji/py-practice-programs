n,q = list(map(int, input().split()))
arr = list(map(int, input().split()))
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        c = arr[query[2]-1:query[2]]
        if c==[0]:
            print("EVEN")
        else:
            print("ODD")
    elif query[0] == 1:
        if arr[query[1]-1] == 0:
            arr[query[1]-1] = 1
        elif arr[query[1]-1] == 1:
            arr[query[1]-1] = 0


