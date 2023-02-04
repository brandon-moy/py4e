# Write a program to prompt the user for hours and rate per hour to computer gross pay
# Enter Hours: XX
# Enter Rate: XX
# Pay: XX

# Create input that stores Hours
# Create input that stores Rate
# Convert Hours and Rate to Integers
# Multiply Integers together for gross pay
# Print Gross pay back to user

hrs = input('Enter Hours: ');
rate = input('Enter Rate: ');
pay = float(hrs) * float(rate);
print('Pay:', pay);
