class Solution:
    def isValid(self, s: str) -> bool:
        """
            use a stack, if its an open bracket character, push to stack, if its closed, check the top
            stack to see if they match then pop the stack. if they don't match, return false
        """
        stack = []
        matching = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        for char in s:
            if char in matching:
                stack.append(char)
            else:
                if not stack:
                    return False

                top = stack.pop()
                if matching[top] != char:
                    return False
            
        return not stack




