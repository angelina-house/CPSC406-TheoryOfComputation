from dfa import DFA  


def generate_words():
    words = [""]  
    alphabet = ['a', 'b']
    
    # Generate words 
    for first in alphabet:
        words.append(first)
        for second in alphabet:
            words.append(first + second)
            for third in alphabet:
                words.append(first + second + third)
    
    return words

def __main__():
    # Define DFA A1
    A1 = DFA(
        Q={1, 2, 3, 4},
        Sigma={'a', 'b'},
        delta={
            (1, 'a'): 2, (1, 'b'): 4,
            (2, 'a'): 2, (2, 'b'): 3,
            (3, 'a'): 3, (3, 'b'): 3,
            (4, 'a'): 4, (4, 'b'): 4
        },
        q0=1,
        F={3}
    )

    # Define DFA A2
    A2 = DFA(
        Q={1, 2, 3},
        Sigma={'a', 'b'},
        delta={
            (1, 'a'): 2, (1, 'b'): 1,
            (2, 'a'): 3, (2, 'b'): 1,
            (3, 'a'): 3, (3, 'b'): 3
        },
        q0=1,
        F={3}
    )

    words = generate_words()
    automata = [A1, A2]

    # Test words on automata
    for X in automata:
       # print(f"{X.__repr__()}") # prints dfa
        for w in words:
            print(f"{w}: {X.run(w)}") # prints true or false
        print("\n")

__main__()