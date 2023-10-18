import numpy as np

# Create an array with mixed data types
sample = [22, 8.5, (3 + 6j), "RACHEL"]
myarray = np.array(sample)

# Test for complex numbers
complex_check = np.iscomplex(myarray)
#print(np.iscomplex(myarray))

complex_numbers = myarray[complex_check]
#print(myarray[complex_check])

# Test for real numbers
real_check = np.isreal(myarray)
real_num = myarray[real_check]

# Test if a given number is of a scalar type
numbercheck = 42
isScalar = np.isscalar(numbercheck)

print(f"The Sample Array is:\n{myarray}")
print(f"\nComplex Numbers are: {complex_numbers}")
print(f"\nReal Numbers are: {real_num}")
print(f"\nIs {numbercheck} a scalar? {isScalar}")
