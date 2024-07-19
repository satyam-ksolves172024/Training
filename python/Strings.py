name = "Alice"
age = 30
height = 1.75

# Using f-string
formatted_string = f"{name:010} is {age:05d} years old and {height:.2f} meters tall."

# Using format() method
# formatted_string = "{0:10} is {1:02d} years old and {2:.2f} meters tall.".format(name, age, height)

print(formatted_string)

# x="hello world"

# x="{0:7.4f}".format(1.2)
# print(len(str(x)))
# print(x)

# print('{0:3.4f}'.format(623.6365))

# age =23
# print(f"hello,{age},my age is {1}")
# print('Mayuri "Agrawal"')

# temp=(1,2,[1,2],{1:4,2:3})
# print(temp)
# print(temp[3])
# print(temp[3].keys())

# temp1=(1,2,[1,2,3],(1,2,3))
# print(temp1)

# print(temp1)


Dict = {1: 'Geeks', 'name': [1,2,3], 3: 3}
# print("Accessing a element using key:")
# print(Dict['name'])
# print("Accessing a element using get:")
# print(Dict[4])

# for key , value in Dict.items():
#     if type(value)==list:
#         print(key,'=',end=' ')
#         for i in value:
#             print(i,end=' ')
#         print('\n')
#     else:
#         print(key,'=',value)
    
# temp = [1,2,3,4,54]

# print(type(temp))

# set1 = set(Dict)
# print(set1)

# print(type(set1))

# Dict = dict([(1, 'Geeks','2'), (2, 'For')])
# print("\nDictionary with each item as a pair: ")
# print(Dict)


temp=[1,2,3,4]
temp1=[3,45,5]
temp.extend(temp1)
print(temp)
di={1:2,3:3}
temp.extend(di)
print(temp)
temp.insert(2,7)
print(temp.sort())
temp.pop(3)       #it takes index as parameter
print(temp)
temp.remove(5)    #it takes value as parameter
print(temp)
temp1 = temp[::-1]
print(temp1)

from collections import Counter

dict1 = Counter(temp1)

print(temp.count(3))

print(dict1)

set1=set(temp)
set1.add(9)
print(set1)

# animals = ['cat','dog','monkey','Cow','goat']

# animals = sorted(animals,key = len(str))

# px=(5,2,1)
# x=sorted(px)
# print(x)


thistuple = ("apple", "banana", "cherry")
y = ("orange","mango")
thistuple += y

print(thistuple)


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

green, yellow, *red = fruits

print(green)
print(yellow)
print(red)

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)
