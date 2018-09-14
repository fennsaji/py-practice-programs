from bubbleSort import bubbleSort as bs

def binarySearch(arr, item):
    mid = len(arr)//2
    beg = 0
    end = len(arr)-1
    while beg < end:
        print(beg,mid,end,arr[mid])
        if arr[mid] == item:
            return mid
        if item > arr[mid]:
            beg = mid+1
        else:
            end = mid
        mid = (beg+end)//2
    return -1

if __name__ == "__main__":
    arr = [5,3,4,2,0,1,8,7]
    arr = bs(arr)
    print(arr)
    i = binarySearch(arr, 3)
    print(i)
