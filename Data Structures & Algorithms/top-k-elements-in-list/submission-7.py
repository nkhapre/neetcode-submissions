class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        check = {}
        ans = []
        for i in nums:
            check[i] = check.get(i,0)+1
        for i in range(k):
            highest = max(check, key=check.get)
            ans.append(highest)
            check.pop(highest)
        return ans
        