from auction import Auction


def launch():

    valid_game = True

    while valid_game:
        print("\x1B[2J")
        print("Welcome to the Secret Auction")
        auction = Auction()

        name = input("What is your name: ")

        while True:
            try:
                bid = int(input("What is your bid? $"))
                break
            except:
                print("Invalid bid, try again!")

        auction.new_bidder(name, bid)

        while True:
            valid_bidders = input(
                "\nAre there any other bidders? Type 'yes' or 'no'\n").lower()
            if valid_bidders == "no":
                break
            elif valid_bidders != "yes":
                print("Invalid input, try again!")
                continue

            print("\x1B[2J")
            name = input("What is your name: ")
            while True:
                try:
                    bid = int(input("What is your bid? $"))
                    break
                except:
                    print("Invalid bid, try again!")

            auction.new_bidder(name, bid)

        print("\x1B[2J")
        auction.check_winner()

        new_auction = input(
            "\nDo you want to start a new auction? Type 'yes' or 'no'\n").lower()

        if new_auction == "no":
            valid_game = False
