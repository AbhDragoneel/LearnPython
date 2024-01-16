def main():
    camelcase = input("camelCase: ")
    print(to_snake(camelcase))


def check_up(tocheck):
    counter = 0
    for c in tocheck:
        if c.isupper():
                return c


def to_snake(camelCase):
    l1 = [''] * len(camelCase)
    i = 0
    for c in camelCase:
        if c.isupper():
            c = c.lower()
            l1.insert(i,"_")
            i+=1
            l1[i] = c
        else:
            l1[i] = c
        i+=1

        final_string = ''.join(l1)

    return final_string
main()
