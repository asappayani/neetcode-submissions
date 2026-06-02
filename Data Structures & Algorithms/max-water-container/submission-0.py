class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        length = distance between index i and j (right - left)
        width = min(bar 1, bar 2)

        whichever pointer is pointing to the smaller bar, increment that pointer to the next bar
        keep note of the biggest area
        """
        left = 0
        right = len(heights) - 1

        ans = 0

        while left < right: 
            length = right - left
            width = min(heights[left], heights[right])

            ans = max(ans, length * width)

            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
                right -= 1
        
        return ans