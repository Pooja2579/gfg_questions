class Solution:
    def insertionSort(self, arr):
        # code here
        for i in range(1, len(arr)):
            current_element = arr[i]
            # points to the perevious element
            j = i- 1
            while j>=0 and arr[j]>current_element:
                arr[j+1] = arr[j]
                j-=1
                arr[j+1]=current_element
            
        return arr