import re

phoneNumRegex = re.compile(r'((Super|Spider|Bat|Iron)man){1}')

message = 'Batman and Spiderman are chutiya but Ironman is a swagger'

mo = phoneNumRegex.search(message)

print(mo.group())

print(phoneNumRegex.findall(message))
