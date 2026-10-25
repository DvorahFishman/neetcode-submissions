class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        resultLeft = []
        resultRight = []
        for i in range(len(nums)):
            resultLeft.append(left)
            left *= nums[i]
        for i in range(len(nums) -1, -1, -1):
            resultRight.append(right)
            right *= nums[i]
        resultRight.reverse()
        resultArr = [x*y for x,y in zip(resultLeft, resultRight)]
        return resultArr
        
 
    