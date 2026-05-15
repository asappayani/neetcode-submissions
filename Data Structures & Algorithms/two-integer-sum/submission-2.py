from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        solution:
        for each num, find the number that needs to be added to it and save that number in a set. 
        for each num, check if it's in the set. if it's in the set, then that number has a pair somewhere
        in the nums list, so we can return those two indices.

        edit: instead of a set, we'll use a hashmap so that we can store the required pair number and the
        index in which we found that pair number.

        nums = [3,4,5,6], target = 7

        hashmap = {
        4: 0,
        3: 1,
        2: 2,
        1: 3
        }

        """

        hashmap = defaultdict(int)
        ans = []

        for i in range(len(nums)):
            hashmap[target-nums[i]] = i
        
        for i in range(len(nums)):
            if nums[i] in hashmap and hashmap[nums[i]] != i:
                ans.append(i)
                ans.append(hashmap[nums[i]])
                return ans

