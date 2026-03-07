class Solution:
    def missingNum(self, arr):
        n=len(arr)+1
        summ=n*(n+1)//2
        s=sum(arr)
        return summ-s
