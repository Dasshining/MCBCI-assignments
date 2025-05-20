import re

file = open("./automataDef.txt")
text = file.read()
print(file.read())


reSig = '(sigma)={([0-9](,[0-9])*)}'
matcherSig = re.compile(reSig)
matchSig = matcherSig.search(text)
print(matchSig)

gruposSig = matchSig.groups()
valoresSig = gruposSig[1]

reQ = '(Q)={(q[0-9](,q[0-9])*)}'
matcherQ = re.compile(reQ)
matchQ = matcherQ.search(text)
print(matchQ)

gruposQ = matchQ.groups()
valoresQ = gruposQ[1]

req0 = '(q0)=(q[0-9])'
matcherq0 = re.compile(req0)
matchq0 = matcherq0.search(text)
print(matchq0)

gruposq0 = matchq0.groups()
valoresq0 = gruposq0[1]

reF = '(F)={(q[0-9](,q[0-9])*)}'
matcherF = re.compile(reF)
matchF = matcherF.search(text)
print(matchF)

gruposF = matchF.groups()
valoresF = gruposF[1]


class Maquina_estado:
    def __init__(self):
        def __init__(self, sigma=None, Q=None, f=None, q0=None, F=None):
            self._sigma = valoresSig
            self._Q = valoresQ
            self._f = None
            self._q0 = valoresq0
            self._F = valoresF
            print(self._sigma)
    #self._sigma = ['0', '1']
    #self._Q = ['q1', 'q2']
    #self._q0 = 'q1'
    #self._f = {
    #    ('q1', '0'): 'q1',
    #    ('q1', '1'): 'q2',
    #    ('q2', '0'): 'q1',
    #    ('q2', '1'): 'q2'
    #}
    #self._F = ['q2']

    @property
    def sigma(self):
        return self._sigma

    @sigma.setter
    def sigma(self, value):
        if isinstance(value, list):
            self._sigma = value
        else:
            raise ValueError("Sigma must be a list")

    @property
    def Q(self):
        return self._Q

    @Q.setter
    def Q(self, value):
        if isinstance(value, list):
            self._Q = value
        else:
            raise ValueError("Q must be a list")

    @property
    def q0(self):
        return self._q0

    @q0.setter
    def q0(self, value):
        if isinstance(value, str):
            self._q0 = value
        else:
            raise ValueError("q0 must be a string")

    @property
    def f(self):
        return self._f

    @f.setter
    def f(self, value):
        if isinstance(value, dict):
            self._f = value
        else:
            raise ValueError("f must be a dictionary")

    @property
    def F(self):
        return self._F

    @F.setter
    def F(self, value):
        if isinstance(value, list):
            self._F = value
        else:
            raise ValueError("F must be a list")
