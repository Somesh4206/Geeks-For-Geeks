class Solution:
    def getSecondLargest(self, arr):
        largest = float('-inf')
        second_largest = float('-inf')
    
        for num in arr:
            if num > largest:
                second_largest = largest
                largest = num
            elif num < largest and num > second_largest:
                second_largest = num
    
        return second_largest if second_largest != float('-inf') else -1
    
