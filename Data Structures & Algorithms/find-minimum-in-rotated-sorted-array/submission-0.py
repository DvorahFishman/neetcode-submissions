class Solution:
    def findMin(self, nums: List[int]) -> int:
        right = len(nums) - 1
        left = 0 
        min_num = nums[0]
        while left <= right:
            mid = (left + right) // 2
            min_num = min(min_num, nums[mid])
            if nums[left] <= nums[right]:
                return min(min_num, nums[left])
            if nums[left] > nums[mid]:
                right = mid - 1
            else :
                left = mid + 1
        return min_num