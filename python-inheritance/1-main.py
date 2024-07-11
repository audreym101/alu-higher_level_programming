# Import the MyList class from the 1-my_list module
MyList = __import__('1-my_list').MyList

# Create an instance of MyList
my_list = MyList()

# Append elements to the list
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)

# Print the original list
print(my_list)

# Print the sorted list
my_list.print_sorted()

# Print the original list again to ensure it has not been modified
print(my_list)
File: tests/1-my_list.txt (for test cases, if needed)
