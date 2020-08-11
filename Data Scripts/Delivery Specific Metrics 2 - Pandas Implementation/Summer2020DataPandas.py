# -*- coding: utf-8 -*-
"""
Papa John's Delivery Data Summer 2020 Pandas data frame

@author: 15123
"""
import pandas as pd
import matplotlib as plt
def DDTDF(TipList, MD, SH, RH, Dates): # Delivery Data To Data Frame
    """
    Tip List: List of tips from the shift
    MD : Short for miles driven, single floating point number for miles driven in the shift
    SH: Short for store hours, single floating point number representing the hours worked in store for the shift
    RH: Short for rode hours, single floating point number representing the hours spent driving on the road for the shift
    Dates: Date for index of the data frame in format DD/MM/YY
    Return dfPizzaMetrics: Program returns a data frame 
    """
    
    dfPizzaMetrics = pd.DataFrame(data={'Tips': [TipList], 'MilesDriven': MD, 'StoreHours': SH, 'RoadHours': RH}, index=Dates)
    
    return dfPizzaMetrics

def GetShiftDD():
    """
    Purpose: used to get the data and then run the data to a data frame using DDTF() function
    """
    Tips = []
    tip = input("Enter tips values from the shift, enter done once finished: ")
    while tip != 'done':
        Tips.append(float(tip))
        tip = input("Enter next tip value: ")
    MD = float(input("Enter the miles driven from the shift: "))
    SH = float(input("Enter the store hours driven from the shift: "))
    RH = float(input("Enter the road hours driven from the shift: "))
    Date = input("Enter the date from the shift in format DD/MM/YY: ")
    DDTDF(Tips, MD, SH, RH, [Date])
    return DDTDF(Tips, MD, SH, RH, [Date])

def AddNewShift():
    """
    This function adds a new shift and writes the new shift data to the cumulative shifts data frame pickle file
    """
    OriginalDF = pd.read_pickle("./DeliveryDataFrame.pkl")
    UpdatedFrame = OriginalDF.append(GetShiftDD())
    pd.to_pickle(UpdatedFrame, "./DeliveryDataFrame.pkl")
    return UpdatedFrame

def GetTotals(PJDF):
    """
    PJDF: Papa John's Data Frame, which is my dataframe defined for the delivery data needed from the shift:::
          sample: pd.DataFrame(data={'Tips': [TipList], 'MilesDriven': MD, 'StoreHours': SH, 'RoadHours': RH}, index=Dates)"""
    ROR = 4.25 # rate on road per hour
    TFR = float(PJDF['RoadHours'].sum())*ROR # Total payout from road
    RIS = 9.50 # rate in store per hour
    TFS = float(PJDF['StoreHours'].sum())*RIS # Total payout for store
    TT = 0
    MD = float(PJDF['MilesDriven'].sum())*0.26 # reimbursement of 26 center per mile
    for shift in PJDF['Tips']:
        for tip in shift:
            TT+=float(tip)
    TotalDollarComp = (TFR + TFS + TT + MD) # Total Dollar Compensation from all shifts worked
    TotalHours = float(PJDF['RoadHours'].sum()) + float(PJDF['StoreHours'].sum())
    return {"Total Payout": "$"+str(TotalDollarComp),
            "Estimated Hourly Rate": "$%.2f per hour" % (TotalDollarComp/TotalHours)}
    
def GetTotalRecent(PJDF):
    """
    PJDF: Papa John's Data Frame, which is my dataframe defined for the delivery data needed from the shift:::
          sample: pd.DataFrame(data={'Tips': [TipList], 'MilesDriven': MD, 'StoreHours': SH, 'RoadHours': RH}, index=Dates)"""
    ROR = 4.25 # rate on road per hour
    TFR = float(PJDF['RoadHours'][-1])*ROR # Total payout from road
    RIS = 9.50 # rate in store per hour
    TFS = float(PJDF['StoreHours'][-1])*RIS # Total payout for store
    TT = 0
    MD = float(PJDF['MilesDriven'][-1])*0.26 # reimbursement of 26 center per mile
    for tip in PJDF['Tips'][-1]:
        TT+=float(tip)
    TotalDollarComp = (TFR + TFS + TT + MD) # Total Dollar Compensation from the most recent shift
    TotalHours = float(PJDF['RoadHours'][-1]) + float(PJDF['StoreHours'][-1])
    return {"Total Payout": "$"+str(TotalDollarComp),
            "Estimated Hourly Rate": "$%.2f per hour" % (TotalDollarComp/TotalHours)}
    
PJDF = pd.read_pickle("./DeliveryDataFrame.pkl")
PayRate, TotalPay = [], []
for tiplist, mile, sh, rh in zip(PJDF['Tips'], PJDF['MilesDriven'], PJDF['StoreHours'], PJDF['RoadHours']):
    tt = 0
    for tip in tiplist:
        tt += float(tip)
    totalmileage = float(mile)*0.26
    shtot = float(sh)*9.50
    rhtot = float(rh)*4.25
    totaldollars = tt+totalmileage+shtot+rhtot # total tip + mileage reimbursement, store hours, road hours
    dph = totaldollars / (float(sh)+float(rh)) # dollar per hour calculation
    PayRate.append(dph)
    TotalPay.append(float("%.2f" % totaldollars))

#PJDF['Totals'] = Totals 
#PJDF['MilesDriven'] = pd.to_numeric(PJDF['MilesDriven'], downcast="float")
pd.to_pickle(PJDF, "./DeliveryDataFrame.pkl")

        
        

 


    
    