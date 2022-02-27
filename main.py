import PokerToy
from PokerToy import GameState
import tkinter as tk
import tkinter.ttk as ttk
import CardDeck

root = tk.Tk()
root.title("Poker Toy")
gamestate = GameState()

# mainframe = ttk.Frame(root)
# mainframe.grid(column=0, row=0)
pokergui = PokerToy.PokerGUI(root)
pokergui.grid(column=0, row=0)

root.mainloop()

