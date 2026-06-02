class Solution:
    def findMinDiff(self, arr, m):
        # code here
        arr.sort()
        
        if m == 0 or m> len(arr):
            return 0
        min_diff = float('inf')
        
        for i in range(0, len(arr)-m+1):
            curr_diff = arr[i+m-1]-arr[i]
            min_diff = min(min_diff, curr_diff)
            
        return min_diff