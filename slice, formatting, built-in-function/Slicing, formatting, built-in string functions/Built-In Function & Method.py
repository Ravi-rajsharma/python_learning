# Built-In String Functions & Methods

# Case Conversion

sample = "hello WORLD"
print("sample word for case conversion :- ",sample, "\n")

print("convert in uppercase :-", sample.upper())       # Converts all characters to uppercase)
print("convert in lowercase :-", sample.lower())       # Converts all characters to lowercase)

print("capitalize first character :-", sample.capitalize()) # Capitalizes the first character only)
print("title case :-", sample.title(),"\n")       # Capitalizes the first letter of each word)

# Searching & Validating

phrase = "Python 3.12"
print ("phrase :- ",phrase)

print("check phrase data start with py :-",phrase.startswith("Py")) # True (Checks prefix)
print("check phrase data end with 12 :-",phrase.endswith("12"),"\n")   # True (Checks suffix)

print("find 1st index of element th :-", phrase.find("th"))  
# return 2 as index (Returns lowest index of substring, or -1 if not found)

print("check 3.12 is in phrase :-", "3.12" in phrase, "\n") 
# True (Evaluates membership using the 'in' operator)

# Type checking methods

print("check 12345 is digit or not :-", "12345".isdigit())       
# True (Check and return if characters are digits)

print("check Alpha is alphabetic or not :-", "Alpha".isalpha(),"\n")      
# True (Check and return if characters are alphabetic)

# Text Modification & Whitespace Cleanup
words_list = ["Python", "is", "fun"]

joined_string = " - ".join(words_list) # Joins an iterable of strings using a separator
print("print word list asjoined string :-", joined_string,"\n") # Output: Python - is - fun

spaced_text = "   clean me   "
print("spaced text :- ",spaced_text)
print("length of spaced text :- ",len(spaced_text),"\n")

# Stripping structural spacing

print("stripped spaced_text :-", spaced_text.strip())     
print("length of stripped spaced_text :-", len(spaced_text.strip()),"\n")     
# output :- "clean me" (Removes leading and trailing whitespace)

print("left stripped spaced_text :-", spaced_text.lstrip())    
print("length of left stripped spaced_text :-", len(spaced_text.lstrip()),"\n")    
# output :- "clean me   " (Removes leading whitespace)

print("right stripped spaced_text :-", spaced_text.rstrip())    
print("length of right stripped spaced_text :-", len(spaced_text.rstrip()),"\n")    
# output :- "   clean me" (Removes trailing whitespace)

# Replacing values
print("print replaced text :-", "I like Java".replace("Java", "Python"),"\n") # Output: I like Python

# Splitting and Joining
csv_line = "apple,banana,cherry"
print("csv line :- ",csv_line)

split_items = csv_line.split(",") # Splits string into a list based on delimiter
print("split csv_line :-", split_items)  # Output: ['apple', 'banana', 'cherry']