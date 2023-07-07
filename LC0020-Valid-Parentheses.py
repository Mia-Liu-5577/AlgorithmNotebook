class Solution:
    def canBeClosed(self, c1, c2):
        if (c1 == '(' and c2 == ')') or \
            (c1 == '[' and c2 == ']') or \
            (c1 == '{' and c2 == '}'):
            return True
        return False

    def isValid(self, s: str) -> bool:
        p_stack = []
        for c in s:
            # check if the current parentheses can be closed, if yes
            # pop out the top element
            if len(p_stack) > 0 and self.canBeClosed(p_stack[-1], c):
                p_stack.pop()
                continue
            p_stack.append(c)
        return len(p_stack) == 0
