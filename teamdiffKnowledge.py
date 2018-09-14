# Write your code here
t = int(input())

for _ in range(t):
    temp = list(map(int, input().split()))
    n = temp[0]
    arr = temp[1:]
    arr.sort()
    team = []
    for i in range(n//2):
        team.append(arr[i]+arr[n-1-i])
    team.sort()
    diff = team[(n//2)-1]-team[0]
    print(diff)
