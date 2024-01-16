def main():
    amt_due = 50
    while True:
        coin = int(input("Insert a coin:"))
        if coin == 25 or coin == 10 or coin == 5:
            amt_due = amt_due - coin
            if amt_due > 0:
                print("Amount Due:", amt_due)
        if amt_due <= 0:
            change = abs(amt_due)
            print("Change Owed:", change)
            break
main()
