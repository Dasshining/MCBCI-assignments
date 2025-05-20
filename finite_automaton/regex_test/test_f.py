import re

a = '@f={(q1 0)->q1,(q1 1)->q2,(q2 0)->q1,(q2 1)->q2}'
ref = r"\(q\d \d\)->q\d"
print(a)

rules = re.compile(ref)
rules = re.findall(ref, a)
print(rules)

rules = re.findall(ref, a)
print(rules)

f_dicc = {}
for rule in rules:
    f = rule.split("->")
    f_dicc[f[0]] = f[1]
print(f_dicc)

chain = '00'
state = 'q1'

for symbol in chain:
    key = f'({state} {symbol})'
    print(key)
    nextState = f_dicc[key]
    print(f'Next state: {nextState}')