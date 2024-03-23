# let's make a slot machine

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

def deposit() -> int:
    while True:
        amount = input("How much will you deposit? $")
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

def get_bet() -> int:
    while True:
        amount = input("What would you like to bet? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("Please pick a valid amount to bet.")
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount! Your current balance is ${balance}")
        else:
            break
    
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: {total_bet}.")
    
    print(balance, lines, bet)

if __name__ == "__main__":
    main()