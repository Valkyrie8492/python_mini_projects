# let's make a slot machine

MAX_LINES = 3

def deposit() -> int:
    while True:
        amount = input("How much will you bet? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("You must bet more than 0!")
        else:
            print("Please enter a valid amount to wager.")
    return amount

def get_number_of_lines() -> int:
    while True:
        lines = input("How many lines will you bet on? (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if lines > 0 and lines <= MAX_LINES:
                break
            elif lines < 1:
                print("You must bet on at least one!")
            elif lines > MAX_LINES:
                print("There aren't that many lines!")
        else:
            print("Please enter a valid number of lines!")
    return lines

def main():
    pass