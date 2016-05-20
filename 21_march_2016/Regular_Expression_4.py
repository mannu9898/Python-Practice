import re

message = 'My phone number are 9984 9856 4562 '

phoneRegex = re.compile(r'(\d\d\d\d ){3}')

mo = phoneRegex.search(message)

print(mo.group())

print(phoneRegex.findall(message))

