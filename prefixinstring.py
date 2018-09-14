s = input()
t = input()

i = 0
count = 0
for ch in s:
    t = t[i:]
    try:
        i = t.index(ch)
        print(t, i , count)
        if i>=0:
            count+=1
        else:
            break
        i+=1
    except:
        break
print(count)

