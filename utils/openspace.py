from utils.table import Table 
import random  

class Openspace:

    def __init__(self,number_of_tables): 
       self.tables = [ ]
       self.number_of_tables = number_of_tables
      
       for i in range (number_of_tables):  
           self.tables.append(Table(4)) 
     
    def organize(self,names): 
        for name in names:
            while True:
                table = random.choice(self.tables)  
                if table.has_free_spot():           
                    table.assign_seat(name)         
                    break                                 
      
    def display(self):   
        table_no = 1
        for table in self.tables:
            occupants = []
            for seat in table.seats:  
                if seat.free:
                    occupants.append("empty")
                else:
                    occupants.append(seat.occupant)
            print(f"Table {table_no}: {', '.join(occupants)}")
            table_no += 1

    def store(self,filename): 
        with open(filename, "w") as f : 
            table_no = 1 
            for table in self.tables :   
                occupants = []    
                for seat in table.seats :  
                    if seat.free:
                        occupants.append("empty")  
                    else:
                        occupants.append(seat.occupant) 
                f.write(f"Table {table_no}: {', '.join(occupants)}\n") 
                table_no += 1
          



        
