'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t = int(input())
h = int(input())

def second_smallest(numbers):
    m1, m2 = float('inf'), float('inf')
    for x in numbers:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2

for _ in range(t):
    arr = []
    for _ in range(h):
        hcol = list(map(int, input().split()))
        arr.append(hcol)
    premini = min(arr[0])
    pmind = arr[0].index(premini)
    sum = 0
    for i in range(h):
        if i == h-1:
            sum+=premini
            break
        mini = min(arr[i+1])
        mind = arr[i+1].index(mini)
        if mind == pmind:
            if mini > premini:
                mini = second_smallest(arr[i+1])
                mind = arr[i+1].index(mini)
            else:
                premini = second_smallest(arr[i])
                pmind = arr[i].index(premini)
        sum+=premini
        premini = mini
        pind = mind
        # else:
        #     sum+=mini+premini
        #     premini = mini
        #     pind = mind
    print(sum)
        
