# String Formatting

name = "Ravi"
age = 22

print ("three main ways to format strings :- \n")
# 1. F-Strings (Python 3.6+) - Recommended

print(f"Hello, {name}. Your age is ${age:.1f}") 
# Output: Hello, Alice. age is $45.68

# 2. str.format() method (Older but widely used)
print("Hello, {}. age is ${:.2f}".format(name, age))

# 3. % Operator (Legacy / C-style)
print("Hello, %s. Your age is $%.3f" % (name, age))

# .format() Method

# Positional arguments
print("The {} is a {}.".format("sky", "blue"))  # Output: The sky is a blue.

# Indexed arguments
print("{1} is older than {0}.".format("Bob", "Charlie"))    # Output: Charlie is older than Bob.

# Keyword arguments
print("{item} costs ${age:.2f}".format(item="Coffee", age=4.5)) # Output: Coffee costs $4.50

# Legacy (%) Formatting (C-style) 
print("Hello, %s. Your score is %d." % ("Ravi", 95))    # Output: Hello, Ravi. Your score is 95.