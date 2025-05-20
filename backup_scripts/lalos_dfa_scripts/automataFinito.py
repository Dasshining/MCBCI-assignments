from maquinaEstado import Maquina_estado

class Automata_finito(Maquina_estado):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'Autómata Finito'

    def chain_review(self, chain):
        state = self.q0
        chain = self.test
        print(f"\nReviewing the chain: {chain}")

        for symbol in chain:
            if symbol not in self.sigma:
                print(f"Invalid Symbol: {symbol}")
                return False

            transition = self.f.get((state, symbol))
            if transition is None:
                print(f"There's not a defined transition for ({state}, {symbol}).")
                return False

            state = transition
            
            print(f" -> State: {state}")

        if state in self.F:
            print("Acepted Chain")
            return True
        else:
            print("Rejected Chain")
            return False