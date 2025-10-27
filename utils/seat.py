class Seat:  

    def __init__(self):
        self.free = True
        self.occupant = ""


    def set_occupant(self,name):
        if self.free:  
            self.occupant = name
            self.free = False  
            print ( f"This seat is occupied by {self.occupant}")  
        else : 
            print ("This seat was already taken") 

    def remove_occupant(self):  
        if not self.free:
            name = self.occupant
            self.occupant = ""
            self.free = True
            print(f"{name} has been removed from the seat")
        else:
            print("This seat is already free")