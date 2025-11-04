import math
#string data type

#literal assignment

first="Greeshma"
last="Kalattur"

print( type(first))
#type() tells you the data type of a variable.
#output : That means the value stored in first is a string (str = short for “string”).
print(type(first)==str)
#this checks whether the type of first is equal to str.
print(isinstance(first,str))
#isinstance() is another (and preferred) way to check data types.
#It checks:“Is first an instance of the class str?”
#The type() function in Python tells you the data type of any value, variable, or object.



#CONSTRUCTOR FUNCTION
pizza = 'pepper'
print(str("pepper"))
print(type(pizza))
print(type(pizza)==str)
print(isinstance(pizza,str))


#concatenation
fullname= first+ " " +last
print(fullname)
fullname+= '!'
print(fullname)

#CASTING A NUMBER TO A STRING
decade=str(1980)
statement="i like rock music from the " + decade +  "s"
print(statement)

#MULTIPLE LINES
multiline=''''
hey!!!
                   how are u ??
                         
                                   r u ok?

'''
print(multiline)


#ESCAPING SPECIAL CHARACTERS

sentence='I\'m back at work!\tHey!\n\nWhere\'s this at located?'
print(sentence)

#STRING METHODS






