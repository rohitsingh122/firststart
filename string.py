name ="edureka"
print(name[-1:-8:-1])
print(name[::-1])
a = "python is a intrepreted language"
print(a[5:])
print(a[0:15:2])
print(a[::-1 ])
print(a.capitalize()) #for making first word capital
print(a.count("p")) #count how many times a word is reapted
print(a.find("p")) # to find the pos of value
print(a.isalnum())
print(a.upper())
print(a.replace("p","$")) # takes two arguments 
print(a.strip()) #basically return the clean version of string
print(a.split("a"))#splits the string into parts according to user 

#operations on ptyhon

a = "python"
b = "ruby"
print(a+b)#concatination of two strings
print((a+b)*2)

#string interpolation
#string interploation is a method which makes is easier for developers to execute string formatting and concatination in python

# % formatting
c = "you can learn %s easily, and %s too" %(a,b)
print(c)

city1 = "delhi"
city2 = "calcutta"
print("the two main cities of india are %s , %s " %(city1,city2))

# f string 

d =f'you can learn {a} and {b} easily'
print(d)

name1 = "amar"
name2 = "sandeep"
print(f"i have 2 bestfriendsyh {name1} , {name2}")

#string.format

e = "you can easily learn{a} and {b}".format(a=a,b=b)
print(e)

name = "rohit"
print("my name is {}".format(name))
