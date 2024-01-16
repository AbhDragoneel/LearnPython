def main():
    print_square(int(input("Enter size:")))

def print_column(height):
    for _ in range(height):
        print("#")

def print_row(width):
    print("#" * width)

def print_square(size):
    for i in range(size):
        print_row(size)

'''def print_square(size):
    #for each row in square
    for i in range(size):
        #for each column in square
        for j in range(size):
            print("#", end="")
        print()'''


main()