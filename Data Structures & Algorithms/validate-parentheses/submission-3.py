class Solution:
    def isValid(self, s: str) -> bool:
        
        valid_parentheses = {')':'(', '}':'{',']':'['}
        stack = []

        for ch in s:
            if ch in valid_parentheses:
                if not stack or stack.pop() != valid_parentheses[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack