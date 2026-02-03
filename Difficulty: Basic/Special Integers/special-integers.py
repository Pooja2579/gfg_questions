
from typing import List


class Solution:
    def specialIntegers(self, n : int, arr : List[int]) -> int:
        # code here
        set_arr = set(arr)
        
        k = 0
        
        for i in set_arr:
            if (i-1)  in set_arr and (i+1) in set_arr:
                k+=1
                
        return k
                
            
        
        
        
