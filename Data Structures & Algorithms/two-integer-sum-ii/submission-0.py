class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        idea: i think O(n^2) solution tbh
        two pointers
        check if right is equal to target - left, then those indices + 1 are your answer

        if not equal then right -= 1 and check again until 


        numbers = [1,2,3,4], target = 6

        another idea: binary search? this should be O(nlogn)
        """

        ans = []

        for left in range(len(numbers)):
            right = len(numbers) - 1

            while right > -1 and target - numbers[right] != numbers[left]:
                right -= 1

            if target - numbers[right] == numbers[left] and right != left:
                ans.append(left+1)
                ans.append(right+1)
                return ans
                    


                
