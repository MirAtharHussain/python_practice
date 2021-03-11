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

#LIST DATA TYPE: To represent a group of values as a single entity where
#Insertion Order is preserved
#Heterogeneous Objects are allowed
#Duplicates are allowed
#Growable in nature
#Values should be enclosed within square brackets.


#List is Mutuable i.e., its can be changed.

list0=[10,10.5,'mir',True,10]
print(list0)
for i in list0:
    print(i)

print(list0[0])
print(list0[:])
print(list0[-1])
list0[0] = 100
print(list0[0])


#Growing or reducing  list

list1 = [10, 20, 30]
print(list1)
list1.append('Ali')
print(list1)
list1.remove(10)
print(list1)

list2 = list1*2
print(list2)

#TUPLE Data TYpe: Tuple elements can be represented within parenthesis.
#tuple data type is exactly same as list data type except that it is immutable.i.e we cannot chage values.
#Note: tuple is the read only version of list.

tuple = (10, 20, 30)
print(tuple)
tuple = (10, 20, 30, 'Ali')
print(tuple)


#RANGE Data Type: To represents a sequence of numbers.
#The elements present in range Data type are not modifiable. i.e range Data type is immutable.

r = range(10)
for i in r :
    print(i)

r = range(10,20)
for i in r :
    print(i)

r = range(10,20,2)
for i in r:
    print(i)

print(r[0])


print(list(range(10)))


#set Data Type: If we want to represent a group of values
# Insertion order is not preserved
# Duplicates are not allowed
# Heterogeneous objects are allowed
# Index concept is not applicable---
# It is mutable collection----
# Growable in nature

s={100,0,10,200,10,'durga'}
print(s)

#print(s[0])===>TypeError: 'set' object does not support indexing

s.add(70)
print(s)

s.remove(10)
print(s)

#frozenset Data Type:
# It is exactly same as set except that it is immutable.
# Hence we cannot use add or remove functions.

s={10,20,30,40}
fs=frozenset(s)

#frozenset({40, 10, 20, 30})
for i in fs:
    print(i)

#dict Data Type
#If we want to represent a group of values as key-value pairs then we should go for dict data type.
#Duplicate keys are not allowed but values can be duplicated. If we are trying to insert an entry with duplicate key then old value will be replaced with new value.
#Note: dict is mutable and the order won’t be preserved.

d = {1:'Ali',2:'Haider',3:'karrar'}
print(d)
d[3] = 'Haider'
print(d)
#We can create empty dictionary as follows
d1 = {}
print(d1)
#We can add key-value pairs as follows
d1['a']= 'apple'
d1['b'] = 'best'
print(d1)

