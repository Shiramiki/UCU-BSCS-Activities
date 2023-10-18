import numpy as np

# Create a NumPy array with the values 1, 7, 13, 105
myarray = np.array([1, 7, 13, 105])

# Determine the size of memory occupied by the array
memory_size = myarray.nbytes

print("NumPy array:")
print(myarray)
print(f"Size of memory occupied by the myarray is: {memory_size} bytes")
