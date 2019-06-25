#Question 1
#Replace all odd numbers in array with -1
import numpy as np
list1 = [0,1,2,3,4,5,6,7,8,9]
arr1 = np.array(list1)

arr1[:][(arr1[:]%2 == 1)] = -1
print("Solution 1: Replace all odd numbers in array with -1")
print(arr1)

#Question 2
#Convert 1d array into 2d array with 2 rows
arr2 = np.arange(10)

B1 = np.reshape(arr2, (-1, 5))
print("Solution 2: Convert 1d array into 2d array with 2 rows")
print(B1)

#Question 3
#Generate custom sequence in numpy without hardcoding
a = np.array([1,2,3])

b = np.r_[np.repeat(a,3),np.tile(a,3)]

print("Solution 3:Generate custom sequence in numpy without hardcoding")
print(b)

#Question 4
#Get common items between 2 numpy arrays
a1 = np.array([1,2,3,2,3,4,3,4,5,6])
b3 = np.array([7,2,10,2,7,4,9,4,9,8])

c = np.intersect1d(a1,b3)
print("Solution 4: Get common items between 2 numpy arrays")
print(c)

#Question 5
#Get positions of 2 arrays where elements match
d = np.nonzero(np.in1d(a1,b3))
print("Solution 5: Get positions of 2 arrays where elements match")
print(d)

#Question 6
#Create 2D array containing random floats between 5 and 10 (5x3)
a2 = np.random.uniform(5,high = 10,size=(5, 3))
print("Solution 6: Create 2D array containing random floats")
print(a2)

#Question 7
#Limit the number of items printed in numpy array
np.set_printoptions(threshold= 5)
print("Solution 7: Limit the number of items printed in numpy array")
arr3 = np.arange(15)

print(arr3) 

#Question 8
#Pretty print numpy array by supressing scientific notation
np.random.seed(100)
np.set_printoptions(suppress=True)
rand_arr = np.random.random([3,3])/1e3
print("Solution 8: Pretty print numpy array by supressing scientific notation")
print(rand_arr)

#Question 9
#Swap 2 columns in a 2D numpy array
print("Solution 9: Swap 2 columns")
arr4 = np.arange(9).reshape(3, 3)
print("Original Array")
print arr4

def swap_cols(arr01, frm, to):
    arr01[:,[frm, to]] = arr01[:,[to, frm]]

swap_cols(arr4, 0, 1)
print("Column Swapped array")
print arr4

#Question 10
#Swap 2 rowa in a 2D numpy array
print("Solution 10: Swap 2 Rows")
arr5 = np.arange(9).reshape(3, 3)
print("Original Array")
print arr5

def swap_rows(arr02, frm, to):
    arr02[[frm, to],:] = arr02[[to, frm],:]


swap_rows(arr5, 0, 1)
print("Row Swapped array")
print arr5

