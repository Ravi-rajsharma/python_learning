# String Slicing :- Use the [start:stop:step] syntax to extract parts of a string:

# • Start: The beginning index (inclusive, defaults to 0).

# • Stop: The ending index (exclusive, defaults to the end of the string).

# • Step: The interval or direction (defaults to 1). A negative step like [::-1] reverses the string.

# • Negative Indexing: Use negative numbers (-1 for the last character) to count backward from the end.

str = "PC Computer"
print ("input string = ",str,"\n")

print ("After String Slicing/Piece")

print("first string = ",str[0])
#print("first string index = ",str[0:1:8]) #invalid statement

print("third to sixth string = ",str[2:6])
print("third to all string = ",str[2:])

print("\nexcept after 4th including 5th string = ",str[:5])
print("last 2nd string = ",str[-2])

print("print 2nd 6th and 1st string = ",str[2:6:1])
#print("print 2nd 1st and 6th string = ",str[2:1:6]) #invalid statement

print("\nprint 2 times = ",str*2)
#print("print 2 times with space = ", str *2)

print("Print concatenated string = ",str+" rajeshwar")
print("except last two string = ",str[:-2])

print("\nwrite opposite = ",str[::-1])
print("write opposite except 2nd (index) word = ",str[::-2])
print("write opposite except 3nd (index) word = ",str[::-3])