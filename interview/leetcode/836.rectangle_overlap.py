#https://leetcode.com/problems/rectangle-overlap
"""
bottom left of rec2 should be less than right top of rec1.
Also bottom left of rec1 should be less than right top of rec2
"""
def isRectangleOverlap(rec1, rec2):
    return rec2[0] < rec1[2] and rec2[1] < rec1[3] and rec1[0] < rec2[2] and rec1[1]< rec2[3]

print(isRectangleOverlap([0,0,2,2], [1,1,3,3]))