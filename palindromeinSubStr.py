s = input()

j = len(s)
count = 0

for i in range(len(s)):
    while i+1:
        temp = s[i:i+j]
        if temp == temp[::-1]:
            count+=1
        i-=1
    j-=1
print(count)
