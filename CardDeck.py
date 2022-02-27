from enum import IntEnum
from enum import Enum

class Rank(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


class Suit(IntEnum):
    CLUB = 0
    DIAMOND = 1
    HEART = 2
    SPADE = 3


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def valid(self):
        return (self.rank is not None) & (self.suit is not None)

class Deck:

    cards = []
    def __init__(self):
        for rank in Rank:
            for suit in Suit:
                self.cards.append(Card(rank, suit))

def DrawCard(deck, card):
    offsetrank = int(card.rank) - 2
    suit = int(card.suit)
    index = (offsetrank * len(Suit)) + int(card.suit)
    card = deck[index]
    deck[index] = None
    return card

# class HoleCards:
#     def __init__(self, first, second):
#         cards = [first, second]


# Special mention deserved for subskybox, author of this article:
# https://www.codeproject.com/Articles/569271/A-Poker-hand-analyzer-in-JavaScript-using-bit-math
# I had to debug for python a little bit, but the article is amazing and the algorithms elegant.

A = 14
K = 13
Q = 12
J = 11
T = 10

cs = [2, Rank.ACE, Rank.ACE, Rank.ACE, Rank.ACE]
ss = [0, 1, 2, 3, 0]
s = 1 << cs[0]-2 | 1 << cs[1]-2 | 1 << cs[2]-2 | 1 << cs[3]-2 | 1 << cs[4]-2
v = 0
o = 0
# print(f"{s:052b}")
print(cs)

for i in range(0, len(cs)):
    o = 1 << (cs[i] - 2)*4
    v += o * (((v//o) & 15)+1)
    # print('offset: ',o)
    # print(f"bit set: {v:052b}")

print(f"bit set: {v:052b}")
print(v)
v = (v) % 15# - ((s/(s&-s) == 31) or 3 if (s == 0x403c) else 1)
bitSetStraightToAce = 4111
straight = (s/(s&-s) == 31) or (s == bitSetStraightToAce)
print(straight)
v = (v) % 15 - (3 if straight else 1)
print(v)

hands = ["4 of a kind", "Straight Flush", "Straight", "Flush", "High Card", "1 Pair", "2 Pair", "", "3 of a Kind", "Full House"]

flush = ss[0] == (ss[1]|ss[2]|ss[3]|ss[4])

# Note that this will in no way catch errors from card arguments. For example, if the cards " 2 2 3 5 7 " all spades (impossible in a real deck)
# come in, the final result will be "high card".
v -= flush

print('Hand: ', hands[v])

# print(f"{v:052b}")
# print(f"{o:052b}")

