from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        iterate through each num. do target - currentnum. if that value is in hashmap, return those indices
        """

        hashmap = defaultdict(int) # key: target - currentnum, value: index
        ans = []

        for i in range(len(nums)):
            if nums[i] in hashmap:
                ans.append(hashmap[nums[i]])
                ans.append(i)
                
                return ans

            hashmap[target - nums[i]] = i