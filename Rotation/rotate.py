# Rotate by 2 is same as shifting all elements to the right by 2
# e.g [1,2,3,4,5,6] -> [3,4,5,6,1,2]

def rotate(arr, r):
    lastpart = arr[:r]
    firstpart = arr[r:]
    firstpart.extend(lastpart)
    return firstpart
    
   
print(rotate([1,2,3,4,5,6], 7)) 