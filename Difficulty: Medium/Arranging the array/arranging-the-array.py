
from typing import List


class Solution:
    def Rearrange(self, n : int, arr : List[int]) -> None:
        # code here
        sorted_arr = self.merge_sort(arr)
        for i in range(n):
            arr[i] = sorted_arr[i]
        
        return arr
        
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
    
        while i < len(left) and left[i]<0:
            res.append(left[i])
            i+=1
        while j< len(right) and right[j]<0:
            res.append(right[j])
            j+=1
    
        while i<len(left):
            res.append(left[i])
            i+=1
        while j<len(right):
            res.append(right[j])
            j+=1
    
    
        return res