#Write a Python program that uses a lambda function to sort
# a list of tuples based on the second element of each tuple.
# Example input: [(2, 'banana'), (3, 'apple'), (1, 'orange')]
# Output: [(3, 'apple'), (2, 'banana'), (1, 'orange')]

input_list = [(2, 'banana'), (3, 'apple'), (1, 'orange')]
sorted_list = sorted(input_list, key=lambda x: x[1])

print(sorted_list)
