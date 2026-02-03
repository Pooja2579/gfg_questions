class Solution:
    def missingNum(self, arr):
        # code here
        n = len(arr) + 1
        total_sum = n*(n+1) // 2
        sum_arr = sum(arr)
        return total_sum - sum_arr