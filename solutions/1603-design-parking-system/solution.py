class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        """
        Initializes the parking system with the given number of slots
        for each car type.
        Index 1: Big
        Index 2: Medium
        Index 3: Small
        Using a 1-indexed list avoids off-by-one arithmetic in addCar.
        """
        self.available_slots = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        """
        Checks if a slot is available for the given carType.
        If available, decrements the slot count and returns True.
        Otherwise, returns False.
        """
        if self.available_slots[carType] > 0:
            self.available_slots[carType] -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
