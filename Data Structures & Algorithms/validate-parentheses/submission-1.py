class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracketMap = {'[':']',
        '{':'}',
        '(':')'}

        for val in s:

            if val in bracketMap.keys():
                stack.append(val)
            else:
                if not stack or bracketMap[stack[-1]] != val:
                    return False
                stack.pop()
    
        return len(stack) == 0