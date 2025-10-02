class Solution:
    def isValid(self, s: str) -> bool:
        stack = []# Stack to keep track of opening brackets
        closeToOpen = {')':'(', ']':'[', '}':'{'}# Mapping of closing to opening brackets stored in a hashmap for O(1) lookup

        for c in s:# Iterate through each character in the string
            if c in closeToOpen:# If it's a closing bracket
                if stack and stack[-1] == closeToOpen[c]:# Check if the top of the stack matches the corresponding opening bracket
                    stack.pop()# If it matches, pop the top of the stack
                else:# If it doesn't match or the stack is empty
                    return False# The string is invalid
            else:# If it's an opening bracket
                stack.append(c)# Push it onto the stack
        return True if not stack else False# If the stack is empty at the end, all brackets were matched; otherwise, it's invalid