class Solution:
    def findKRotation(self, arr):
        # code here
        min_val = min(arr)
    
        return arr.index(min_val)
        