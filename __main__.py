from tkinter import Tk
import __player__ as pl

def init() :    
    __game__ = Tk()
    __game__.title("Snake")
    play = pl.Player(__game__)
    play.Update(__game__)
    __game__.mainloop()

if __name__ == "__main__" :
    init()