f = open("input2.txt", "r")

class ScratchCard:

    def __init__(self, id: int, winning_numbers: list[int], card_numbers: list[int]) -> None:
        self.id = id
        self.winning_numbers = winning_numbers
        self.card_numbers = card_numbers
        self.matches = -1


def card_with_id(id: int, cards: list[ScratchCard]) -> ScratchCard:
    return next(filter(lambda x: x.id == id, cards))
    
def scratch_the_cards(id: int, cards: list[ScratchCard]) -> int:
    card: ScratchCard = card_with_id(id, cards)
    
    if card.matches != -1:
        return card.matches
    
    matches: int = 0
    for c in card.card_numbers:
        if c in card.winning_numbers:
            matches += 1
    
    for i in range(id + 1, id + 1 + matches):
        matches += scratch_the_cards(i, cards)
    
    card.matches = matches
    return card.matches
    pass

cards: list[ScratchCard] = []
for line in f.readlines():
    
    numbers: list[str] = line.split(":")
    id: int = int(numbers[0].split(" ")[-1])

    tokens: list[str] = numbers[1].split(" | ")

    win_numbers: list[int] = []
    for n in tokens[0].split(" "):
        if n != '':
            win_numbers.append(int(n))

    card_numbers: list[int] = []
    for n in tokens[1].split(" "):
        if n != '':
            card_numbers.append(int(n))
    cards.append(ScratchCard(id, win_numbers, card_numbers))
    pass

all_matches: int = 0
for card in cards:
    all_matches += scratch_the_cards(card.id, cards) + 1

print(all_matches)
