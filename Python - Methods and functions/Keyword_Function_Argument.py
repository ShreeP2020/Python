def greeting(**kwargs):
  print(kwargs)


greeting()
greeting(first = 'Kristine', last = 'Hudgens')

def greeting1(**kwargs):
  if kwargs:
    print(f"Hi {kwargs['first']} {kwargs['last']}, have a great day!")
  else:
    print('Hi Guest!')


greeting1()
greeting1(first = 'Kristine', last = 'Hudgens')