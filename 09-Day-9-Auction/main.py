'''
Auction
'''
import os
from art import logo

print(logo)
print('Welcome to the secret auction prgram.')

END_AUCTION = False
bids_data = []
while not END_AUCTION:
    name  = input("What is your name? ")
    bid = float(input("What is your bid? $"))
    bid_dict = {}
    bid_dict['name'] = name
    bid_dict['bid'] = bid
    bids_data.append(bid_dict)

    any_other_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if any_other_bidder == 'no':
        END_AUCTION = True
    clear = lambda: os.system('clear')
    clear()
# Sort to get highest bid
bids_data.sort(key = lambda d: d['bid'], reverse = True)

print(f"The winner is {bids_data[0]['name']} with {bids_data[0]['bid']}")
