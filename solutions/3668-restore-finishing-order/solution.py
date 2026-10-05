from typing import List

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        # Step 1: Create a hash set (or 'set' in Python) from the 'friends' list.
        # This allows for O(1) average time complexity for checking if a participant ID
        # is one of our friends. The 'friends' list being sorted is not directly
        # leveraged here, as set construction and lookup don't depend on input order.
        friend_set = set(friends)
        
        # Step 2: Initialize an empty list to store the IDs of friends in their
        # finishing order. This list will be our final result.
        result = []
        
        # Step 3: Iterate through the 'order' array. This array represents the
        # participants in their exact finishing sequence.
        for participant_id in order:
            # Step 4: For each participant in the finishing order, check if their ID
            # is present in our 'friend_set'.
            if participant_id in friend_set:
                # If the participant is found in the 'friend_set', it means they are
                # one of our friends. We add their ID to our 'result' list.
                # By iterating through 'order' and appending, we naturally preserve
                # the relative finishing order of our friends.
                result.append(participant_id)
                
        # Step 5: After checking all participants in the 'order' array, the 'result'
        # list will contain all our friends' IDs in their correct finishing order.
        return result
