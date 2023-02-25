class Auction:
    def __init__(self) -> None:
        self.bidders = {}

    def new_bidder(self, name: str, bid: int) -> None:
        self.bidders[name] = bid

    def check_winner(self):
        winner_name = None
        winner_bid = 0

        for i in self.bidders:
            if self.bidders[i] > winner_bid:
                winner_bid = self.bidders[i]
                winner_name = i

        print(f"The winner is {winner_name} with a bid of {winner_bid}")
