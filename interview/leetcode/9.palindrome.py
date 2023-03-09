#https://leetcode.com/problems/palindrome-number/
"""
Iterate for half of the length, and keep checking first and last elements until half iteration.
"""

def isPalindrome(x):
    number_string = str(x)
    half = len(number_string)//2
    for pos in range(half):
        if number_string[pos] != number_string[-(pos+1)]:
            return False
    return True

print(isPalindrome(122221))