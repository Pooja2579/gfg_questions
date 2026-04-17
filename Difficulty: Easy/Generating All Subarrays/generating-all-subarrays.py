#User function Template for python3
class Solution:
    def getSubArrays(self, arr, start = 0, end = 0, result= None):
        #code here
        if result is None:
            result = []
            
        if start >= len(arr):
            return result  
            
        if end >= len(arr):
            return self.getSubArrays(arr, start + 1, start + 1, result)
        
      
        result.append(arr[start:end + 1])
   
        return self.getSubArrays(arr, start, end+1, result)