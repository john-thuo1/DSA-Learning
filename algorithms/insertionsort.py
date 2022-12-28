def insertionSort(array):
    for i in range(1, len(array)):
        while array[i-1] > array[i] and i>0:
            array[i], array[i-1] = array[i-1], array[i]
            i-=1
            
    return array

array = [ 6,4,5,2,1,0]

print(insertionSort(array))


        
    