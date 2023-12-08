from functools import reduce

class Hand():

    
    # Five of a kind := 6
    # Four of a kind := 5
    # Full house := 4
    # Three of a kind := 3
    # Two pair := 2
    # One pair := 1
    # High card := 0
    ranking: dict[str, int] = {"2":0,"3":1,"4":2,"5":3,"6":4,"7":5,"8":6,"9":7,"T":8,"J":9,"Q":10,"K":11,"A":12}

    def __init__(self, cards: list[str], multiplicator: int):
        self.cards: list[str] = cards
        self.multiplicator: int = multiplicator

    def number_of_different_cards(self, cards: list[int]) -> int:
        index: int = 1
        res: int = 1
        while index < len(cards):
            if cards[index] != cards[index-1]:
                res += 1
        return res
        
    def get_type(self) -> int:
        card_copy = self.cards.copy()
        card_copy.sort()

        index: int = 1
        card_amount: list[int] = [1]
        while index < len(card_copy):
            if card_copy[index] != card_copy[index-1]:
                card_amount.append(1)
            else:
                card_amount[len(card_amount)-1] += 1
            index += 1

        card_amount.sort(reverse=True)
        
        if card_amount[0] == 5:
            return 6
        if card_amount[0] == 4:
            return 5
        if card_amount[0] == 3 and card_amount[1] == 2:
            return 4
        if card_amount[0] == 3:
            return 3
        if card_amount[0] == 2 and card_amount[1] == 2:
            return 2
        if card_amount[0] == 2:
            return 1
        
        return 0
    
    def compareCard(self, card1: str, card2: str) -> int:
        return self.ranking[card1] - self.ranking[card2]

    

    def __eq__(self, other):
        return self.get_type() == other.get_type() and self.cards[0] == other.cards[0] and self.cards[1] == other.cards[1]

    def __lt__(self, other):
        t1 = self.get_type()
        t2 = other.get_type()
        if t1 < t2:
            return True
        

        if t1 == t2:
            index: int = 0
            while index < len(self.cards):
                if self.compareCard(self.cards[index], other.cards[index]) != 0:
                    return self.compareCard(self.cards[index], other.cards[index]) < 0 
                index += 1

        return False


def main():
    f = open("input1.txt", "r")
    lines: list[str] = f.readlines()
    f.close()

    hands: list[Hand] = []
    for l in lines:
        tokens: list[str] = l.split(" ")
        hands.append(Hand(list(tokens[0]), int(tokens[1])))
        
    hands.sort()
    res: int = 0
    counter: int = 1
    for hand in hands:
        res += hand.multiplicator * counter
        counter += 1

    print(res)


    pass

if __name__ == "__main__":
    main()


#254024898