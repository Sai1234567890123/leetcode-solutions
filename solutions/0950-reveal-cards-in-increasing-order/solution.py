from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        n = len(deck)
        # Sort the deck so we can place cards in increasing order
        sorted_deck = sorted(deck)

        # Use a queue to simulate the card-revealing process on indices
        index_queue = deque(range(n))
        result = [0] * n

        for card in sorted_deck:
            # The next revealed slot gets the smallest available card
            reveal_idx = index_queue.popleft()
            result[reveal_idx] = card

            # Move the next top index to the bottom of the deck if cards remain
            if index_queue:
                index_queue.append(index_queue.popleft())

        return result
