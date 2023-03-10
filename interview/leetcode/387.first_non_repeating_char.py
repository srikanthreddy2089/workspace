#https://leetcode.com/problems/first-unique-character-in-a-string/
"""
Iterate each letter and if its first time then add into dict(key is letter, value is position),
and also append to new string. If any letter is found in dict then remove the letter in new string. 
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