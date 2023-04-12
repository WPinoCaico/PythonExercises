import sys

a = "HOLA MUNDO"
b = 25
c = -25
d = [1,2,3]
e = (1,2,3)

print ("LAS VARIABLES SON: \n")
print (a)
print (b)
print (c)
print (d)
print (e)

print ("\n\nLOS PESOS SON\n")

print (sys.getsizeof(a))
print (sys.getsizeof(b))
print (sys.getsizeof(c))
print (sys.getsizeof(d))
print (sys.getsizeof(e))

input()