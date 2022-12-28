def linearSearch(element, arr):
    for elem in range(len(arr)):
        if arr[elem] == element:
            return f"Element {element} found at index {elem} of the array"
        
    return -1
        
print(linearSearch(10, [2,3,4,5,6,10,11,12]))