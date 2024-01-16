def greeting():
    greet = input("Enter your greetings: ")
    return greet

def main():
    greet = greeting().strip()
    greetn = greet.lower()
    if greetn.startswith("hello"):
        print("$0")
    elif greetn.startswith("h"):
        print("$20")
    else:
        print("$100")

main()
