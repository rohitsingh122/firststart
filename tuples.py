#so basically tuples are immutable because its content is never change once its made.
my_tuple = ()
print(my_tuple)

my_tuple = (1,2,3,4,5)
print(my_tuple)

my_tuple =(1,"hello",3.4)
print(my_tuple)

#nested tuple
my_tuple =("mouse",(1,3,4),(12,34,45))
print(my_tuple[0][3])
print(my_tuple[1][2])
print(my_tuple[2][1])

#tuples can be created without paranthesis
my_tuple = 1,2, "dogs"
print(my_tuple)

#tuple unpacking is also be done.
a,b,c = my_tuple
print(a)
print(b)
print(c)

tuple=(1,2,3)
print(type(tuple))


#tuple support -ve indexing

mytuple = (1,2,3,4,5)
print(mytuple[-3])

#slicing also can be happens in tuples
mytuple = (1,2,3,4,5)
print(mytuple[::-1])
print(mytuple[2:4])

#we cant change the content of tuples once we declared,
#But, if the element is itself a mutable data type like list,
#   its nested items can be changed.
mytuple = ("hello",[1,2,3],(5,6,7))
mytuple[1][1] = 9
print(mytuple)

#concatination by + operator
mytuple =(1,2,3,"hello")
mytuple1=(2,3,4,5,6)
print(mytuple + mytuple1)

#we cant change the content of tuple nither we delete the item
mytuple2 = (1,2,3,4)
del mytuple2
#This produces the following result. Note an exception raised, this is because after 
# del mytuple2 tuple does not exist any more −
#Advantages of Tuple over List
#Since tuples are quite similar to lists, both of them are used in similar situations. However, there are certain advantages of implementing a tuple over a list. Below listed are some of the main advantages:

#We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.
#Since tuples are immutable, iterating through a tuple is faster than with list. So there is a slight performance boost.
#Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
#If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.