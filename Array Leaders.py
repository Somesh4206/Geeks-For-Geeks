class Solution:
    def leaders(self, arr):
        n = len(arr)
        leaders_list = []
        maxRight = arr[-1]
        leaders_list.append(maxRight)
        for i in range(n-2, -1, -1):
            if arr[i] >= maxRight:
                leaders_list.append(arr[i])
                maxRight = arr[i]
        leaders_list.reverse()
        return leaders_list
