
#https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack=[]
        for i in s:
            if i=='(' or i=='{' or i=="[":
                stack.append(i)
            else:
                if stack:
                    x=stack.pop()
                    if (x=='(' and i==')') or (x=='{' and i=='}') or (x=='[' and i==']'):
                        pass
                    else:
                        return False

                else:
                    return False
        if stack==[]:
            return True
        else:
            return False
