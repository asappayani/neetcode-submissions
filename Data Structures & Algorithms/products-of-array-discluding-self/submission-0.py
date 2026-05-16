class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        my attempt from only listening to his explanation

        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] * nums[i])
        
        postfix = [nums[-1]]
        for i in range(len(nums)-2, -1, -1):
            postfix.append(postfix[-1]*nums[i])

        postfix = postfix[::-1]

        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(postfix[0])
            else if i == len(nums) - 1:
                ans.append(prefix[len(nums)-2])
        """

        # yeahhhh i'ma have to come back to this one. here's the solution tho

        ans = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]

        return ans


