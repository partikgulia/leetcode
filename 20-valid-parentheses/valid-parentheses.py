class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        closetopen= {')':'(','}':'{',']':'['}
        for c in s:
            if c in closetopen:
                if stack and stack[-1] == closetopen[c]:
                    stack.pop()
                else:
                    return False   
            else:
                stack.append(c)
        if not stack:
            return True
        else: 
            return False
        


                