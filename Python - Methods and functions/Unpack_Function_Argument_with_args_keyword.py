def greeting(*args):
  print('Hi ' + ' '.join(args))


greeting('Kristine', 'M', 'Hudgens')
greeting('Tiffany', 'Hudgens')


def greeting1(*names):
  print('Hi ' + ' '.join(names))


greeting1('Kristine', 'M', 'Hudgens')
greeting1('Tiffany', 'Hudgens')


def greeting2(time_of_day, *args):
  print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}")


greeting2('Afternoon', 'Kristine', 'M', 'Hudgens')
greeting2('Morning', 'Tiffany', 'Hudgens')