import deck


class Solitaire:
    def __init__(self):
        self.deck = deck.Deck()
        self.deck.shuffle()
        self.tableau = [[], [], [], [], [], [], []]
        self.foundation = [[], [], [], []]
        self.waste = []
        self.stock = []
        self._deal()

    def _deal(self):
        for x in range(7):
            for i in range(x, 7):
                self.tableau[i].append(self.deck.draw(1)[0])
            self.tableau[x][-1].flip()
        self.stock = self.deck.draw(24)

    def draw(self):
        if len(self.stock) == 0:
            self.waste.reverse()
            self.stock = self.waste
            self.waste = []
        else:
            for i in range(3):
                if len(self.stock) > 0:
                    self.waste.append(self.stock.pop())

    def move_to_foundation(self, card, from_list):
        for f in self.foundation:
            if (not f and card.number == 1) or (f and card.suit == f[0].suit and card.number == f[-1].number + 1):
                f.append(card)
                card.flip()
                from_list.remove(card)
                if len(from_list) > 0:
                    from_list[-1].flip()
                return True
        return False

    def move_to_tableau(self, cards: list, tableau, from_list):
        card = cards[0]

        if (not tableau and card.number == 13) or (tableau and card.number == tableau[-1].number - 1 and card.isRed() != tableau[-1].isRed()):
            for c in cards:
                tableau.append(c)
                c.flip()
                from_list.remove(c)
            if len(from_list) > 0:
                from_list[-1].flip()
            return True
        return False

    def print_game(self):
        print("Foundation")
        print("-"*20)
        for f in self.foundation:
            if len(f) == 0:
                print("[ ]", end='\t')
            else:
                print("[", f[-1], "]", end='\t')
        print("\n")

        max_tableau_height = max(len(t) for t in self.tableau)

        tableaus_width = len(self.tableau)*15

        print("Tableaus".center(tableaus_width))
        for i in range(1, len(self.tableau)+1):
            print(f"      {i}".ljust(15), end=' ')
        print()
        print("-"*tableaus_width)

        for i in range(max_tableau_height):
            print(f"{i+1} |".ljust(4), end='')
            for t in self.tableau:
                if i < len(t):
                    if t[i].flipped:
                        print(f"[ {t[i]} ]".ljust(24), end=' ')
                    else:
                        print("[ ]".ljust(15), end=' ')
                else:
                    print(" ".ljust(15), end=' ')
            print("\n  |  ")

        # Print Stock and Waste
        print()
        print(f"Stock: [ ({len(self.stock)}) ]")
        print(
            f"Waste: [ {self.waste[-1] if self.waste else ''} ({len(self.waste)}) ]")
        print("\n")


def getNum(vals):
    val_string = [str(v + 1) for v in vals]
    a = input("Input (" + ", ".join(val_string) + "): ")
    if a in val_string:
        return int(a)
    return getNum(vals)


def move_from_tableau(game):
    print("What tableau would you like to move from?")
    source = getNum(range(7)) - 1
    tableau = game.tableau[source]
    if not tableau:
        return
    indices = [i for i in range(
        len(tableau)) if tableau[i].flipped]
    index = -1
    if (len(indices) > 1):
        print("What starting index of card would you like to move?")
        index = getNum(indices) - 1
    if (index == len(tableau) - 1 or index == -1):
        print("Would you like to move to (1) another tableau or (2) a foundation?")
        b = getNum(range(2))
    else:
        b = 1
    cards = []
    if (index != -1):
        for i in range(index, len(tableau)):
            cards.append(tableau[i])
    else:
        cards.append(tableau[-1])
    match b:
        case 1:
            print("What tableau would you like to move to?")
            dest = getNum(range(7)) - 1
            if game.move_to_tableau(cards, game.tableau[dest], tableau):
                print("Moved card.")
            else:
                print("Invalid move.")
        case 2:
            if game.move_to_foundation(cards[0], tableau):
                print("Moved card.")
            else:
                print("Invalid move.")


def move_from_waste(game):
    if game.waste:
        print("Would you like to move to (1) a tableau or (2) a foundation?")
        b = getNum(range(2))
        match b:
            case 1:
                print("What tableau would you like to move to?")
                dest = getNum(range(7)) - 1
                card = game.waste[-1]
                if game.move_to_tableau([card], game.tableau[dest], game.waste):
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


def move_from_foundation(game):
    if any(game.foundation):
        print("What foundation would you like to move from?")
        source = getNum(range(4)) - 1
        found = game.foundation[source]

        if len(found) < 1:
            print("No cards in foundation.")
            return

        print("What tableau would you like to move to?")
        dest = getNum(range(7)) - 1
        card = found[-1]
        if game.move_to_tableau([card], game.tableau[dest], found):
            print("Moved card.")
        else:
            print("Invalid move.")

    else:
        print("No cards in foundation.")


def menu(game):
    print("What would you like to do?")
    print("Options: \n (1) Draw from stock \n (2) Move a card from tableau \n (3) Move a card from waste \n (4) Move a card from a foundation \n (5) Quit")
    a = getNum(range(5))
    match a:
        case 1:
            game.draw()
        case 2:
            move_from_tableau(game)
        case 3:
            move_from_waste(game)
        case 4:
            move_from_foundation(game)
        case 5:
            exit()
        case _:
            pass


def game_over(game):
    for f in game.foundation:
        if len(f) < 13:
            return False
    return True


def play_game():
    game = Solitaire()

    while True:
        print("\n")
        print("-"*15)
        print("\n")
        if (game_over(game)):
            print(
                "Congratulations! You've won solitare. Would you like to: \n (1) Play again? \n (2) Quit")
            a = getNum(range(2))
            match a:
                case 1:
                    game = Solitaire()
                case 2:
                    exit()
        game.print_game()
        menu(game)


if __name__ == "__main__":
    play_game()
