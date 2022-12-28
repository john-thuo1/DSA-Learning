def countSort(arr):
    k= max(arr)
    counts = [0]* (k+1)
   
   
    # Count the number of occurences in the arr
    for num in arr:
        counts[num] += 1
    
    # Cumulative Sums
    for elem in range(1, len(counts)):
        counts[elem] += counts[elem-1]
    
    # Create an array 
    newArray = [0 for _ in range(len(arr))]  
    
    # Sorting Phase
    for value in arr:
        index = counts[value] -1
        newArray[index] = value 
        counts[value] -=1
        
    return newArray
     
    
print(countSort([1,1,5,3,6,4]))    