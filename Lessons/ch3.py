# Conditional Execution

x = 5 # Assign an int to a variable
if x < 10: # IF statement - no parenthesis and uses : (colon) to go next
  print('Smaller'); # condition code blocl is indented below the IF statement
  print('Than 10');
if x > 20: print('Bigger'); # You can one line if only running 1 line of conditional code

print('Finis');

# Pyathon Comparison Operators
# < Less Than
# <= Less than or Equal to
# == Equal to
# >= Greater than or Equal to
# > Greater than
# != Not equal

# elif -> else if
if x < 2: # checks if this if no goes to ln 22
    print('small')
elif x < 10: # if not < 2 then check is < 10
    print('Medium')
else: # if not < 10 then runs line 25
    print('LARGE')
print('All done')

# try / except
# surround a dangerous section of code with try and except
# if the code in try works - the except is skipped
# if the code in try fails - it jumps to the except section

astr = 'Hello Bob'
istr = int(astr); # This fails and throws an error because you cannot convert
# letter characters to an integer -- use a try / except to get around this and
# allow the rest of the code to run
print('First', istr);
astr = '123'
istr = int(astr);
print('Second', istr)

astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1

print('First', istr);
# returns 'First -1'

astr = '123'
try:
    iatr = int(astr);
except:
    istr = -1;

print('Second', iatr);
# returns 'Second 123'

rawstr = input('Enter a number: ')
try:
    ival = int(rawstr);
except:
    ival = -1

if ival > 0 :
    print('Nice work')
else :
    print('Not a number')
