#Write a Python program that takes a nested dictionary where
# each key is a person's name, and the value is another dictionary
# containing their age and city. The program should print out all
# the names of people who live in 'New York' and are over 30 years old.
# Example input:
#people = {
#	'John': {'age': 45, 'city': 'New York'},
#	'Mike': {'age': 22, 'city': 'Los Angeles'},
#	'Sarah': {'age': 32, 'city': 'New York'},
#	'Anna': {'age': 28, 'city': 'Chicago'}
#}
# Output: ['John', 'Sarah']

people = {
    'John': {'age' : 45, 'city': 'New york'},
    'Mike': {'age': 22, 'city': 'Los Angeles'},
    'Sarah': {'age': 32, 'city': 'New york'},
    'Anna': {'age': 28, 'city': 'Chicago'}
}

result = [name for name,info in people.items() if info['city'] == 'New york' and info['age'] > 30]

print(result)

