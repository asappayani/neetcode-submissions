class Solution:
    def trap(self, height: List[int]) -> int:
        """
        -have left at beginning and right at end.
        -track the current maxleft and maxright
        -shift the pointer whose max height is smaller
        -when a pointer is shifted, subtract the current max (left or right) by the new height thats being
        pointed to, this will tell us how much water can be held at that h[i]. (if < 0 then 0 water can 
        be held at h[i]).
        - update maxes
        - if maxes are equal then just shift one of them

        """
        if not height: return 0

        maxleft = height[0]
        maxright = height[-1]

        left = 0
        right = len(height) - 1

        ans = 0

        while left < right:
            if maxleft < maxright:
                left += 1

                waterAmount = maxleft - height[left]
                if waterAmount > 0:
                    ans += waterAmount
                
                maxleft = max(maxleft, height[left])
            else:
                right -= 1

                waterAmount = maxright - height[right]
                if waterAmount > 0:
                    ans += waterAmount
                
                maxright = max(maxright, height[right])
            
        return ans

                