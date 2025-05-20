from automataFinito import Automata_finito
from automataPila import Automata_pila
from maquinaTuring import Maquina_turing

chains = ['1', '0', '11', '101', '01010', '000', '111111']

# Autómata Finito
automataFinito = Automata_finito()
print(automataFinito)
for chain in chains:
    automataFinito.chain_review(chain)

# Autómata con Pila
automataPila = Automata_pila()
print(automataPila)
#for chain in chains:
#    automataPila.chain_review(chain)

# Máquina de Turing
maquinaTuring = Maquina_turing()
print(maquinaTuring)
#for chain in chains:
#    maquinaTuring.chain_review(chain)

# path = 'nombre del archivo'
# file = open(path)
# text = file.read()   o   text = file.read lines()
# print(type(text))

'''EXPRESIONES REGULARES'''
# import re              - Libreria para expresiones regulares
# re_Q = 'Q = {q[0-9](,q[0-9])*}'
# matcher = re.compile(re_Q)
# print(matcher)
# print(type(matcher))
# match = matcher.search(text)
# rupos = match.groups()
# variable = grupos[0]
# valor = grupos[1]
# print(variable, valor)
# re.search()
# print(match)
# print(match.groups())