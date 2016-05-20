import re

message = 'Call me 415-555-1011 tomorrow or at 415-555-95 99'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

print(phoneNumRegex.findall(message))

#print(mo.group())
