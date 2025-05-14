#Task 2
from collections import defaultdict

grammar = {
    'S': [('A', 'B'), ('B', 'C')],
    'A': [('B', 'A'), ('a',)],
    'B': [('C', 'C'), ('b',)],
    'C': [('A', 'B'), ('a',)]
}

def reverse_grammar(grammar):
    new_map = defaultdict(set)
    for lhs in grammar:
        for rule in grammar[lhs]:
            new_map[rule].add(lhs)
    return new_map

def cyk_algorithm(grammar, input_string):
    n = len(input_string)
    if n == 0:
        return False

    reverse_map = reverse_grammar(grammar)
    table = [[set() for _ in range(n)] for _ in range(n)]

    for siam, character in enumerate(input_string):
        key = (character,)
        if key in reverse_map:
            table[siam][siam].update(reverse_map[key])

    for length in range(2, n+1):  
        for start in range(n - length + 1):  
            end = start + length - 1  
            for split in range(start, end):
                left = table[start][split]
                right = table[split+1][end]
                for B in left:
                    for C in right:
                        key = (B, C)
                        if key in reverse_map:
                            table[start][end].update(reverse_map[key])

    return 'S' in table[0][n-1]


def main():
    input_str = input("Enter string like 'ba': ").strip()
    result = cyk_algorithm(grammar, input_str)
    print("Accepted" if result else "Rejected")

main()