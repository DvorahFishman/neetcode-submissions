class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int: 
        cars = sorted(zip(position, speed), reverse=True) 
        fleets = 0     
        previous_time_to_target = 0

        for pos, spd in cars:
            time_to_target = (target - pos) / spd
            if (time_to_target > previous_time_to_target):
                fleets += 1
                previous_time_to_target = time_to_target
                
        return fleets




                 
        





        