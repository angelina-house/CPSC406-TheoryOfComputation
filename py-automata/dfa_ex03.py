from dfa import DFA 

def generate_words():
    words = [""]
    alphabet = ['a', 'b']
    
    for first in alphabet:
        words.append(first)
        for second in alphabet:
            words.append(first + second)
            for third in alphabet:
                words.append(first + second + third)
    
    return words

def __main__():
    # Define DFA A 
    A = DFA(
        Q={1, 2, 3, 4},  
        Sigma={'a', 'b'},  
        delta={  
            (1, 'a'): 2, (1, 'b'): 4,
            (2, 'a'): 3, (2, 'b'): 4,
            (3, 'a'): 3, (3, 'b'): 3,
            (4, 'a'): 2, (4, 'b'): 4
        },
        q0=1,  # Initial state
        F={3, 4}  # Accepting state
    )

    # Define DFA A0 (refuse)
    A0 = A.refuse()

    words = generate_words()
    automata = [A, A0]

    # Test words on automata
    for X in automata:
        # print(f"{X.__repr__()}") # prints dfa
        for w in words:
            print(f"{w}: {X.run(w)}")  # Prints true or false
        print("\n")

__main__()