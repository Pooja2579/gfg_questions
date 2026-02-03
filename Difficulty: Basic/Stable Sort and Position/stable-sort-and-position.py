class Solution:
    # Function to get the index of an element in a sorted array
    def getIndexInSortedArray(self, arr, k):
        #Write Code Here
        value = arr[k]
        smaller_count = 0
        equal_bfr_count = 0
        
        
        for i in range(len(arr)):
            
            # 
            
            if arr[i]< value:
                smaller_count +=1
                
            # line count how many elements with teh smae value as our element werre originaaly before it in the array
                
            elif arr[i] == value and i<k:
                equal_bfr_count +=1
            
            
            
            
        return smaller_count + equal_bfr_count
        