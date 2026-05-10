class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = {}
        for i in nums:
            if i not in check:
                check[i] = check.get(i,0)+1
            else:
                return True
        return False
            
            


      