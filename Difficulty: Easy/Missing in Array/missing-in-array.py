class Solution:
    def missingNum(self, arr):
        # code here
        n = len(arr) + 1   # because one number is missing

        expected_sum = n * (n + 1) // 2
        actual_sum = sum(arr)
    
        return expected_sum - actual_sum