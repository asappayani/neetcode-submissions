from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """ 
        sliding window with frequency map

        starting with both pointers at [0]
        whenever we see something not in our map increment longest by 1 and add letter to map
        do max(longest, ans)
        
        if we've seen it before, shorten window from left and decrement frequency of whatever we remove

        seen = {a: 1, b: 1, c: 1, }

        ans = "bca"
        """
        seen = defaultdict(int)
        ans = l = 0

        for r in range(len(s)):
            seen[s[r]] += 1

            while seen[s[r]] > 1:
                seen[s[l]] -= 1
                l += 1
            
            ans = max(ans, r - l + 1)

        return ans
            





                




        
            
            