class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i, n in enumerate(nums):
            diff = target-n
            if diff not in check:
                check[n] = i
                
            else:return [check[diff], i]
            
        

        