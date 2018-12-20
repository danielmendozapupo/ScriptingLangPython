import re
phone1 = re.compile(r"^((?:[(]\\d+[)]?\\s*\\d+(?:-\\d+)?)$")
phone2 = re.compile(r"^((?:[(]\d+[)]?\s*\d+(?:-\d+)?)$")
print (phone2)
