def chiceSort(arr):
    for i in range(len(arr)):
        minPos = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minPos]:
                minPos = j
        if minPos != i:
            arr[i], arr[minPos] = arr[minPos], arr[i]
    return arr
                
if __name__ == '__main__':
    arr = [3,2,5,1,4]
    arr = chiceSort(arr)
    print(arr)
