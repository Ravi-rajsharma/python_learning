# Mutable Objects in Action
my_list = [1, 2, 3]

print("Mutable Objects in Action :-\n")

print("my_list :- ", my_list)
print("id of my_list :- ", id(my_list), "\n")  # e.g., ID changes every execution times

my_list.append(4)
print("my_list after append :- ", my_list)      # Output: [1, 2, 3, 4]
print("id of my_list after append :- ", id(my_list), "\n")  # Same ID: 140234891234

# Immutable Objects in Action
text = "Hello"

print("Immutable Objects in Action :- \n")

print("text :- ", text)
print("id of text :- ", id(text), "\n")     # e.g.,ID: 140234895555 changes every execution times

text += " World"    # Creates a new string object
print("new text :- ", text)         # Output: Hello World
print("new id :- ", id(text), "\n")     # New ID: 140234899999 changes every execution times

my_tuple = (10, 20, 30)

print("my_tuple :- ", my_tuple)
# my_tuple[0] = 99    # Raises TypeError: 'tuple' object does not support item assignment