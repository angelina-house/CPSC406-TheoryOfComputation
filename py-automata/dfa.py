# dfa.py
class DFA:
    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q  # Set of states
        self.Sigma = Sigma  # Alphabet
        self.delta = delta  # Transition function
        self.q0 = q0  # Initial state
        self.F = F  # Accepting states

    def __repr__(self):
        return f"DFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"

    def run(self, w):
        current_state = self.q0
        for symbol in w:
            if symbol not in self.Sigma:
                return False
            current_state = self.delta.get((current_state, symbol))
            if current_state is None:
                return False
        return current_state in self.F  # Accept if in accepting state

    def refuse(self):
        #new dfa that refuses input
        return DFA(self.Q, self.Sigma, self.delta, self.q0, set())  
    
# Example DFA 
if __name__ == "__main__":
    Q = {'q0', 'q1'}
    Sigma = {'0', '1'}
    delta = {
        ('q0', '0'): 'q0',
        ('q0', '1'): 'q1',
        ('q1', '0'): 'q1',
        ('q1', '1'): 'q0'
    }
    q0 = 'q0'  # Initial state
    F = {'q1'}  # Accepting state

    dfa = DFA(Q, Sigma, delta, q0, F)
    print(dfa.run('101'))  # false
    print(dfa.run('100'))  # true