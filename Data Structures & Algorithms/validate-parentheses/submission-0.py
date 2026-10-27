class Solution:
    def isValid(self, s: str) -> bool:
        
        valid_parentheses = {')':'(', '}':'{',']':'['}
        stack = []

        for ch in s:
            if ch in valid_parentheses:
                if not stack or stack[-1] != valid_parentheses[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return True if not stack else False