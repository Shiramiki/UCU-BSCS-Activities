stack_example = []

#append() function to push elements in the stack
stack_example.append('one')
stack_example.append('two')
stack_example.append('Three')
stack_example.append('four')

print("Initial stack with four elements one, two, three, four loaded in sequence ")
print(stack_example)

#pop() function to pop elements from stack to LIFO order:
print("3 Elements popped from a stack in LIFO order")
print(stack_example.pop())
print(stack_example.pop())
print(stack_example.pop())

print("\nStack after 3 elements are popped")

print(stack_example)

#stack left with one element
