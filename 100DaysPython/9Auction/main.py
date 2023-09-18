bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"Winner is - {winner}")

while not bidding_finished:
    name = input("What is your name?")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_continue = input("Any other bidders? yes/no ")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)