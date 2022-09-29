from replit import clear
# You can call clear() to clear the output in the console.

from art import logo

print(logo)

bids = {}
bidding_finished = False


def find_hightest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Bill": 123, "John": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


while not bidding_finished:
    print("Welcome to the secret auction program.")
    name = input("What is you name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no.\n").lower()
    if should_continue == 'no':
        find_hightest_bidder(bids)
        bidding_finished = True
    elif should_continue == 'yes':
        clear()