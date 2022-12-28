def quickSort(array):
    if len(array)>1:
        pivot = array.pop()
        items_greater = []
        items_lower = []
        for item in array:
            if item >pivot:
                items_greater.append(item)
            else:
                items_lower.append(item)
        
        return (quickSort(items_lower) + [pivot]+ (quickSort(items_greater)))
    else:
        return array
    
array = [6, 2, 1, 4, 5, 8, 0]

print(quickSort(array))

