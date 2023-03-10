#https://leetcode.com/problems/valid-parentheses/
"""
Iter each item and keep adding to que if not matching with param_map.
If matchhed remove last item from que. If que empty its valid.
"""
def isValid(s):
    param_map = {"{":"}",
                 "[":"]",
                 "(":")"}
    que = ''
    for each in s:
        if not que or param_map.get(que[-1]) != each:
            que += each
        else:
            que = que[:-1]
    if que:
        return False
    else:
        return True
s='()[]{}'
s="([)]"
print(isValid(s))