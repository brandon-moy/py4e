# Ch 5

# Standard while loop
n = 5
while n > 0 :
    print(n)
    n = n - 1
print('Blastoff!')
print(n)

# Breaking out of a loop
# break statement ends the current loop and jumps to the statement
# immediately following the loop

while True :
    line = input('> ')
    if line == 'done' :
        break
    print(line)
print('Done!')

# Finishing a loop with continue
# The continue statement ends the current iteration and jumps to the top of the
#loop and starts the next iteration

while True:
    line = input('> ')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')

# Definite Loops
# List of items in a file - a finite set of items
# loop runs for each item in  the set

for i in [5, 4, 3, 2, 1] :
    print(i)
print('Blastoff!')

superfriends = ['Brandon', 'Jake', 'Jianni']
for friend in superfriends :
    print('Super Friends:', friend)
print('UNITE')

# Loop Idioms

# Find largest value

largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)

print('After', largest_so_far)

# Change largest to find smallest?

smallest = None
print('Before', smallest)
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None
        smallest = value
    if value < smallest :
        smallest = value
    print(smallest, value)

print('After', smallest)

# Counting in a Loop

zork = 0
print(' Before', zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + 1
    print(zork, thing)
print('After', zork)
