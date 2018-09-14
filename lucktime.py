# Write your code here
n = int(input())

def formatTime(h,m,s):
    if h//10 == 0:
        h= "0"+ str(h)
    if m//10 == 0:
        m = "0"+ str(m)
    if s//10 == 0:
        s = "0"+str(s)
    time = str(h)+":"+str(m)+":"+str(s)
    return time

def checkAllSame(h,m,s):
    time = formatTime(h,m,s)
    for i in range(len(time)):
        if time[i] == ':':
            continue
        if time[i] in time[i+1:]:
            return False
    return True

for t in range(n):
    s = input()
    h,m,s = list(map(int, s.split(":")))
    while True:
        if checkAllSame(h,m,s):
            print(formatTime(h,m,s))
            break
        if m == 59 and s == 59:
            h=(h+1)%24
            m=0
        if s == 59:
            m+=1
            s =-1
        s+=1
