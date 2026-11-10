# string is a data_type that stores a sequence of charactors

str = "ravi raj"
print ("str = ",str, "\n")

# basic operator length and comparison, concatenation of string

# Python includes built-in functions like len(), min(), and max(), 

str1 = "hello"
str2 = "world"

print("str1 &str2 = ",str1,str2)
print("length of str1 &str2 = ",len(str1),len(str2), "\n")

print("\nconcatenation1 of str1 and str2 = ",str1+str2)
print("concatenation1 length = ",len(str1+str2), "\m")

print("\nconcatenation2 of str1 and str2 = ",str1+ " " +str2)
print("concatenation2 length = ",len(str1+ " " +str2), "\n")

#indexing (start with 0 in list :-[]) of string

print ("1st index of string = ",str[0])
print ("2nd index of string = ",str[1], "\n")

#slilcing used to access parts of a string :- 

#str[start_idx:end_idx], end_idx(ending_index) is not included

print ("print avi = ",str[1:4])
print ("print ravi = ",str[:4], "\n") #same as str[0:4]

print ("print avi raj = ",str[1:]) #same as str[1:len(str)]
print ("print one charactor = ",str[1:2], "\n")

#slicing negative index used access string from last
print ("print opposite string = ",str[-7:-1])

#print ("print opposite string = ",str[-1:-8])

#string function for Searching & Checking :
print ("check str end with er = ",str.endswith("er."), "\n")

print ("check str start with r = ",str.startswith("r"))
print ("make 1st letter as capital = ",str.capitalize(), "\n")

print ("in str replace vi with ja = ",str.replace("vi","ja"))
print ("in str replace r with k = ",str.replace("r","k"))

print ("find a in str = ",str.find("a")) #return 1st index of 1st occurence
print ("count how many time a in str = ",str.count("a"))