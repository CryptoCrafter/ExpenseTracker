import pandas as pd
###################
#Cash additions
###################
print("Please enter any cash gained.")
cashIn = input()
varInput = {'Balance': [cashIn]}
df = pd.DataFrame(varInput, columns=['Balance'])
df.to_csv(r'CashIn.csv', mode='a', header=False)



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
    varInput = {'Cost': [costIn]}

    df = pd.DataFrame(varInput, columns=['Cost'])

    df.to_csv(r'Entertainment.csv', mode='a', header=False)
    ###################
    #Food
    ###################
  elif typeIn == "Food":
    varInput = {'Cost': [costIn]}

    df = pd.DataFrame(varInput, columns=['Cost'])

    df.to_csv(r'Food.csv', mode='a', header=False)

    ###################
    #Gifts
    ###################
  elif typeIn == "Gifts":
    varInput = {'Cost': [costIn]}

    df = pd.DataFrame(varInput, columns=['Cost'])

    df.to_csv(r'Gifts.csv', mode='a', header=False)

    ###################
    #Misc
    ###################
  elif typeIn == "Misc":
    varInput = {'Cost': [costIn]}

    df = pd.DataFrame(varInput, columns=['Cost'])

    df.to_csv(r'Misc.csv', mode='a', header=False)


    ###################
    #Personal
    ###################
  elif typeIn == "Personal":
    varInput = {'Cost': [costIn]}

    df = pd.DataFrame(varInput, columns=['Cost'])

    df.to_csv(r'Personal.csv', mode='a', header=False)

    ###################
    #Savings
    ###################
  elif typeIn == "Savings":
    varInput = {'Cost': [costIn]}

    df = pd.DataFrame(varInput, columns=['Cost'])

    df.to_csv(r'Savings.csv', mode='a', header=False)

   ###################
    #Subscriptions
    ###################
  elif typeIn == "Subscriptions":
    varInput = {'Cost': [costIn]}

    df = pd.DataFrame(varInput, columns=['Cost'])

    df.to_csv(r'Subscriptions.csv', mode='a', header=False)

    ###################
    #Transportation
    ###################
  elif typeIn == "Transportation":
    varInput = {'Cost': [costIn]}

    df = pd.DataFrame(varInput, columns=['Cost'])

    df.to_csv(r'Transportation.csv', mode='a', header=False)