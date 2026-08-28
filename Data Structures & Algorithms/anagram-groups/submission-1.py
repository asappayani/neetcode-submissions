from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
            for each str in strs, we iterate through each char in a str, create a freq map for each char.

            take that freq map, turn it into a frozen set, then check mastermap if that freq map
            is already a key, if so, then append that str to the list

            mastermap = {
                {h:1, a:1, t:1} : ["hat",]
                .
                .
                .
                .
            }

            get all lists into the answer list by iterating through every value in mastermap
        """

        ans = []
        mastermap = defaultdict(list)

        for word in strs:
            freq = defaultdict(int)

            for char in word:
                freq[char] += 1

            freq = frozenset(freq.items())
            mastermap[freq].append(word)
        
        for v in mastermap.values():
            ans.append(v)

        return ans


