class Solution:
    def maxSubarraySum(self, arr):
        maxx=arr[0]
        s=arr[0]
        for i in range(1,len(arr)):
            s=max(arr[i],s+arr[i])
            maxx=max(maxx,s)
        return maxx
