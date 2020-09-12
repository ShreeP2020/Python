# heading = "Python: An Introduction, and Python: Advanced"

# header, _, subheader = heading.partition(': ')

# print(header)
# print(subheader)

tags = 'python,coding,programming,development'

list_of_tags = tags.split(',')
another_list_of_tags = tags.split()

print(list_of_tags)
print(another_list_of_tags)

heading = "Python: An Introduction"

heading, subheading = heading.split(': ')

print(heading)
print(subheading)