import csv
import sys
import pandas as pd
import numpy as np  
from matplotlib import pyplot as plt 
import tkinter
import PySimpleGUI as sg
########################
#GUI
########################
varInput = ""
sg.theme('DarkAmber')   # Add a touch of color
print('loading')
layout = [ 
            [sg.Text('Finances login')],
            [sg.Text('Enter an expense/gain to append'), sg.InputText()],
            [sg.Button('Graph Expenses'), sg.Button('Add Expense'), sg.Button('Add Gain'), sg.Button('Exit'), sg.Button('Submit')]
         ]
layoutgained = [
            [sg.Text('Finances Gained')],
            [sg.Text('Enter the cash gained'), sg.In(size=(8,1), key='cashgained')],
            [sg.Button('Graph Expenses'), sg.Button('Add Expense'), sg.Button('Add Gain'), sg.Button('Submit Gain'), sg.Button('Exit')]
]
layoutexpense = [
            [sg.Text('Finances')],
            [sg.Text('Enter the cash spent'), sg.In(size=(8,1), key='cashout')],
            [sg.Text('Enter the Finance type'), sg.In(size=(8,1), key='typein')],
            [sg.Button('Graph Expenses'), sg.Button('Add Expense'), sg.Button('Add Gain'), sg.Button('Exit'), sg.Button('Submit loss')]
]
#Graph = [[sg.Text('Plot test', font='Any 18')],
 #         [sg.Canvas(size=(figure_w, figure_h), key='-CANVAS-')],
  #        [sg.OK(pad=((figure_w / 2, 0), 3), size=(4, 2))]]



#Cash Gained Window########################
#Cash Lost Window############################

#Graph Window################################33

#Main Window
# STEP3 - the event loop

#############################################
#############################################
##SAVE VARS##################################
###################
#Functions
###################
def func(pct, allvalues): 
    absolute = int(pct / 100.*np.sum(allvalues)) 
    return "{:.1f}%\n({:d} g)".format(pct, absolute)
def save_csv():
  df = pd.DataFrame(varInput, columns=['Balance', 'Entertainment', 'Food', 'Gifts', 'Misc', 'Personal', 'Savings', 'Subscriptions', 'Transportation'])
  df.to_csv(r'Tracking.csv', mode='a', index = False, header=False)

def save_allin(a):
  varInput = {'Balance': [a]}
  print(varInput)
  save_csv()
  print("b")

def save_allcost(a, b):
    ###################
    #Entertainment
    ###################
  if typeIn == "Entertainment":
    varInput = {[a]: [b]}
    save_csv()
    ###################
    #Food
    ###################
  elif typeIn == "Food":
    varInput = {'Food': [costIn]}

    save_csv()

    ###################
    #Gifts
    ###################
  elif typeIn == "Gifts":
    varInput = {'Gifts': [costIn]}
    save_csv()
    ###################
    #Misc
    ###################
  elif typeIn == "Misc":
    varInput = {'Misc': [costIn]}
    save_csv()
    ###################
    #Personal
    ###################
  elif typeIn == "Personal":
    varInput = {'Personal': [costIn]}
    save_csv()
    ###################
    #Savings
    ###################
  elif typeIn == "Savings":
    varInput = {'Savings': [costIn]}
    save_csv()
   ###################
    #Subscriptions
    ###################
  elif typeIn == "Subscriptions":
    varInput = {'Subscriptions': [costIn]}
    save_csv()
    ###################
    #Transportation
    ###################
  elif typeIn == "Transportation":
    varInput = {'Transportation': [costIn]}
    save_csv()
#############################################




#PICHART
def graphchart():
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
  #
  totalRemaining = totalBalance - totalSpent
  #####################
  #PieChart
  #####################
  # Creates set dataset
 #spendingChart = ['Entertainment', 'Food', 'Gifts', 
 #       'Misc', 'Personal', 'Savings', 'Subscriptions', 'Transportation'] 
  #Imports the data into the data set
 #data = [entertainmentTotal, foodTotal, giftsTotal, miscTotal, personalTotal, savingsTotal, subscriptionTotal, transportationTotal] 
 #print(data)
  #Set color
 #colors = ( "purple", "maroon", "brown", 
 #          "grey", "indigo", "beige", "lime", "red") 
 # Sets properties of wedges
 #wp = { 'linewidth' : 2, 'edgecolor' : "black" } 

 #explode = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]

 # Creates autocpt arguments 
 #Creating Pie Chart 
 #fig, ax = plt.subplots(figsize =(10, 7)) 
 #wedges, texts, autotexts = ax.pie(data,  
 #                                  autopct = lambda pct: func(pct, data), 
 #                                  labels = spendingChart, 
 #                                  colors = colors, 
 #                                  startangle = 90, 
 #                                  wedgeprops = wp, 
                                  #textprops = dict(color ="black")) 
 #Adds legend to chart
 #ax.legend(wedges, spendingChart, 
 #          title ="Budgeting", 
 #          loc ="center left", 
 #          bbox_to_anchor =(1, 0, 0.5, 1)) 
  
 #plt.setp(autotexts, size = 8, weight ="bold") 
 #ax.set_title("Spending Percentages") 
 #shows chart 
 #plt.show() 
 ##########################3
 #total_percentage_chart = ['Spent', 'Remaining']
 #percentData = [totalBalance, totalSpent]
 #def absolute_value(val):
 #    a  = np.round(val/100.*(totalBalance + totalSpent), 0)
 #    return a
 #fig1, ax1 = plt.subplots()
 #ax1.pie(percentData, labels=total_percentage_chart, autopct=absolute_value,
 #        shadow=True, startangle=90)
 #ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

 # plt.show()
window = sg.Window('Main', layout, grab_anywhere=True)
print("Window Started")
while True:
    event, values = window.read()   # Read the event that happened and the values dictionary
    print(event, values)
    if event in (None, 'Exit'):     # If user closeddow with X or if user clicked "Exit" button then exit
        break
    if event == 'Graph':
      print("Graphing Expense")
      fig_photo = draw_figure(window['-CANVAS-'].TKCanvas, fig)

    if event == 'Add Expense':
      window = sg.Window('CashSpentpage', layoutexpense, grab_anywhere=True)
    if event == 'Add Gain':
      window = sg.Window('CashGainedPage', layoutgained, grab_anywhere=True)
    if event == 'Submit Gain':
      cashIn = values['cashgained']
      print(cashIn)
      save_allin(cashIn)
    if event == 'Submit Cost':
      #costIn == {dollarstring}
      costIn = float(values['cashout'])
      typeIn = values['typein']
      save_allcost(typeIn, costIn)
    else:
        print("Error")
window.close()