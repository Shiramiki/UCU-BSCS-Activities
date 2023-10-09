# Scenario Assignment

"""
There once was a hat. The hat contained no rabbit, but a list of five numbers: 1, 2, 3, 4, and 5.

Your task is to:

write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (Step 1)
write a line of code that removes the last element from the list (Step 2)
write a line of code that prints the length of the existing list (Step 3).

"""

hat = [1,2,3,4,5]
hat[2] = int(input("please enter a number:"))
#print(hat)
del(hat[-1])
#print(hat)
print("length of the list is:", len(hat))
