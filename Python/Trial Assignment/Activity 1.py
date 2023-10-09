"""
Activity 1: 
Question: Write a Python function that calculates the sum of even numbers and the sum of all odd numbers in a given range.

"""

even_total = 0
odd_total = 0
counter =int(input("How many numbers do you want to add"))
nums=[counter]
count = 0

while count < counter:
    nums[count] = int(input(f"Please enter a number {count+1} value"))
    count= count + 1

def summation(nums):
    for num in nums:
        if (num % 2 == 0):
            even_total += num
            num= num + 1
            
        else:
            odd_total += num
        
    print(f"The total of all even numbers is {even_total}")
    print(f"The total of all odd numbers is {odd_total}")

summation(nums)
