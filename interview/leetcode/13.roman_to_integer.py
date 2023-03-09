#https://leetcode.com/problems/roman-to-integer/description/
"""
Iterate from reverse of roman string. While iteration compare with current and right side element.
First iteration assinging right side element as None
"""
map_romans = {
            "I": 1,
            "V": 5, 
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500, 
            "M": 1000
            }
def romanToInt(s):
    nex = None
    sum = 0
    for pos in range(len(s)):
        current = map_romans[s[-(pos+1)]]
        if not nex or current >= nex:
            sum = sum + current
        else:
            sum = sum - current
        nex = current
    return sum

print(romanToInt('MCMXCIV'))#1994