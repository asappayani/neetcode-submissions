from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """ 
        solution 1: iterate through both strings and create a map for the frequency of every character.
        check if those maps are equal

        solution 2: iterate through first string and get frequency of every character, then iterate through
        second char and start subtracting every character that's already in the map. characters not in
        map = return false. characters whose frequency doesn't = 0 by the end means return false

        solution 3: do set() for each string and then check if they're equal. edit: nope b/c there can be 
        multiple of one character
        """
        hashmap = defaultdict(int)

        for char in s:
            hashmap[char] += 1

        for char in t:
            if char not in hashmap:
                return False

            hashmap[char] -= 1

        for key in hashmap:
            if hashmap[key] != 0:
                return False

        return True
        

        