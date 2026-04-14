class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # No. of Cars
        n = len(position)
        ttr = list(zip(position,speed))
        ttr.sort(reverse=True)

        stack = []
        for pos,spe in ttr:
            
            time = (target - pos)/spe
             
            if not stack or time > stack[-1]:
                stack.append(time)

                
        return len(stack)
            
