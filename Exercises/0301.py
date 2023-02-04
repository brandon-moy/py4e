# Rewrite your pay computation to give the employees 1.5 times the hourly rate
# for hours above 40 hours

# Create input that stores Hours
# Create input that stores Rate
# Convert Hours and Rate to Integers
# check if hours > 40
# if yes then create a new variable that is hours - 40 and set hours = 40
# Multiply Integers together for gross pay
# Print Gross pay back to user

hrs = input('Enter Hours: ');
rate = input('Enter Rate: ');
ihrs = float(hrs)
irate = float(rate)
if ihrs > 40:
  ot = ihrs - 40
  ihrs = 40
  ot = ot * irate * 1.5
  pay = ihrs * irate + ot
else:
  pay = float(hrs) * float(rate);
print('Pay:', pay);
