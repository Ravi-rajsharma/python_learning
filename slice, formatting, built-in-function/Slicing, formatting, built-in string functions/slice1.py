# String Slicing

text = "Python Programming"

# Basic slicing (extracts indices 0 to 5)
print(text[0:6])      

# Omitting start or stop takes it from/to the boundary
print(text[:6])        
print(text[7:])        

# Using step to skip characters
print(text[::2])       # it print Every second character

# Negative indexing (counts backwards from the end)
print(text[-11:-7])    

# Reversing a string with a negative step
print(text[::-1])     

# Copying the entire string
print(text[:]) 