# Numeric Expressions
xx = 2;
xx = xx + 2;
print(xx);
# 4

yy = 440 * 12;
print(yy);
# 5280

zz = yy / 1000;
print(zz);
# 5.28

jj = 23;
kk = jj % 5;
print(kk);
# 3

print(4 ** 3);
# 64

# Operator Precedence - Parenthesis, Power, Multiplication, Addition, Left to Right
x = 1 + 2 ** 3 / 4 * 5;
# 1 + [2 ** 3] / 4 * 5
# 1 + [8 / 4] * 5
# 1 + [2 * 5]
# 1 + 10
print(x);
# 11

# + is arithmetic and concatenation
ddd = 1 + 4
print(ddd);
# 5

eee = 'hello ' + 'there';
print(eee);
# hello there

#Type matters in Python, cannot concatenate string and integer
print(type(eee));
# <class 'str'>
print(type('hello'));
# <class 'str'>
print(type(1));
# <class 'int'>

# numbers with decimals are 'float' point numbers
# Integer division produces a floating point result (Python3)
# Changing str int to int needs to have integers else throws error
# nav = 'hello'
# inav = int(nav);
# ValueError: invalid literal for int() with base 10: 'hello'

# User Input
# Python can pause and read data from the user using input() -> returns a string
nam = input('Who are you? '); # pauses after who are you until input it received
print('Welcome', nam); # after input is received, prints this and input was variable

# Converting User Input
# Read a number input from a user ... but input returns a string!
# Convert the string to an integer
# Calculate the difference
# Return the calculated difference
inp = input('Europe floor? '); # returns string
usf = int(inp) + 1; # convert string to int to run arithmetic calculation
print('US Floor', usf); # returns the calculated number
