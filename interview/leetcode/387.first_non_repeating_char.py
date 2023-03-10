#https://leetcode.com/problems/first-unique-character-in-a-string/
"""
"""

def firstUniqChar(s):
    table = {}
    ans = ''
    for pos in range(len(s)):
        temp = s[pos]
        if temp not in table:
            table[temp] = pos
            ans = ans + temp
        else:
            ans = ans.replace(temp,'')
    return table[ans[0]] if len(ans) else -1

s= 'aabb'
s= 'aab'
print(firstUniqChar(s))