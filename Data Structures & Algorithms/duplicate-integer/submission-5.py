class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = {}
        for i in nums:
            check[i] = check.get(i,0)+1
        for i in check.values():
            if i >1:
                return True
        return False
            


      