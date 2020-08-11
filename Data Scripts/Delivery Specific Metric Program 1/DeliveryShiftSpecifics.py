# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 20:04:30 2020

@author: 15123
"""


def ToCSV(Date, Tips, TotalMiles):
    
    """
    Date: date of the delivery shift, (format MM/DD/YYYY), ex. 12/06/2000
    Tips: List of floating point dollar numeric values you made in that shift, ex. [12.00, 5.00, 6.00, 3.14, 5.10]
    TotalMileage: Floating point number of miles driven, ex. 50.6
    """
    
    with open("DeliveryData.csv", "a") as csvHeaders:  # writing new dates I'm doing this every time not sure how to store the data in csv without overwriting it everytime...
        csvHeaders.write(Date)
                 
         
    with open("DeliveryData.csv", "a") as csvData:     # writing each dates data for the column
        
        for i in range(len(Tips)-2):
            csvData.write(str(i)+",")
        
        csvData.write(str(TotalMiles)+"\n")
        
        return
    

def GetShiftData():
    
    Dates = input("Enter the Date in this format: MM/DD/YYYY: ")
    Tips = []
    tip = 0
    
    while tip != "done":
        tip = input("Input tip value, input done once no tips left from shift to enter: ")
        Tips.append(tip)
        
    TotalMiles = input("Enter the total miles driven during the shift: ")
    
    return (Dates, Tips, TotalMiles)

a = GetShiftData()

ToCSV(a[0], a[1], a[2])
    
    
    
            
            
    
        
        
    