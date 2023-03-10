#https://leetcode.com/problems/fizz-buzz/
"""
Readable code
"""

def fizzBuzz(n):
        lis= []
        for each in range(1,n+1):
            if each%3==0:
                if each%5==0:
                    ele = 'FizzBuzz'
                else:
                    ele = 'Fizz'
            elif each%5==0:
                ele = 'Buzz'
            else:
                ele = str(each)
            lis.append(ele)
        return lis

n=30
print(fizzBuzz(n))