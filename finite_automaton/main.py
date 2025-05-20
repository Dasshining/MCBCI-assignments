from dfa import Automaton

def retrieve_dfa():
    file = "./automataDef.txt"
    reSig = r'(sigma)={([0-9](,[0-9])*)}'
    reQ = r'(Q)={(q[0-9](,q[0-9])*)}'
    ref = r"\(q\d \d\)->q\d"
    req0 = r'(q0)=(q[0-9])'
    reF = r'(F)={(q[0-9](,q[0-9])*)}'
    reTest = r'(test)={[(\w)*\, ]*}'
    dfa = Automaton(file, reSig, reQ, ref, req0, reF, reTest)
    dfa.printDfaDefinition()

    for i in range(len(dfa.test)):
        dfa.chain_review(dfa.test[i])

retrieve_dfa()
