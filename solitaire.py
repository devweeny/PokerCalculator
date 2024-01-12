import deck


class Solitaire:
    def __init__(self):
        self.deck = deck.Deck()
        # self.deck.shuffle()
        self.tableau = [[], [], [], [], [], [], []]
        self.foundation = [[], [], [], []]
        self.waste = []
        self.stock = []
        self._deal()

    def _deal(self):
        for x in range(7):
            for i in range(x, 7):
                self.tableau[i].append(self.deck.draw(1)[0])
        self.stock = self.deck.draw(24)

    def draw(self):
        if len(self.stock) == 0:
            self.waste.reverse()
            self.stock = self.waste
            self.waste = []
        for i in range(3):
            if len(self.stock) > 0:
                self.waste.append(self.stock.pop())

    def move_to_foundation(self, card, from_list):
        for f in self.foundation:
            if (not f and card.number == 1) or (f and card.suit == f[0].suit and card.number == f[-1].number + 1):
                f.append(card)
                from_list.remove(card)
                return True
        return False

    def move_to_tableau(self, card, tableau, from_list):

        if (not tableau and card.number == 13) or (tableau and card.number == tableau[-1].number - 1 and card.isRed() != tableau[-1].isRed()):
            tableau.append(card)
            from_list.remove(card)
            return True
        return False

    def print_game(self):
        for f in self.foundation:
            if len(f) == 0:
                print("[ ]", end='\t')
            else:
                print("[", f[-1], "]", end='\t')
        print("\n")

        for t in self.tableau:
            if len(t) == 0:
                print("[ ]", end='\t')
            else:
                print("[", t[-1], f"({len(t)})", "]", end='\t')
        print("\n")

        print(
            f"Stock: [ {self.stock[-1] if self.stock else ''} ({len(self.stock)}) ]")
        print(
            f"Waste: [ {self.waste[-1] if self.waste else ''} ({len(self.waste)}) ]")


def getNum(vals):
    vals = [str(v + 1) for v in vals]
    a = input("Input (" + ", ".join(vals) + "): ")
    if a in vals:
        return int(a)
    return getNum(vals)


def menu(game):
    print("What would you like to do?")
    print("Options: \n (1) Draw from stock \n (2) Move a card from tableau \n (3) Move a card from waste \n (4) Move a card from a foundation \n (5) Quit")
    a = getNum(range(5))
    match a:
        case 1:
            game.draw()
        case 2:
            print("What tableau would you like to move from?")
            source = getNum(range(7)) - 1
            if not game.tableau[source]:
                return
            print("Would you like to move to (1) another tableau or (2) a foundation?")
            b = getNum(range(2))
            match b:
                case 1:
                    print("What tableau would you like to move to?")
                    dest = getNum(range(7)) - 1
                    card = game.tableau[source][-1]
                    if game.move_to_tableau(card, game.tableau[dest], game.tableau[source]):
                        print("Moved card.")
                    else:
                        print("Invalid move.")
                case 2:
                    card = game.tableau[source][-1]
                    if game.move_to_foundation(card, game.tableau[source]):
                        print("Moved card.")
                    else:
                        print("Invalid move.")
        case 3:
            if game.waste:
                print("Would you like to move to (1) a tableau or (2) a foundation?")
                b = getNum(range(2))
                match b:
                    case 1:
                        print("What tableau would you like to move to?")
                        dest = getNum(range(7)) - 1
                        card = game.waste[-1]
                        if game.move_to_tableau(card, game.tableau[dest], game.waste):
                            print("Moved card.")
                        else:
                            print("Invalid move.")
                    case 2:
                        card = game.waste[-1]
                        if game.move_to_foundation(card, game.waste):
                            print("Moved card.")
                        else:
                            print("Invalid move.")
            else:
                print("No cards in waste.")
        case 4:
            if any(game.foundation):
                print("What foundation would you like to move from?")
                source = getNum(range(4)) - 1
                print(
                    "Would you like to move to (1) a tableau or (2) another foundation?")
                b = getNum(range(2))
                match b:
                    case 1:
                        print("What tableau would you like to move to?")
                        dest = getNum(range(7)) - 1
                        card = game.foundation[source][-1]
                        if game.move_to_tableau(card, game.tableau[dest], game.foundation[source]):
                            print("Moved card.")
                        else:
                            print("Invalid move.")
                    case 2:
                        card = game.foundation[source][-1]
                        if game.move_to_foundation(card, game.foundation[source]):
                            print("Moved card.")
                        else:
                            print("Invalid move.")
            else:
                print("No cards in foundation.")
        case 5:
            exit()
        case _:
            pass


def play_game():
    game = Solitaire()
    ended = False

    while not ended:
        print("\n")
        print("-"*15)
        print("\n")
        game.print_game()
        menu(game)


if __name__ == "__main__":
    play_game()
