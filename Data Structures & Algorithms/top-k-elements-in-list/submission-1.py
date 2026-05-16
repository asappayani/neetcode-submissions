from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        solution:
        iterate through nums and build a frequency map for each number
        create a list with pairs of (frequency, number)
        sort that list
        grab the last k elements in the list
        """

        hashmap = defaultdict(int)
        pairs = []
        ans = []

        for num in nums:
            hashmap[num] += 1

        for key in hashmap:
            pairs.append((hashmap[key], key))
        pairs.sort()

        for i in range(k):
            ans.append(pairs[len(pairs)-1-i][1])

        return ans
    


        

