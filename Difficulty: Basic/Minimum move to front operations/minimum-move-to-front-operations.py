
class Solution:
    def minMoves(self, arr):
        #code here
        n = len(arr)
        lookingfor = n
        
        for i in range(n-1, -1, -1):
            if arr[i] == lookingfor:
                lookingfor -=1
            
            
            
        return lookingfor