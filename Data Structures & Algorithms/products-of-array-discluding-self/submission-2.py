class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        flag = 0
        prod = 1
        ans = nums
        place = 0
        for i in range(len(nums)):
            if nums[i] ==0:
                flag += 1
                place = i
                continue
            prod *= nums[i]
        if flag == 1:
            ans = [i *0 for i in ans]
            ans[place] = prod
            return ans
        elif flag >1:
            ans = [i *0 for i in ans]
            return ans
        else:
            for i in range(len(nums)):
                ans[i] = prod//nums[i]
            return ans






            



                
       