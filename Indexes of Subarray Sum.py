class Solution:
    def subarraySum(self, arr, target):
        start=0
        cur_sum =0
        for end in range(len(arr)):
            cur_sum+=arr[end]
            while cur_sum > target and start<end:
                cur_sum -= arr[start]
                start+=1
            if cur_sum == target:
                return [start+1,end+1]
        return [-1]
