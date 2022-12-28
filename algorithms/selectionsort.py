"""The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending
order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array. 1)
The subarray which is already sorted. 2) Remaining subarray which is unsorted. In every iteration of selection sort,
the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted
subarray. """
'''Example [2,1,9,6,7] . 2 Arrays Sorted[2]  unsorted[1,9,6,7] Minimum value is 2. Loop through the array and change 
  minimum value to 1 and keep doing this throughout.'''
""" The issue with Bubble sort is for every iteration, swapping takes a lot of processing power."""
def selectionSort(array):
    for i in range(len(array)-1):
        minimumValuePosition = i   # Default Minimum value index that will likely change as we loop
         # The loop i+1 represents elements to the right / the unsorted array of elements
        for j in range(i+1,len(array)):
            # If element to the right in the unsorted list is less than chosen minimum element, swap the 2
            if array[j] < array[minimumValuePosition] :
                minimumValuePosition = j
        # Now swap the values.        
        array[minimumValuePosition], array[i] = array[i], array[minimumValuePosition]
            
    return array


array = [9,1,3,4,5,1,6]
print(selectionSort(array))
                
        
        
        