class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        
        self.dict = {1:big,2:medium, 3:small}
    def addCar(self, carType: int) -> bool:
        
        if not self.dict[carType]:
            return False
        self.dict[carType] -= 1
        return True
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

#Runtime: 136 ms, faster than 79.04% of Python3 online submissions for Design Parking System.
#Memory Usage: 14.4 MB, less than 92.00% of Python3 online submissions for Design Parking System.
#Fu-Ti, Hsu 
#shifty049@gmail.com
