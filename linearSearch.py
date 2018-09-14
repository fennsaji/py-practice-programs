def linearSearch(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return -1

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    i = linearSearch(arr, 5)
    print(i)
