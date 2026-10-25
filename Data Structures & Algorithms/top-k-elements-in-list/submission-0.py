class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_frequent = {}
        for num in nums:
            if num in count_frequent:
                count_frequent[num] += 1
            else: 
                count_frequent[num] = 1
        count_num = [[] for _ in range(len(nums) + 1)]
        for num, freq in count_frequent.items():
                count_num[freq].append(num)
        result = []
        for i in range(len(count_num) - 1, 0, -1):
            for num in count_num[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result