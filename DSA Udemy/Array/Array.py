""" One Dimensional Array """
# create array using array module:
from array import *
my_array = array('i', [1, 2, 3, 4, 5])
print(my_array)

# 1. traverse the array
for i in my_array:
    print(i)

# 2. Access individual elements through indexes
print("step 2")
print(my_array[0])
print(my_array[1])
print(my_array[2])
print(my_array[3])
print(my_array[4])

# 3. Append any value to the array using append() method
print("step-3")
my_array.append(10)
print(my_array)

# 4. Insert value in an array using insert() method
print("step-4")
my_array.insert(0, 15)    # it takes two parameter first index second element
print(my_array)

# 5. Extended python array using extended() method
print("step-5")
my_array1 = array('i', [20, 25, 30])   # my_array1 is a new array
my_array.extend(my_array1)
print(my_array)

# 6. Add items from list into array using fromlist() method
print("step-6")
temp_list = [16, 17, 18]
my_array.fromlist(temp_list)
print(my_array)

# 7. Remove any array element using remove() method
print("step-7")
my_array.remove(15)
my_array.pop()     # pop() method remove last element from the array
print(my_array)

# 8. find any index through its element using index() method
print("step-8")
print(my_array.index(20))

# 9. Reverse a python array using reverse() method
print("step-9")
my_array.reverse()
print(my_array)

# 10. Get array buffer information through buffer_info() method
print("step-10")
print(my_array.buffer_info())

# 11. Check for number of occurrences of an element using count() method
print("step-11")
print(my_array.count(5))    # by using count method we can find occurrences of an element

# 12. Slice Elements from an array
print("step-12")
print(my_array[0:])
print(my_array[1:5])
print(my_array[:])
print(my_array[:7])

""" Two Dimensional Array """
# Create two D array using Numpy module
import numpy as np

two_d_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [15, 16, 17, 18]])
print(two_d_array)

# Insertion Two Dimensional Array
new_two_d_array = np.insert(two_d_array, 0, [[50, 60, 70, 80]], axis=0)   # axis = 1, column
print(new_two_d_array)
# Approach 2
# new_two_d_array = np.append(two_d_array, [[25, 35, 45, 55]], axis=0)
# print(new_two_d_array)

# Accessing an element of Two dimensional Array
def accessElement(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        print("Incorrect Index")
    else:
        print(array[rowIndex][colIndex])


accessElement(two_d_array, 2, 3)

# Traversing Two dimensional Array
def traverseTDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])


traverseTDArray(two_d_array)

# Searching for an element in Two dimensional Array
import numpy as np

two_d_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [15, 16, 17, 18]])
print(two_d_array)

def searchTDArray(array, value):
    for i in range(len(array)):     # Row
        for j in range(len(array[0])):  # Column
            if array[i][j] == value:
                return 'The value is located at index '+str(i)+" "+str(j)
    return 'The element is not found'


print(searchTDArray(two_d_array, 11))

# Deletion in 2D Array
import numpy as np

two_d_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [15, 16, 17, 18]])
print(two_d_array)

new2DArray = np.delete(two_d_array, 0, axis=1)  # axis = 0 row, axis = 1, column
print(new2DArray)
