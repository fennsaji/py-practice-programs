import numpy as np
t, r, g, b = list(map(int, input().split()))
red = r
gre = g
blu = b
redOn = [0]*t
greenOn = [0]*t
blueOn = [0]*t

for i in range(t):
    if r<t:
        redOn[r:r+red] = np.ones(red, dtype=int)
        r = r + 2*red
    if g<t:
        greenOn[g:g+gre] = np.ones(gre, dtype=int)*4
        g = g + 2*gre
    if b<t:
        blueOn[b:b+blu] = np.ones(blu, dtype=int)*8
        b = b + 2*blu

r=g=b=y=c=m=w=bl=0
for i in range(t):
    val = redOn[i]+greenOn[i]+blueOn[i]
    if val == 0:
        bl+=1
    elif val == 1:
        r+=1
    elif val == 4:
        g+=1
    elif val == 8:
        b+=1
    elif val == 5:
        y+=1
    elif val == 12:
        c+=1
    elif val == 9:
        m+=1
    elif val == 13:
        w+=1

print("{} {} {} {} {} {} {} {}".format(r,g,b,y,c,m,w,bl))
        
