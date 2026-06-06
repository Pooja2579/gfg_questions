
from typing import List


class Solution:
    def findPair(self, arr: List[int], x: int) -> int:
        # code here
        arr.sort()
        left = 0
        right = 1
        while right < len(arr):
            diff = arr[right] - arr[left]
            if diff == x:
                return True
            elif diff < x:
                right += 1
            else:
                left += 1
            
            if left == right:
                right += 1
        return False
