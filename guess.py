def get_guess():
    guess = int(input("Enter a guess: "))
    return guess

def main():
    guess = get_guess
    if guess == 15:
        print("CORRECT!")
    else:
        print("INCORRECT!!")
        off = abs(15 - guess)
        print("you were off by " + str(off))
        

main()

    