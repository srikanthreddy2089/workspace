#https://leetcode.com/problems/rectangle-area-ii/
"""
update the total area, take two consecutive points and find the total height of the interval bettween them (by merging height intervals),
then update the area by (point2 - point1) * height
"""

def rectangleArea(self, r):
    g = [i  for x1, y1, x2, y2 in r for i  in [[x1,y1,y2,0],[x2,y1,y2,1]]]
    ans, last, heap = 0, g[0][0], [(1e10,1e10)]
    for x, y1, y2, k in sorted(g):
        h = start = end =  0
        for (m,n) in heap:
            if m > end:
                h += end - start
                start, end = m, n
            else:
                end = max(end, n)  
        ans += (x-last) * h 
        heap.remove((y1,y2)) if k else bisect.insort(heap,(y1,y2))
        last = x 
    return ans % (10 ** 9 + 7)

