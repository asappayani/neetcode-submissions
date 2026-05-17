class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        create a set with nums to have o(1) lookup
        create a seen set so that we don't look through the same things again
        create a max length variable



        algorithm:
        1. iterate through nums
        2. if nums[i] in seen, then skip that one since we've already searched through it
        3. otherwise, do a while loop, if that num[i] + j exists, add to seen, keep track of a length variable
        4. check the max between current length and max length
        
        ex 1.
        nums = [20,4,10,3,4,5]
        numset = (2,20,4,10,3,4,5)
        seen = ()
        length = "-infinity"
        delta = 1

        loop:
        
        currlength = 0
        i = 0: 
            2 is not in seen, add it to seen, currlength + 1 -> while nums[i] + delta in numset 
                                -> add nums[i] + delta in seen 
                                -> currlength + 1
                                -> delta + 1
                length = max(length, currlength)
                delta = 1
                currlength = 0

        i = 1: 20 is not in seen, add it to seen, currlength + 1 -> same while loop
        i = 2: 4 is in seen, skip
        i = 3: 10 is not in seen, add to seen, currlength + 1 -> while loop
        i = 4: 3 is in seen, skip
        i = 5: 4 in seen, skip
        i = 6: 5 in seen, skip

        return length
        """

        if len(nums) == 0:
            return 0

        numset = set(nums)
        seen = set()
        length = float("-inf")

        for i in range(len(nums)):
            currlength = 0
            delta = 1

            if nums[i] not in seen:
                seen.add(nums[i])
                currlength += 1

                while nums[i] + delta in numset:
                    seen.add(nums[i] + delta)
                    currlength += 1
                    delta += 1
                
                length = max(length, currlength)

        return length

