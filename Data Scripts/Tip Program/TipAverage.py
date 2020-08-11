# -*- coding: utf-8 -*-


def Update_tips(value):
    with open("C:/Users/15123/Desktop/Code/Python/Functions/PJs/Tips.csv", "a") as MyTips:
        MyTips.write(value)
        MyTips.write("\n")
    return 

    
def Average_tips(ListTips):
    Total = 0
    
    for EachTip in ListTips:
        Total += float(EachTip)
        
    Average = Total / len(ListTips)
    
    return (Average, Total, len(ListTips))   

Entry = input("Enter the tip value: ")

while Entry != "stop":
    
    Update_tips(Entry)
    
    with open("C:/Users/15123/Desktop/Code/Python/Functions/PJs/Tips.csv", "r") as ReadTip:
        TheData = ReadTip.readlines()
        print(Average_tips(TheData)[0]," is the running average of all your tips")
        print("$",Average_tips(TheData)[1]," is the total earned in tips")
        print(Average_tips(TheData)[2]," is the total runs executed")
        
    Entry = input("Enter the tip value: ")
    

    
with open("C:/Users/15123/Desktop/Code/Python/Functions/PJs/Tips.csv", "r") as ReadTip:
        TheData = ReadTip.readlines()    
print(Average_tips(TheData)[0]," is the running average of all your tips")
        
        