# CH 4 Functions
# Stored (and reused) Steps
# def is the DEFining keyword for functions

x = 5;
print('Hello')

def print_lyrics(): # Definted function
    print("I'm a lumberjack, and I'm okay.") # runs in function code block
    print('I sleep all night and I work all day.') # additional line in code block

print('Yo')
print_lyrics()
x = x + 2
print(x)


def greet(lang): # Function using parameter
  if lang == 'es':
      print('Hola')
  elif lang == 'fr':
      print('Bonjour')
  else:
      print('Hello')

greet('en') # Calling function with argument
greet('es')
greet('fr')

# return returns a value from the function and ends the function

def greet2(lang): # Function using parameter
  if lang == 'es':
      return 'Hola'
  elif lang == 'fr':
      return 'Bonjour'
  else:
      return 'Hello'

print(greet2('en'), 'Brandon')
print(greet2('es'), 'Brandon')
print(greet2('fr'), 'Brandon')
