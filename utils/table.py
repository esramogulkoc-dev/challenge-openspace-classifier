class Table:
    
    def __init__(self,capacity): 
       self.capacity = capacity
       self.seats = [Seat() for _ in range(capacity)] 
       
    def has_free_spot(self): 
        for seat in self.seats:
            if seat.free:  
                return True
        return False 


    def assign_seat(self,name):   
        for seat in self.seats:
            if seat.free: 
                seat.set_occupant(name) 
                return(f"{name} is assigned to this table") 
        return ("No seats left") 
    
    def left_capacity(self): 
            left_capacity = 0
            for seat in self.seats:
                if seat.free:
                    left_capacity +=1
            return left_capacity
