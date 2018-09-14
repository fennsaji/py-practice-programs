for i in range(n):
    string = input()
    j = 1
    subStrings = string.split('*')
    count = 0
    for ss in subStrings:
        if not 'X' in ss:
            count+= ss.count('O')
    print(count)
