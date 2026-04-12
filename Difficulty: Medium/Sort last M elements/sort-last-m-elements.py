#User function Template for python3

class Solution:
	def sortLastMelements(self, nums, n, m):
		# code here
        # if len(arr)<=1:
        #     return arr
    
        # left_arr = arr[:n]
    
        # # last elements 
        # right_arr = arr[-m:]
    
        # sorted_right_arr = self.merge_sort(right_arr)
    
        # return left_arr + sorted_right_arr
        
        last_m = nums[n:]
        
        sorted_last_m = self.merge_sort(last_m)
        for i in range(m):
            nums[n+i] = sorted_last_m[i]
           
       
    def merge_sort(self, arr):
        if len(arr)<=1:
            return arr
        
        mid = len(arr)//2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
    
        return self.merge(left, right)
    
    
    def merge(self, left, right):
        res = []
        i, j = 0, 0
    
        while i < len(left) and j<len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
    
        while i<len(left):
            res.append(left[i])
            i+=1
        while j<len(right):
            res.append(right[j])
            j+=1
    
    
        return res
