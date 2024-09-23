from art import logo

print(logo)

bids= {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid ${highest_bid}.")
import clear
while not bidding_finished:
    bidder_name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: $"))
    bids[bidder_name] = bid_amount
    
    should_continue = input("Are there any bidders? Type 'yes' or 'no' ").lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    else :
        clear.clear_screen()
