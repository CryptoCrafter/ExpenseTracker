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
  ###########
  #Entertainment
  df = pd.read_csv('Entertainment.csv')
  entertainmentTotal = df['Cost'].sum()
  df = 0
  ###################
  #Food
  ###################
  df = pd.read_csv('Food.csv')
  foodTotal = df['Cost'].sum()
  df = 0
  ######################
  #Gifts
  ######################
  df = pd.read_csv('Gifts.csv')
  giftsTotal= df['Cost'].sum()
  df = 0
  ######################
  #Misc
  ######################
  df = pd.read_csv('Misc.csv')
  miscTotal = df['Cost'].sum()
  df = 0
  ######################
  #Personal
  ######################
  df = pd.read_csv('Personal.csv')
  personalTotal = df['Cost'].sum()
  df = 0
  ######################
  #Savings
  ######################
  df = pd.read_csv('Savings.csv')
  savingsTotal = df['Cost'].sum()
  df = 0
  ######################
  #Subscriptions
  ######################
  df = pd.read_csv('Subscriptions.csv')
  subscriptionTotal = df['Cost'].sum()
  df = 0
  ######################
  #Transportation
  ######################
  df = pd.read_csv('Transportation.csv')
  transportationTotal = df['Cost'].sum()
  df = 0
  ######################
  #TotalSpent
  ######################
  totalSpent = entertainmentTotal + foodTotal + giftsTotal + miscTotal + personalTotal + savingsTotal + subscriptionTotal + transportationTotal
  ######################
  #Total Added
  ######################
  df = pd.read_csv('CashIn.csv')
  totalAdded = df['Balance'].sum()
  df = 0
  ######################
  #Total Remaining
  ######################
  totalRemaining = totalAdded - totalSpent


  print(foodTotal)
  print(transportationTotal)
  print(totalSpent)
  # Creating dataset 
spendingChart = ['Entertainment', 'Food', 'Gifts', 
        'Misc', 'Personal', 'Savings', 'Subscriptions', 'Transportation','Remaining money'] 
  
data = [entertainmentTotal, foodTotal, giftsTotal, miscTotal, personalTotal, savingsTotal, subscriptionTotal, transportationTotal, totalRemaining] 

colors = ( "purple", "maroon", "brown", 
          "grey", "indigo", "beige", "lime", "red", "green") 
# Wedge properties 
wp = { 'linewidth' : 3, 'edgecolor' : "black" } 

# Creating autocpt arguments 
def func(pct, allvalues): 
    absolute = int(pct / 100.*np.sum(allvalues)) 
    return "{:.1f}%\n({:d} g)".format(pct, absolute)
# Creating plot 
fig, ax = plt.subplots(figsize =(10, 7)) 
wedges, texts, autotexts = ax.pie(data,  
                                  autopct = lambda pct: func(pct, data), 
                                  labels = spendingChart, 
                                  shadow = True, 
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
ax.set_title("Customizing pie chart") 
# show plot 
plt.show() 
  

  
  




#transportationTotal
#subscriptionsTotal
#entertainmentTotal
#giftsTotal
#savingsTotal
#personalTotal
#miscellaneousTotaln
