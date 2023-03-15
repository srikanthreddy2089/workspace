#https://leetcode.com/problems/rectangle-area/
"""
If overlap, the remove the common area from the area of two rectangles.
"""

def computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    area1 = abs(ax2-ax1)*abs(ay1-ay2)
    area2 = abs(bx1-bx2)*abs(by1-by2)
    w = min(ax2,bx2)-max(ax1,bx1)
    h = min(ay2, by2)-max(ay1,by1)
    if w<=0 or h<=0:
        return area1 + area2
    else:
        return area1 + area2 - w*h

print(computeArea(ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2))