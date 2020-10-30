import pandas as pd
###################
#Functions
###################
def save_csv():
  df = pd.DataFrame(varInput, columns=['Balance', 'Entertainment', 'Food', 'Gifts', 'Misc', 'Personal', 'Savings', 'Subscriptions', 'Transportation'])
  df.to_csv(r'Tracking.csv', mode='a', index = False, header=False)
###################
#Cash additions
###################
print("Please enter any cash gained.")
cashIn = input()
varInput = {'Balance': [cashIn]}
save_csv()



###################
print("------------------------------------------")
print("Valid expense types are Food, Transportation, Savings, Subscriptions, Personal, Gifts, Entertainment, and Misc")
print("------------------------------------------")

while 1 == 1:

  print("Input Expense Type")
  typeIn = input()
  print("Input Expense Cost")
  costIn = input()
  if typeIn == "":
    exec(open('main.py').read())
    ###################
    #Entertainment
    ###################
  elif typeIn == "Entertainment":
    varInput = {'Entertainment': [costIn]}
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