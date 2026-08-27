from collections import defaultdict 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
            anagram: same characters and same character frequency
        """
        
        hashmap = defaultdict(int)

        for c in s:
            hashmap[c] += 1
        
        for c in t:
            hashmap[c] -= 1

        for key in hashmap:
            if hashmap[key] != 0:
                return False
        
        return True
