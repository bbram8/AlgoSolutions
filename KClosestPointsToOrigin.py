# reference - https://leetcode.com/problems/k-closest-points-to-origin/description/
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # Use a min heap, hence the point furthest from origin will be the smallest element in the heap since we are storing by -(distance) on the heap
        
        heap = []

        for (x,y) in points:
            distance = -(x*x + y*y)
            if len(heap) == k:
                heapq.heappushpop(heap, (distance, x,y))
            else:
                heapq.heappush(heap, (distance,x,y))
        
        return [(x,y) for (distance,x,y) in heap]
            
