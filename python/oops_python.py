
# # Private attributes start with "__".

# # Creating a Base class
# class Base:
#     def __init__(self):
#         self.a = "GeeksforGeeks"
#         self.__c = "GeeksforGeeks" 
# # # Creating a derived class
# class Derived(Base):
#     def __init__(self):

#         # Calling constructor of
#         # Base class
#         Base.__init__(self)
#         print("Calling private member of base class: ")
#         print(self.__c)


# # Driver code
# obj1 = Base()
# print(obj1.a)

# # Uncommenting 
# print(obj1.c) 
# will
# raise an AttributeError

# Uncommenting 
# obj2 = Derived() 
# will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class



# Python program to 
# demonstrate protected members 

# Creating a base class 
# class Base: 
# 	def __init__(self): 

# 		# Protected member 
# 		self._a = 2

# # Creating a derived class 
# class Derived(Base): 
# 	def __init__(self): 

# 		# Calling constructor of 
# 		# Base class 
# 		Base.__init__(self) 
# 		print("Calling protected member of base class: ", 
# 			self._a) 

# 		# Modify the protected variable: 
# 		self._a = 3
# 		print("Calling modified protected member outside class: ", 
# 			self._a) 


# obj1 = Derived() 

# obj2 = Base() 

# # Calling protected member 
# # Can be accessed but should not be done due to convention 
# print("Accessing protected member of obj1: ", obj1._a) 

# # Accessing the protected variable outside 
# print("Accessing protected member of obj2: ", obj2._a) 


# class student:
#     def __init__(self,name="xyz",age=18):
#         self.name = name 
#         self.age = age

# s1 = student()
# print(s1.__dict__)

# setattr(s1,"value",62)

# print(s1.__dict__)

# s2=student()

# print(s2.__dict__)

# print(s2.__doc__)

# class Employee:  
#     __count = 0;  
#     def __init__(self):  
#         Employee.__count = Employee.__count+1  
#     def display(self):  
#         print("The number of employees",Employee.__count)  
# emp = Employee()  
 
# try:  
#     emp.display()  

#     # print(emp.__count)  
# finally:  
#     # emp.display()  
#     print(emp.__count)  



class Vehicle:
    def display(self):
        print("base class")

class Car(Vehicle):
    def display(self):
        print("car class")

class Truck(Vehicle):
    def display(self):
        # super().display()
        print("truck class")
        # super().display()
class Cycle(Truck,Car):
    def display(self):
        pass

# t = Truck()
# t.display()
c = Cycle()

print(Cycle.__mro__)
