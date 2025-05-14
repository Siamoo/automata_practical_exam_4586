#Taks 3
def is_prime(n):
    if n < 2:        
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def simulate_turing_machine(user_input):
    if any(siam != '1' for siam in user_input): # check if any other char not "1"
        print(f"{user_input} is not prime, Invalid characters in input ")
        return False

    num = len(user_input) 
    
    if is_prime(num):
        print(f" {user_input} is  prime.")
        return True
    else:
        print(f" {user_input} is not prime.")
        return False


def main():
    tape_input = input("Enter ur input like '111' : ").strip()
    simulate_turing_machine(tape_input)

main()