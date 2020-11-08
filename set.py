#no duplicate values 
#immutable
#cannt support slicing or indexing.

print("set support union intersection difference complement")
#creating a set
my_set = {1,2,3}
print(my_set)
my_set = {1,2,3,(1,2,3)}
print(my_set)
my_set ={1,2,3,4,3,2,1}
print(my_set)

a = {}
print(type(a))

#to create an empty string
a = set()
print(type(a))

#adding ad deleteing 
a  ={1,2}
a.add(2)
print(a)
a.update([2,3,4,5]) # add mulitple items
print(a)

#delete items
print("A particular item can be removed from a set using the methods discard() and remove().The only difference between the two is that the discard() function leaves a set unchanged if the element is not present in the set. On the other hand, the remove() function will raise an error in such a condition (if element is not present in the set).")
a ={1,2,3,4,5}
print(a)
a.discard(4)
print(a)
a.remove(5)
print(a)

#discard the element which is not present in set
a.discard(6)
print(a)
#leave no change in set

#use remove while element is not present in set
#a ={1,2,3,4,5}
#a.remove(6)
#print(a)
#so remove method gives an error


#what if we want to clear set completely

a = {1,2,3,4,5,6,7}
a.clear()
print(a)

#so by using pop method it is unclear whic element gonna be deleted.
a = {1,2,3,4,5,6,7}
a.pop()
print(a)

#python set operations
c = {1,2,3,4,5,6}
b = {4,5,6,7,8,9}
print(c.union(b))

#use union by | operator
print(c | b) 

#intersection 
c = {1,2,3,4,5,6}
b = {4,5,6,7,8,9}
print(c.intersection(b))

#use operator
print(c & b)

#difference
c = {1,2,3,4,5,6}
b = {4,5,6,7,8,9}
print(c.difference(b))
print(b - c)

#set symmetric difference 
# Symmetric difference of two sets
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A ^ B)
#not include commans values.
a= {1,2,3}
b ={4,5,6}
print(a.isdisjoint(b))#written true if have null intersection.

#itreate through sets
for letter in set("apple"):
    print(letter)

#python frozenset
#python frozensets are set with immuatable elements.
A = frozenset([1,2,3,4,5])
B = frozenset([2,3,4,5,6])
print(A | B)


