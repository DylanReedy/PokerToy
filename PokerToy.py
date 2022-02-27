import tkinter as tk
import tkinter.ttk as ttk
from CardDeck import *

class GameState:

    def __init__(self):
        self.deck = Deck()

class PokerGUI(ttk.Label):
    #The gui keeps track of the card currently be selected with an int index
    activecardslot = 0
    activecard = Card(None, None)
    drawncards = []
    activecardbuttons = []
    activecardstrings = []

    def __init__(self, parent):

        def update_card_display():
            if self.activecard.valid() and self.activecardslot is not None:
                cardinfo = str(self.activecard.rank) + str(self.activecard.suit)
                if cardinfo in self.drawncards:
                    print('ERROR: CARD HAS ALREADY BEEN SELECTED')
                else:
                    self.drawncards.append(cardinfo)
                    self.activecardbuttons[self.activecardslot].configure(text=cardinfo)
                self.activecardslot = None
                self.activecard.rank = None
                self.activecard.suit = None

        def update_card_slot(activeslot):
            self.activecardslot = activeslot
            update_card_display()

        def update_card_rank(rank):
            self.activecard.rank = rank
            update_card_display()

        def update_card_suit(suit):
            self.activecard.suit = suit
            update_card_display()

        super().__init__(parent)
        self.applicationheader = ttk.Label(self, text="Poker Toy", padding="5 5 5 5")
        self.applicationheader['relief'] = 'sunken'
        self.applicationheader.grid(column=1, row=0)

        # Create the 3 columns

        # Create handpicker column
        self.handpickerframe = ttk.Frame(self)
        self.handpickerframe['borderwidth'] = 2
        self.handpickerframe['relief'] = 'sunken'
        self.handpickerframe.grid(column=0, row=1, sticky='n')
        self.handpickerlabel = ttk.Label(self.handpickerframe, text='Hand Picker', padding="5 5 5 5")
        self.handpickerlabel.grid(column=0, row=0)

        self.ranknames = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
        self.suitnames = ['\u2663', '\u2666', '\u2665', '\u2660']
        self.rankbuttons = []
        self.suitbuttons = []

        def hideRankButtons():
            for button in self.rankbuttons:
                button.grid_remove()
            for button in self.suitbuttons:
                button.grid()

        def showRankButtons():
            for button in self.rankbuttons:
                button.grid()

        def onSuitButtonClick(suit):
            showRankButtons()
            update_card_suit(suit)

        def onRankButtonClick(rank):
            hideRankButtons()
            update_card_rank(rank)

        for x in range(0, 4):
            self.suitbuttons.append(ttk.Button(self.handpickerframe, text=self.suitnames[x],
                                               command=lambda suit=self.suitnames[x]: onSuitButtonClick(suit)))
            self.suitbuttons[x].grid(column=0, row=x + 1)
            self.suitbuttons[x].grid_remove()

        for x in range(0,13):
            self.rankbuttons.append(ttk.Button(self.handpickerframe, text=self.ranknames[x],
                                               command=lambda rank=self.ranknames[x]: onRankButtonClick(rank)))
            self.rankbuttons[x].grid(column=0, row=x + 1)

        #Create current hand column
        self.currenthandframe = ttk.Frame(self)
        self.currenthandframe['borderwidth'] = 2
        self.currenthandframe['relief'] = 'sunken'
        self.currenthandframe.grid(column=1, row=1, sticky='n')

        #Create contents for current hand column
        #Column label
        self.currenthandlabel = ttk.Label(self.currenthandframe, text='Current Hand', padding="5 5 5 5")
        self.currenthandlabel.grid(column=0, row=0)
        self.currenthandlabel['borderwidth'] = 2
        self.currenthandlabel['relief'] = 'sunken'

        self.pocketcardslabel = ttk.Label(self.currenthandframe, text='Pocket Cards', padding="5 5 5 5")
        self.pocketcardslabel.grid(column=0, row=1)
        self.pocketcardslabel['borderwidth'] = 2
        self.pocketcardslabel['relief'] = 'sunken'

        self.pocketcardsframe = ttk.Frame(self.currenthandframe)
        self.pocketcardsframe['borderwidth'] = 2
        self.pocketcardsframe['relief'] = 'sunken'
        self.pocketcardsframe.grid(column=0, row=2)

        for x in range(0, 2):
            self.activecardbuttons.append(ttk.Button(self.pocketcardsframe, text='[--]',
                                                     command=lambda x=x: update_card_slot(x)))
            self.activecardbuttons[x].grid(column=x, row=0)

        self.communitycardslabel = ttk.Label(self.currenthandframe, text='Community Cards', padding="5 5 5 5")
        self.communitycardslabel.grid(column=0, row=3)
        self.communitycardslabel['borderwidth'] = 2
        self.communitycardslabel['relief'] = 'sunken'

        self.communitycardsframe = ttk.Frame(self.currenthandframe)
        self.communitycardsframe['borderwidth'] = 2
        self.communitycardsframe['relief'] = 'sunken'
        self.communitycardsframe.grid(column=0, row=4)

        self.communitycardbuttons = []
        self.communitycardstrings = []

        for x in range(0, 5):
            # there are 7 active cards, and the first two are the pocket cards, so the community cards assignments are offset by 2
            self.activecardbuttons.append(ttk.Button(self.communitycardsframe, text='[--]',
                                                     command=lambda x=x+2: update_card_slot(x)))
            self.activecardbuttons[x+2].grid(column=x, row=0)


        self.dataframe = ttk.Frame(self)
        self.dataframe['borderwidth'] = 2
        self.dataframe['relief'] = 'sunken'
        self.dataframe.grid(column=2, row=1, sticky='n')
        self.datalabel = ttk.Label(self.dataframe, text='Hand Data', padding="5 5 5 5")
        self.datalabel.grid(column=2, row=0)

        #Widgets are added, now lock in the size of the app
        self.update()
        self.grid_propagate(False)


