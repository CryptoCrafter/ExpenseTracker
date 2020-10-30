import csv
import sys
import pandas as pd
import numpy as np  
from matplotlib import pyplot as plt 
print("Do you need to add expenses/money? Y/n")
runInput = input()
if (runInput == 'Y'):
  #Runs dailyinputs.py
  exec(open('DailyInputs.py').read())
else:

  ###################################################
  totalSpent = 0
  ######################
  #Totals
  ######################
  df = pd.read_csv('Tracking.csv')
  totalBalance = df['Balance'].sum()
  entertainmentTotal = df['Entertainment'].sum()
  foodTotal = df['Food'].sum()
  giftsTotal= df['Gifts'].sum()
  miscTotal = df['Misc'].sum()
  personalTotal = df['Personal'].sum()
  savingsTotal = df['Savings'].sum()
  subscriptionTotal = df['Subscriptions'].sum()
  transportationTotal = df['Transportation'].sum()
  #Non CSV reading totals
  totalSpent = entertainmentTotal + foodTotal + giftsTotal + miscTotal + personalTotal + savingsTotal + subscriptionTotal + transportationTotal

  totalRemaining = totalBalance - totalSpent
  # Creating dataset 
spendingChart = ['Entertainment', 'Food', 'Gifts', 
        'Misc', 'Personal', 'Savings', 'Subscriptions', 'Transportation'] 
  
data = [entertainmentTotal, foodTotal, giftsTotal, miscTotal, personalTotal, savingsTotal, subscriptionTotal, transportationTotal] 

colors = ( "purple", "maroon", "brown", 
          "grey", "indigo", "beige", "lime", "red") 
# Wedge properties 
wp = { 'linewidth' : 2, 'edgecolor' : "black" } 

# Creating autocpt arguments 
def func(pct, allvalues): 
    absolute = int(pct / 100.*np.sum(allvalues)) 
    return "{:.1f}%\n({:d} g)".format(pct, absolute)
# Creating plot 
fig, ax = plt.subplots(figsize =(10, 7)) 
wedges, texts, autotexts = ax.pie(data,  
                                  autopct = lambda pct: func(pct, data), 
                                  labels = spendingChart, 
                                  colors = colors, 
                                  startangle = 90, 
                                  wedgeprops = wp, 
                                  textprops = dict(color ="black")) 
# Adding legend 
ax.legend(wedges, spendingChart, 
          title ="Budgeting", 
          loc ="center left", 
          bbox_to_anchor =(1, 0, 0.5, 1)) 
  
plt.setp(autotexts, size = 8, weight ="bold") 
ax.set_title("Spending Percentages") 
# show plot 
plt.show() 