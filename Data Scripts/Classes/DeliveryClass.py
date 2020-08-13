class Shift:
    #instance attributes
    def __init__(self, tiplist=[], milesdriven=None, storehours=None, roadhours=None, date=None):
        self.tiplist = tiplist # this 
        self.milesdriven = milesdriven
        self.storehours = storehours
        self.roadhours = roadhours
        self.date = date # format MM/DD/YY
        
        
    #public class variables
        
    def update_tip_list(self):
        
        completed = False
    
        
        while completed != True:
            
            completed = input("Enter the the tip values one at a time, once complete enter False: ")
            
            if completed == "False":
                completed = bool(completed)
            else:
                self.tiplist.append(float(completed))
                
        
        return self.tiplist
    
    def update_miles_driven(self):
        
        numofmiles = input("Enter the number of miles: ")
        self.milesdriven = numofmiles # updating class attribute
        
        return
    
    def update_store_hours(self):
        
        shours = input("Enter the number of store hours: ")
        self.storehours = shours # updating class attribute
        
        return
    
    def update_road_hours(self):
        
        rhours = input("Enter the number of road hours: ")
        self.roadhours = rhours
        
        return
        
    def get_date(self):
        d = input("Enter the date of the shift (format: DD/MM/YY): ")
        self.date = d
        
        return
        
    def print_tip_list(self):
        print("Updated: ", self.tiplist)
        
        return 


User = "Not Done" # Enter the loop
shifts = [] # organization for storing shift data classes

while User != "Done":
    ShiftClassification = input("Enter either morning, mid, or evening to classify the shift: ")
    ShiftClassification = Shift()
    ShiftClassification.update_tip_list()
    ShiftClassification.update_store_hours()
    ShiftClassification.update_road_hours()
    ShiftClassification.get_date()
    User = input("Are you done yet? If so enter:  ""Done""")
    shifts.append(ShiftClassification)
    
    
    
    
    
            
        

    

            
            
    
            
            
       
            
            
            
            
        
        
        
        
    
    