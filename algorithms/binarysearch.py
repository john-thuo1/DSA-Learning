def binarySearch(start, end, element, array):
    midpoint = ((start+end)//2)
    if (array==sorted(array)):
    
        if (start>end):
            return "Element Does not exist"
    
        if array[midpoint] == element:
            return f"Found element {element} at index {midpoint}"
        elif array[midpoint] < element:
            return binarySearch(midpoint,end, element, array)
        else:
            return binarySearch(start, midpoint-1, element, array)
    else:
        return "Array not Sorted"
array = [2,3,4,5,6, 8, 9, 10] 
element = 9      
start = 0
end = len(array)

print(binarySearch(start, end, element, array))
    