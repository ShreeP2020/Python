post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

# Removing elements from end
post = post[:-1]
print(post)

# Removing elements from beginning
post = post[1:]
print(post)

# Removing specific element (messy/not recommended)
post = list(post)
post.remove('Intro guide to Python')
post = tuple(post)

print(post)