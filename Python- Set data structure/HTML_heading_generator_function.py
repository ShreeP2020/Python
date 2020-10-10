"""
heading_generator(title, heading_type)
heading_generator('Greetings!', '1')
<h1>Greetings!</h1>

heading_generator('I am in a title', '3')
<h3>I am in a title</h3>
"""


def heading_generator(title, heading_type):
  return f'<h{heading_type}>{title}</h{heading_type}>'
  

print(heading_generator('Greetings!', '1'))
print(heading_generator('I am in a title', '3'))