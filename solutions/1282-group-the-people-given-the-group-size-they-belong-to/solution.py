from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        result = []
        # Maps group_size -> list of candidate person IDs currently accumulating
        buckets = defaultdict(list)
        
        for person_id, size in enumerate(groupSizes):
            buckets[size].append(person_id)
            # Once the bucket reaches its required capacity, flush it into result
            if len(buckets[size]) == size:
                result.append(buckets[size])
                buckets[size] = []
                
        return result
