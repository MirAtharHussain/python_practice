#int DataTpe: To represent integer's.
a=10
print(type(a))
print(a)

#float DataType: To represent Floating point data.

f=1.234
type(f)
print(f)

#complex DataType: a and b contain Intergers OR Floating Point Values, contians Real and Imaginary part.
a=10+1.5j
b=20+2.5j
c = a+b
print(c)

#Boolean Data Type: To represent boolean values i.e., True  and False.
a = True
if (a==True):
    print("Mir Athar Hussain")
else:
    print("a is not true.")

#str Data Type: Represents string datatype. A String is a sequence of characters enclosed within single quotes or double quotes.
a = 'Mir Athar Hussain'
b = "Mir Athar Hussain"
if(a == b):
    print(True)
else:
    print(False)

s1 = ''' hello
world'''
print(s1)
s1 = """Hellow
world"""
print(s1)

s = '''This "Python class very helpful" for java students'''
print(s)

#Slicing of Strings.
#slice means a piece
#\[ \] operator is called slice operator, which can be used to retrieve parts of String.
#In Python Strings follows zero based index.
#The index can be either +ve or -ve.
#+ve index means forward direction from Left to Right
#-ve index means backward direction from Right to Left

m = 'Kabir_Ali'
print(m[:])
print(m[0])
print(m[-1])
print(m[1:])
print(m[:5])
print(m[1:9])

print(m*2)
print(len(m))