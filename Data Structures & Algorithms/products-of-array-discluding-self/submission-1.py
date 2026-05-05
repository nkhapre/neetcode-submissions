class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod = 1
        flag = 0
        place = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                flag += 1
                place = i
                continue
            prod *= nums[i]
        ans = nums
        if flag ==1:
            ans = [i*0 for i in ans]
            ans[place] = prod
            return ans
        if flag >1:
            ans = [i*0 for i in ans]
         
            return ans
        for i in range(len(nums)):
            ans[i] = prod//nums[i]
        return ans
            



                