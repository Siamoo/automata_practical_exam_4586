#task 1
from collections import deque
from typing import Set, Dict, Tuple

class DFA:
    def __init__(self,
                states: Set[str],
                alphabet: Set[str],
                transition_function: Dict[Tuple[str, str], str],
                start_state: str, accept_states: Set[str]
                ):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def accepts(self, input_string: str) -> bool:
        current = self.start_state
        for siam in input_string:
            if (current, siam) not in self.transition_function:
                return False
            current = self.transition_function[(current, siam)]
        return current in self.accept_states

def symmetric_difference(dfa1: DFA, dfa2: DFA) -> DFA:
    set_of_states = set()
    dict_of_transitions = {}
    set_of_accepts = set()

    for s1 in dfa1.states:
        for s2 in dfa2.states:
            state_now = (s1, s2)
            set_of_states.add(state_now)

            for siam in dfa1.alphabet:
                next1 = dfa1.transition_function.get((s1, siam))
                next2 = dfa2.transition_function.get((s2, siam))
                if next1 is not None and next2 is not None:
                    dict_of_transitions[(state_now, siam)] = (next1, next2)

            # Accept if only one of them is in accept states not tow dfa
            accept_1 = (s1 in dfa1.accept_states)
            accept_2 = (s2 in dfa2.accept_states)
            if accept_1 != accept_2 :
                set_of_accepts.add(state_now)

    start = (dfa1.start_state, dfa2.start_state)

    return DFA(
        states=set_of_states,
        alphabet=dfa1.alphabet,
        transition_function=dict_of_transitions,
        start_state=start,
        accept_states=set_of_accepts
    )

def symmetric(dfa: DFA) -> bool:
    seen = set()
    q = deque([dfa.start_state])
    seen.add(dfa.start_state)

    while q:
        curr = q.popleft()
        if curr in dfa.accept_states:   #have a difference
            return False 

        for siam in dfa.alphabet:
            next = dfa.transition_function.get((curr, siam))
            if next and next not in seen:
                seen.add(next)
                q.append(next)

    return True

def same_or_not(dfa1: DFA, dfa2: DFA) -> bool:
    two_dfa = symmetric_difference(dfa1, dfa2)
    return symmetric(two_dfa)

def main():

    dfa1 = DFA(
        states={'q0', 'q1'},
        alphabet={'0', '1'},
        transition_function={
            ('q0', '0'): 'q0',
            ('q0', '1'): 'q1',
            ('q1', '0'): 'q0',
            ('q1', '1'): 'q1',
        },
        start_state='q0',
        accept_states={'q0'}
    )
    print('\ndfa1 -->',dfa1.accepts('1010'))

    dfa2 = DFA(
        states={'s0', 's1'},
        alphabet={'0', '1'},
        transition_function={
            ('s0', '0'): 's0',
            ('s0', '1'): 's1',
            ('s1', '0'): 's0',
            ('s1', '1'): 's1',
        },
        start_state='s0',
        accept_states={'s0'}
    )
    print('dfa2 -->',dfa2.accepts('1010'))

    if same_or_not(dfa1, dfa2):
        print("DFAs are same language ")
    else:
        print("DFAs are not same language ")

main()