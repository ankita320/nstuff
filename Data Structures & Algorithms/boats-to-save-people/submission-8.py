class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #sort numbers
        #l and r
        #count var
        #check w l and right add and check -> if sum > limit -> mv left by 1
        #check if r = limit -> count that
        # r > limit, break
        people.sort()
        l = 0
        r = len(people) - 1
        boats = 0
        
        while l <= r:
            # If the lightest and heaviest can fit together
            if people[l] + people[r] <= limit:
                l += 1  # Lightest person gets on the boat
            
            # Heaviest person always gets on the boat
            r -= 1
            boats += 1  # Increment boat count
            
        return boats