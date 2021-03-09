import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
sb.set(rc={'figure.figsize':(11.7,8.27)})
pd.set_option('display.max_column',None)
pd.set_option('display.max_rows',None)


#constructor
'''def __init__(self, csvData):
    self.csvData = csvData'''

def readData():
    #pre2k=pd.read_csv('approval-date-1990-1999.csv')
    #fileName = input("Enter your file name: ")
    fileName = 'approval-date-2000-feb-2012.csv'
    csvData = pd.read_csv(fileName)
    return csvData

# display a bar graph of the flat's resale price against the town
def barPriceVsTown(csvData):
    plot = sb.barplot(x='resale_price', y='town', data = csvData)
    fig = plot.get_figure()
    fig.savefig('town.png')                     # save plot to PNG for use in HTML
    
# display a bar graph of the flat's resale price against the flat type
def barPriceVsFlatType(csvData):
    plot = sb.barplot(x='resale_price', y='flat_type', data=csvData, order=["1 ROOM", "2 ROOM", "3 ROOM", "4 ROOM", "5 ROOM", "EXECUTIVE", "MULTI-GENERATION"])
    fig = plot.get_figure()
    fig.savefig('flat_type.png')                # save plot to PNG for use in HTML

# display a point plot of the flat's resale price against the year the resale occurred
def pointPriceVsYear(csvData):
    csvData['year']=csvData['month'].str[:4]
    plot = sb.pointplot(x='year', y='resale_price', data=csvData)
    fig = plot.get_figure()
    fig.savefig('year.png')                     # save plot to PNG for use in HTML
    
'''
#for debugging
def main():
    print("Hello World!")
    yes = readData()
    barPriceVsTown(yes)

if __name__ == "__main__":
    main()
'''
