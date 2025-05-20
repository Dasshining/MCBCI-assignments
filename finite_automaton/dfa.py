import re

class Automaton:
    def __init__(self, file, regSigma, regQ, regf, regq0, regF, regTest):
        self.file = open(file)
        self.text = self.file.read()
        self.sigma = self.get_sigma(regSigma)
        self.Q = self.get_Q(regQ)
        self.f = self.get_f(regf)
        self.q0 = self.get_q0(regq0)
        self.F = self.get_F(regF)
        self.f_dicc = self.fToDic()
        self.test = self.get_test(regTest)
    
    def chain_review(self, chain):
        state = self.q0
        print(f"\nReviewing the chain: {chain}")

        for symbol in chain:
            if symbol not in self.sigma:
                print(f"Invalid Symbol: {symbol}")
                return False

            key = f'({state} {symbol})'
            transition = self.f_dicc[key]
            if transition is None:
                print(f"There's not a defined transition for ({key}).")
                return False
            
            state = transition
            print(f" -> State: {state}")

        if state in self.F:
            print("Acepted Chain")
            return True
        else:
            print("Rejected Chain")
            return False
    
    def get_sigma(self, regSigma):
        try:
            sigma = re.compile(regSigma)
            sigma = sigma.search(self.text)
            sigma = sigma.groups()
            sigma = sigma[1]
            return sigma
        except:
                return 0
    
    def get_Q(self, regQ):
        try:
            q = re.compile(regQ)
            q = q.search(self.text)
            q = q.groups()
            q = q[1]
            return q
        except:
            return 0
    
    def get_f(self, regf):
        try:
            f = re.compile(regf)
            f = f.findall(self.text)
            return f
        except:
            return 0
    
    def get_q0(self, regq0):
        try:
            q0 = re.compile(regq0)
            q0 = q0.search(self.text)
            q0 = q0.groups()
            q0 = q0[1]
            return q0
        except:
            return 0
    
    def get_F(self, regF):
        try:
            f = re.compile(regF)
            f = f.search(self.text)
            f = f.groups()
            f = f[1]
            return f
        except:
            return 0
    
    def get_test(self, regTest):
        try:
            test = re.compile(regTest)
            test = test.search(self.text)
            test = test.group()
            test = test.split("=")
            test = test[1].strip("{}")
            test = test.split(",")
            return test
        except:
            return 0
    
    def get_regex_definition(self, regex):
        try:
            regOutput = re.compile(regex)
            regOutput = regOutput.findall(self.text)
            return regOutput
        except:
            return 0

    def printDfaDefinition(self):
        print(f'sigma={self.sigma}')
        print(f'Q={self.Q}')
        print(f'f={self.f}')
        print(f'q0={self.q0}')
        print(f'F={self.F}')
        print(f'Test={self.test}')
    
    def fToDic(self):
        f_dicc = {}
        for rule in self.f:
            f = rule.split("->")
            f_dicc[f[0]] = f[1]
        return f_dicc