text = "the best things in life are free"
print ("String = ",text, "\n")

print ("expensive is absent in string :- ", "expensive" not in text) # not in keyword used for check
print ("free is present in string", "free" in text, "\n") # in keyword used for check

if "things" in text :
    print ("no, things is present in things")

if "expensive" not in text :
    print ("yes, expensive is not present in text \n")

#important string function in python
print ("in capital letter = ",text.upper())
print ("in small letter = ",text.lower())

print ("1st capital letter = ",text.capitalize())
print ("each 1st word capital letter = ",text.title(), "\n")

name = " ravi "
print ("actual name = ",name, "\n")

print (name.strip(),",after remove leading and trailing whitespace")
print ("after changing substring with another = ",name.replace("v","n"))

print ("after changing substring with another = ",name.replace("vi","jo"))
print ("after changing substring with another = ",name.replace("v""i","j""a"), "\n")

print ("find t index in python = ","python".find("t"))
print ("count occurrences/repeated number of e in string = ",text.count("e"))

#print ("count occurrences/repeated number of e in string = ",text.count("text"))
print ("split string into list = ",text.split(","), "\n")

print ("join iterable element into a string = ","+".join(["a""b""c"]))
print ("return true if alphabet = ","python".isalpha(), "\n") #check only if word is double code 

# language = "python"
# print ("check if string start with specified value = ", language.startwith("py"))  #not proper work
# print ("check if string end with specified value = ", language.endwith("on"))    #not proper work  

print ("return true if digit = ","15973".isdigit()) #check only if digit is in double code 
print ("return length of string = ", len("textnabx"))   