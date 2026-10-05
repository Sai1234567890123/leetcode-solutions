class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        total_time = 0
        last_m = last_p = last_g = 0
        
        # 1. Total pickup time is simply the total length of all strings in garbage.
        # 2. Track the farthest house index that contains each type of garbage.
        for i, g in enumerate(garbage):
            total_time += len(g)
            if 'M' in g:
                last_m = i
            if 'P' in g:
                last_p = i
            if 'G' in g:
                last_g = i
                
        # Compute prefix sums of travel times to quickly get travel cost to any house.
        # travel_prefix[i] stores the travel time from house 0 to house i.
        prefix_sum = 0
        travel_prefix = [0] * len(garbage)
        for i in range(len(travel)):
            prefix_sum += travel[i]
            travel_prefix[i + 1] = prefix_sum
            
        # Add travel times for each truck up to its respective last house.
        total_time += travel_prefix[last_m]
        total_time += travel_prefix[last_p]
        total_time += travel_prefix[last_g]
        
        return total_time
