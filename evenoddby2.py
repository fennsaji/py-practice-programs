n = int(input())
arr = []

for i in range(n):
    if i%2==0:
        arr.append(i)
    else:
        arr.append((i-1)//2)
print(arr)
