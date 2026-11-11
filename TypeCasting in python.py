# typecasting in python
a,b = 1,2.0
sum = a + b

print ("Value & Type of A = ",a, type(a))
print ("Value & Type of B = ",b, type(b))
print ("Value & Type of Sum of A and B = ",sum, type(sum), "\n")


c,d = 1,"2"
print("Value & Type of c",c,type(c))
print("Value & Type of d",d,type(d), "\n")

""" #Problem 1
    sum2 = c + d
    print ("C + D = ",sum2) #Generate error
"""
            #Solution of Problem 1 (Type Casting)
e = int (d)
sum3 = c + e

print ("Value & Type of E after Type Casting (D) = ",e, type(e))
print ("C + E = ",sum3, "\n")

num = "3"
Num = int(num) # here convert String (num) to Integer (Num) without input base 10
print("Value & Type of num = ",num,type(num))
print("Value & Type of Num = ",Num,type(Num), "\n")

num1 = 3
Num1 = float(num1)
print("Value & Type of num1 = ",num1,type(num1))
print("Value & Type of Num1 = ",Num1,type(Num1), "\n")

num2 = 6
Num2 = complex(num2)    #Creat Complex Number Without Writing (real[imag])
print("Value & Type of num2 = ",num2,type(num2))
print("Value & Type of Num2 = ",Num2,type(Num2), "\n")

num3 = 9
Num3 = str(num3)
print("Value & Type of num3 = ",num3,type(num3))
print("Value & Type of Num3 = ",Num3,type(Num3), "\n")

num4 = "Ravi"
Num4 = list(num4)   #List Value Always Apply On String
print("Value & Type of num4",num4,type(num4))
print("Value & Type of Num4",Num4,type(Num4), "\n")

num5 = 20
Num5 = hex(num5)
print("Value & Type of num5 :- ",num5,type(num5))
print("Value & Type of Num5 :- ",Num5,type(Num5))