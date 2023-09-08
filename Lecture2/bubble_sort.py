def bubbleSort(arr):
    needSort = True
    while(needSort):
        needSort = False
        for i in range(len(arr) - 1):
            if(arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                needSort = True
    return arr            
                
if __name__ == '__main__':
    arr = [3,2,5,1,4]
    arr = bubbleSort(arr)
    print(arr)
