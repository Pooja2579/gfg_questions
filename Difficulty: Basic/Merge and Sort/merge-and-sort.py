class Solution:
    def mergeNsort(self, arr1, arr2):
        # code here
        merge_arr = arr1 +arr2
        
        mergers_merge_arr = list(set(merge_arr))
        mergers_merge_arr.sort()
        return mergers_merge_arr
        
    #     res = []
    #     i, j = 0, 0
    #     n, m = len(arr1), len(arr2)
    
    #     while i<n and j<m:
    #         if arr1[i]<= arr2[j]:
    #             res.append(arr1[i])
    #             i+=1
    #         else:
    #             res.append(arr2[j])
    #             j+=1
    
    
    #     if i<n:
    #         while i<n:
    #             res.append(arr1[i])
    #             i+=1
        
    #     if j<m:
    #         while j<m:
    #             res.append(arr2[j])
    #             j+=1
    
    
    #     return res
    
    
    
    # def merge_sort(self, arr):
        
        
        # if len(arr)<=1:
        #     return arr
        # mid = len(arr)//2
        # left_arr = arr[:mid]
        # right_arr = arr[mid:]
    
        # left = self.merge_sort(left_arr)
        # right = self.merge_sort(right_arr)
    
        # return self.mergeNsort(left, right)
            
