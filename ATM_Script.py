import sys

### Starting Account balance assigned to variable 
account_balance = float(500.25)


#First Function - simply prints balance
def print_balance ():
  print("Your current balance:\n $" + str(account_balance))

#Deposit function - when called accepts user input as a float and stores it in account balance
def deposit ():
  account_balance = float(500.25)
  deposit_amount = input("How much would you like to deposit today?\n")
  account_balance += float(deposit_amount)
  print("Deposit was $" + str('%.2f' % float(deposit_amount)) + ", current balance is $" + str(account_balance))

#Withdrawl function - accepts withdrawal amount as input from user unless withdrawl amount is greater than account balance in which case the customer is notified
def withdrawal ():
  account_balance = float(500.25) ### Floats being used to print a familiar currency format (two places after decimal).
  withdrawal_amount = input("How much would you like to withdraw today?\n")
  if float(withdrawal_amount) > account_balance:
    print("$" + str('%.2f' % float(withdrawal_amount)) + " is greater than your account balance of $" + str('%.2f' % float(account_balance)))
  else:
    account_balance -= float(withdrawal_amount) #If withdrawl amount doesn't exceed balance it is subtracted from account balance and printed back out to the user as a brief summary
    print("Withdrawal amount was $" + str('%.2f' % float(withdrawal_amount)) + ", current balance is $" + str('%.2f' % float(account_balance)))
## Option to quit using program - no balance, no withdrawl and no deposit.
def quit():
    print("Thank you for banking with us.")
  


## Based off user input (Deposit, Withdrawl, Balance, or Quit) four different functions are called, with different code blocks performing different instructions for each. 
userchoice = input("What would you like to do?\n")

if (userchoice == 'D'):
    deposit()
elif (userchoice == 'W'):
  withdrawal()
elif (userchoice == 'B'):
  print_balance()
elif (userchoice == 'Q'):
  quit()
  

