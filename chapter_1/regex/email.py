import re

email = re.compile(r'(?P<user>[\w.]+)@(?P<domain>\w+)\.(?P<suffix>[a-z]{3})')
text = "My email is guido@python.org or guido@google.com"
print(*(x.groupdict() for x in email.finditer(text)))
