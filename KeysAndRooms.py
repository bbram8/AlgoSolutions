# reference - https://leetcode.com/problems/keys-and-rooms/description/
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
    
        """
        Logic: 
        BFS using queue
        - Push the first unlocked rooms into q (room 0 in this case)
        - Pop from Q and for each room that is popped
            - go to the index in the array and unlock the room
            - push keys in this room to Q
            - maintain a visited set to track the rooms we've been to
            - if len(visited) == len(rooms) then return true else return false 
        """

        if not rooms:
            return False
    
        rooms_q = collections.deque([rooms[0]])
        visited = set()

        visited.add(0)

        while rooms_q: 
            key_set = rooms_q.popleft()

            for key in key_set:
                if key not in visited:
                    visited.add(key)
                    # Now you add the room to the queue so you can get its keys
                    # the next time you iterate
                    rooms_q.append(rooms[key])
    
        return True if len(visited) == len(rooms) else False

