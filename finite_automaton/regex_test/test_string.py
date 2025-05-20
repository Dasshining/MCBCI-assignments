import re

a = '@test={1,0,11,101,01010,000,111111}'
ref = r'(test)={[(\w)*\, ]*}'

test = re.compile(ref)
test = test.search(a)
test = test.group()
print(test)

test = test.split("=")
print(test)
test = test[1].strip("{}")
print(test)
test = test.split(",")
print(test)