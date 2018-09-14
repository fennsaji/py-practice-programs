def gcd(n, i):
    for j in range(min(n,i)):
        if n%j==0 and i%j==0:
            break
    return 1

def foo(n):
    ret = 0
    for i in range(1, n):
        if gcd(n,i) is 1:
            ret+=1
    return ret
    
def specialSum(n):
    ret = 0
    for i in range(1, n):
        if n%i == 0:
            ret+=foo(i)
    return ret
    
n = int(input())
arr = list(map(int, input().split()))

for ch in arr:
    print(specialSum(ch), end=" ")
