#f-string: formatted string literals

name = 'Kristine'
product = 'Python elearning course'
greeting = f'This is my {{bracket}} blog post'

email_content = f"""
Hi {name}

Thank you for purchasing {product}

Regards,

Sales Team
"""
print(email_content)
print(greeting)