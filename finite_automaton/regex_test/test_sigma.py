chain = '010105'
estado_actual = 'q1'
sigma = '0,1'

exReg = '\([1], [0-1]* ,[1]*)'
f = '(q1 0)->q1', '(q1 1)->q2', '(q2 0)->q1', '(q2 1)->q2'
reg_f = '\(q[0-9] [0-1]\)->q[0-9]'

reglas = re.findall(reg_f, f)

f_dicc = {}
for regla in reglas:
    elementos_f = regla.split('->')
    f_dicc[elementos_f[0]] = elementos_f[1]

for simbolo in chain:
    key = f'({estado_actual} {simbolo})'
    estado_siguiente = f_dicc[key]
    print(f'Estado siguiente: {estado_siguiente}')