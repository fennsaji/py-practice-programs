def kaprekarNumbers(p, q):
    for i in range(p,q):
        square = i * i;
        fh = sh = 0;
        length = int(len(str(square)))
        lenHalf = length - (length//2)
        if length!=0:
            fh = square//(10**lenHalf)
            sh = square%(10**lenHalf)
        if fh+sh == i:
            print(i, end=" ")
        

kaprekarNumbers(1, 99999)
