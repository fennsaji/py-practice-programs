def bubbleSort(arr):
    for i in range(len(arr)-1, 0, -1):   
        for j in range(i):
            if arr[j+1] < arr[j]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

if __name__ == "__main__":
    arr = [3,4,2,1,0,6,5]
    print(arr)
    arr = bubbleSort(arr)
    print(arr)
        
