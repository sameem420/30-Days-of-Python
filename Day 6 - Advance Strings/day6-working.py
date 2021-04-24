text = "This is a really {myText} string.".format(myText="really cool")

print(text)

text1 = "This is a really {0} {1} string.".format("really", "cool")

print(text1)

data = {'name': 'Hodor', 'email': 'holdthe@door.com'}
txt = 'Name: {name}\nEmail: {email}'.format(**data)
print(txt)



first = "Hello"
second = "World"
third = 32.3122
fourth = "{:.2f}".format(third)
txt = f"{first} {second} {first.upper()} {third} {fourth}"
print(txt)