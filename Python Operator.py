a = 50
b = 10
print ("value of a =", 50)
print ("value of b =", 50, "\n")


print ("Airthmetic Operator")
print ("a + b =", a + b)
print ("a - b =", a - b)
print ("a * b =", a * b)
print ("a / b =", a / b)
print ("a % b =", a % b)
print ("a ** b =", a ** b) #a ka power b
print ("b ** a =", b ** a, "\n") #b ka power a


print ("Relational/Comparison Operators")
print ("a == b :- ", a == b)
print ("a != b :- ", a != b)
print ("a > b :- ", a > b)
print ("a >= b :- ", a >= b)
print ("a < b :- ", a < b)
print ("a <= b :- ", a <= b, "\n")

# Problem 1 ( Try By Self )
print ("a =", a + 50)
print ("a =", a + 50, "\n") #a = 100, because value of a is constant not variable


print ("Assignment Operator") #Solution of Problem 1
# equal to ( = ) is also an assignment operator
a += 50
print ("a = ",a)

a -= 50
print ("a = ",a)

a *= 50
print ("a = ",a)

a /= 50
print ("a = ",a)

a %= 50
print ("a = ",a)

a **= 50
print ("a = ",a, "\n")

print ("Logical Operator")
print (not False)   #not operator
print (not True)

print (not (a>b))
print (not (a<b))

val1 = True
val2 = False
print ("and operator :- ",val1 and val2)
print ("or operator :- ",val1 or val2)