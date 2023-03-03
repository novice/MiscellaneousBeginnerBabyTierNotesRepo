# this is a comment!!
money_girl = "Nami"
# above is variable assign, variable cannot start with number and no symbols except _
# variable (assign) value
# example value is string
print("Who loves money the most? " + money_girl + "!")
# > Who loves money the most? Nami!
# You can use either single or double quotes. ' or ""

# Two common python errors are NameError and SyntaxError
# SyntaxError problem with Syntax, such as unclosed string
# NameError can't find variable by name

# An (int)eger is a whole number without decimal point, it can be negative.
# A float is a decimal number.
a_int = 2
a_float = 2.1
print (an_int + 3) # the 3 is known as a literal and not a variable with 3 assigned
# > Output: 5 (This is the sum of the two numbers)
# floats can behave in weird ways from how computers store them
# more info (may check later?) https://docs.python.org/3/tutorial/floatingpoint.html

# "Compute" in computer comes from their history of solving math questions
# Python performs the arithmetic operations with usual +,-,*,/
# New python when dividing converts ints to floats, but 2.7 rounds to nearest int
# attempting to divide by 0 throws unique error ZeroDivisionError
# python follows order of operations when computing math
print(2 + 3 * 4)
# Output: 14 (3*4=12, 12+2=14)

# variables assigned numeric values can be treated as numbers in math operations
# you can do operations with them and literals (as seen above)
# performing arithmetic doesn't change the variable, you can only update a variable using =
box_width = 4
box_height = 6
print(box_width * box_width)
# Output: 24
box_width = 4
# redo print, Output: 16
print(box_width + 4)
# Output: 8, box_width still 4

# you can do exponets (to the power of) in python with **
print(4 ** 3)
# Output: 64 (4 * 4 * 4)
# and you're capable of doing fractional exponents
print(8 ** 0.5)
# Output: 4

# Modulo is a similar operator to division; it's indicated by % and gives the remainder of a division calculation.
# if the number is divisible, then the result will be 0
# modulo by 2 returns 0 for even, 1 for odd
print(37 % 5)
# Output: 2 (five goes into 37 seven times but a remainder of 2)

# + symbol can also be used for strong concatenation (combining the two strings)
print("Hello"+"World!")
# Outputs: HelloWorld! (doesn't add a space!)
# you can convert non string variables with str() in order to concat
print("Only "+str(4)+"?")
# Outputs: Only 4? (would error without str conversion)
# you don't need to convert when printing though; you can pass it as another argument to print using commas.
print("Only",4,"?")
# Outputs: Only 4 ? (but in 2.7, seems to do ("Only",4,"?"))

# Python offers a shorthand for updating variables, for example: +=
cats = 3
print(cats) # > 3
cats += 2
print(cats) # > 5
# plus-equals operator can also be used for string concatenation
msg = "Hello "
msg += "World!"
print(msg)
# Output: Hello World!

# using three quote-marks, you can do multi-line strings
"""Hello
World!"""
# (without assigning to a variable, it's treated as a comment)
# this can be useful for strings containing quote-marks

# useful(?) resources
# https://www.codecademy.com/resources/docs/python?page_ref=catalog
# https://www.codecademy.com/workspaces/new



# WHY DO I HAVE TO WRITE MY INITIALS???
# https://www.codecademy.com/courses/learn-python-3/projects/python-block-letters

# LEFT OFF HERE
# https://www.codecademy.com/courses/learn-python-3/projects/python-furniture-store
