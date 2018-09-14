# Write your code here
n = int(input())

arr = list(map(int, input().split()))

print("NO")
while True:
    #g = max(arr)
    if any(v == 0  for v in arr):
        print("NO")
        break
    flag = False
    for i in range(0, n-1):
        arr[i] -= 1
        arr[i+1] -= 1
        if all(v == 0 for v in arr):
            flag = True
            print("YES")
            break
        if arr[i]==0 or arr[i+1]==0:
            
            flag = True
            print("NO")
            break
    if flag:
        break
