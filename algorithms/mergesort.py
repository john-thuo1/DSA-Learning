def mergeSort(array):
   lenOfArray = len(array)
   if lenOfArray>1:
   
       left_array = array[0:lenOfArray//2]
       right_array = array[lenOfArray//2:]
       
       mergeSort(left_array)
       mergeSort(right_array)

       i=0
       j=0
       k=0
       while i < len(left_array) and j <len(right_array):
           if left_array[i] <= right_array[j]:
               array[k] = left_array[i]
               i+=1
               k+=1
           else:
               array[k] = right_array[j]
               j+=1
               k+=1
       while i<len(left_array):
           array[k] = left_array[i]
           i+=1
           k+=1
        
       while j<len(right_array):
           array[k] = right_array[j]
           j+=1
           k+=1
       return array
   else:
       return array

           
           
array = [54,26,93,17,77,31,44,55,20]


print(mergeSort(array))  

           
    
       
       
       
        
        
       
       
    
    
    


