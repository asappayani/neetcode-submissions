class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """ 
        no duplicates, use frozenset for seen triplets

        Input: nums = [-1,0,1,2,-1,-4]
        [-4, -1, -1, 0, 1, 2]

        -4: 0 - -4 = 4
        can we find two numbers that will add to 4?

        -1 + 2 = 1 < 4
         less than means make left ++
         greater than means make right --

         if left < right then move on to next num b/c there is no triplet for that num

         -1: 0 - -1 = 1
         -4 + 2 = -2 < 1

         if left or right == curr num then move one more

         -1 + 2 = 1 (correct numbers found)

         triplet = (currnum, num[left], num[right])\
         check if triplet in seen, add if not
         so ans.append(triplet)
        """

        nums.sort()
        seen = set()
        ans = []

        for i in range(len(nums)):
            left = 0
            right = len(nums) - 1
            goal = 0 - nums[i]

            while left < right:
                if left == i:
                    left += 1
                    continue
                if right == i:
                    right -= 1
                    continue

                if nums[left] + nums[right] == goal:
                    triplet = [nums[i], nums[left], nums[right]]
                    if tuple(sorted(triplet)) not in seen:
                        seen.add(tuple(sorted(triplet)))
                        ans.append(triplet)
                    left += 1
                    right -= 1

                elif nums[left] + nums[right] < goal:
                    left += 1
                elif nums[left] + nums[right] > goal:
                    right -= 1
        
        return ans
                    



