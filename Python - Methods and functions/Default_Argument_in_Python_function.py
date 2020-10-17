def greetings(name = 'Guest'):
    print(f'Hi {name}!')


greetings()
greetings('Kristine')

# Nope
def some_function(collection = []):
  collection.append(1)
  print(id(collection))
  return collection


print(some_function())
print(some_function())