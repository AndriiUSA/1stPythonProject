def get_bet_details():
    all_bets = []

    while True:
        bet_details = {}

        name = input("Enter your name: ")
        bet_details['name'] = name

        size = int(input("Enter the size of the bet: "))
        bet_details['size'] = size

        all_bets.append(bet_details)

        # print("Bet details:", bet_details)

        repeat = input("Do you want to enter another bet? (yes/no): ")
        if repeat.lower() != 'yes':
            # print("\nHiding previous bets and rates...\n")
            break

    return all_bets


def get_highest_bid(bets):
    if not bets:
        return None

    highest_bid = max(bets, key=lambda x: x['size'])
    return highest_bid


bets = get_bet_details()
highest_bid = get_highest_bid(bets)

if highest_bid:
    print("The highest bid is:", highest_bid['size'])
    print("Name with the highest bid:", highest_bid['name'])
else:
    print("No bids were entered.")

