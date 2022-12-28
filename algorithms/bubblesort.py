def bubbleSort(array):
    sorted = False
    while not sorted :
        
        sorted = True
        # len(array)-1 because we can't compare the number to the last position with another number as it is the last
        if len(array) == 1:
            return array
        else: 
            for i in range(len(array)-1):
                if array[i] > array[i+1]:
                    sorted = False
                    array[i], array[i+1] = array[i+1], array[i]
                
    return array        

array = [ 5]


print(bubbleSort(array))