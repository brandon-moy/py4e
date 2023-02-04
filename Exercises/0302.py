# Rewrite the pay program using try and except so that the program handles
# non-numberic input gracefully by printing a message and exiting the program
# Example:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input

hrs = input('Enter Hours: ');
rate = input('Enter Rate: ');
try:
  ihrs = float(hrs)
  irate = float(rate)
except:
  print('Error, please enter numeric input')
  quit()
if ihrs > 40:
  ot = ihrs - 40
  ihrs = 40
  ot = ot * irate * 1.5
  pay = ihrs * irate + ot
else:
  pay = float(hrs) * float(rate);
print('Pay:', pay);
