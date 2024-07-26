import numpy as np

arr = np.array([[1,2,3],[3,4,5]])
# print(arr.ndim)
# print(arr[0:2][1])

arr2 = np.array([[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7]])

# temp = arr2[1:,2:4]

# temp1 = arr2[:,[0,1,3]]
# print(temp)
# print(arr2<3)
arr1 = arr2<3
newarr = arr2[arr1]

# print(newarr)

arr3 = np.zeros_like(arr2)

# print(arr3)
# print(arr2)


x = [1, 2, 3, 4,5]
# y = [4, 5, 6, 7]
# z = []

# for i, j in zip(x, y):
#   z.append(i + j)
# print(z)



# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# for x in np.nditer(arr):
#   print(x)

# newarr = np.array(x,dtype="S")

# print(newarr)


# print(type(newarr[0]))

# for ind,val in np.ndenumerate(x):
#     print(ind)

# x[ind]


import numpy as np
from numpy import linalg as geek

# Creating an array using array function
# a = np.array([[1, -2j], [2j, 5]])

# print("Array is:", a)

# # Calculating eigenvalues and eigenvectors using eigh() function
# c, d = geek.eigh(a)

# print("Eigenvalues are:", c)
# print("Eigenvectors are:", d)


# x = np.arange(0, 9)
# A = np.array([x, np.ones(9)])

# print(A)

# # Creating an array using diag function
# a = np.diag((1, 2, 3))

# print("Array is:", a)



# Python Program illustrating
# numpy.linalg.lstsq() method
 
 
import numpy as np
import matplotlib.pyplot as plt
 
# x co-ordinates
x = np.arange(0, 9)
A = np.array([x, np.ones(9)])
 
# linearly generated sequence
y = [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24]
# obtaining the parameters of regression line
# w = np.linalg.lstsq(A.T, y)[0] 
 
# # plotting the line
# line = w[0]*x + w[1] # regression line
# plt.plot(x, line, 'r-')
# plt.plot(x, y, 'o')
# plt.show()


# ones_arr = np.ones((4,5,3))
# ones_arr_1d = np.ones((1,5))
# print(ones_arr_1d)
# product = ones_arr * 5

# print(product.shape)
# print(ones_arr)

# A      (4d array):  8 x 1 x 6 x 1
# B      (3d array):      7 x 1 x 5
# Result (4d array):  8 x 7 x 6 x 5

ones_arr = np.ones((8,1,6,1))
ones_arr_1d = np.ones((7,1,6))

print(ones_arr.ndim)

''' *************************ERROR*******************************
product = ones_arr * ones_arr_1d
ValueError: operands could not be broadcast together with shapes (8,1,6,1) (7,2,6) '''


product = ones_arr * ones_arr_1d
ones_arr_1d.flatten()
print(ones_arr_1d)
print("")
print(ones_arr)
print(product.shape)