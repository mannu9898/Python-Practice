import re

phoneRegex = re.compile(r'((\(\d\d\) )?(\d){10}(,)?){3}')

message = 'My phone numbers are  (91) 7533010073,8009981401,(91) 9838416939'

print(phoneRegex.findall(message))

mo = phoneRegex.search(message)

print(mo.group())


#(\(\d\d\))?

#(,)?){3}

