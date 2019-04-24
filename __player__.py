from tkinter import Canvas
from random import randint

class Player :

    def __init__(self, tk) :
        self.flag, self.dirflag, self.xsp, self.ysp = False, False, 10, 0       
        self._can = Canvas(tk, width=500, height=500)
        self._can.configure(background='black')
        self._len, self._li, self.RectangleList, self.IndexList = 1, [(0, 0)], [self._can.create_rectangle(0, 0, 10, 10, fill='white')], [0]
        self._can.bind("<Button-1>", self.Yo)
        self._can.bind("<Key>", self.UpdateDir)
        self._can.pack()
        self.foodpos = self.FoodGenerator(tk)

    def IncreaseSize(self) :
        last, bef = self._li[self._len-1], (-1, -1) if self._len == 1 else self._li[self._len-2]
        xnew, ynew = last[0] - Conditional(bef != (-1, -1), bef[0]-last[0], self.xsp), last[1] - Conditional(bef != (-1, -1), bef[1]-last[1], self.ysp)
        self.RectangleList.append(self._can.create_rectangle(xnew, ynew, xnew+10, ynew+10, fill='white'))
        self._li.append((xnew, ynew))
        self._len += 1
        
    def OutOfBounds(self):
        return self._li[0][0] < 0 or self._li[0][0] > 490 or self._li[0][1] < 0 or self._li[0][1] > 490

    def Update(self, tk) :
        if self.flag: 
            self.dirflag, temp = False, self._li[0]
            self._can.move( self.RectangleList[0] , self.xsp , self.ysp )
            self._li[0] = ( self._li[0][0]+self.xsp , self._li[0][1]+self.ysp )
            if self._li[0] in self._li[1:] or self.OutOfBounds() :
                print('Game Over')

            else :
                for i in self.IndexList[1:] :
                    disx, disy = (temp[0]-self._li[i][0]), (temp[1]-self._li[i][1])
                    self._can.move(self.RectangleList[i], disx, disy)
                    temp = self._li[i]
                    self._li[i] = (self._li[i][0]+disx, self._li[i][1]+disy)

                if self._li[0][0] == self.foodpos[0] and self._li[0][1] == self.foodpos[1] :
                    self._can.delete(self.foodpos[2])
                    self.IncreaseSize()
                    self.IndexList.append(self._len-1)
                    self.foodpos = self.FoodGenerator(tk)

                tk.after(75, self.Update, tk)
        else :
            tk.after(500, self.Update, tk)

    def FoodGenerator(self, tk) :
        x, y = (randint(1, 49)*10), (randint(1, 49)*10)
        while (x, y) in self._li:
            x, y = (randint(1, 49)*10), (randint(1, 49)*10)
        self._foodrec = self._can.create_rectangle(x, y, x+10, y+10, fill='red')
        return x, y, self._foodrec

    def UpdateDir(self, event) :
        if not(self.dirflag) :
            if (self.xsp == 10 or self.xsp == -10) and event.char == 'w' :
                self.xsp, self.ysp = 0, -10
            elif (self.xsp == 10 or self.xsp == -10) and event.char == 's' :
                self.xsp, self.ysp = 0, 10
            elif (self.ysp == 10 or self.ysp == -10) and event.char == 'a' :
                self.xsp, self.ysp = -10, 0
            elif (self.ysp == 10 or self.ysp == -10) and event.char == 'd' :
                self.xsp, self.ysp = 10, 0
            self.dirflag = True

    def Yo(self, event):
        self.flag = not(self.flag) 
        self._can.focus_set()

def Conditional(condition, true, false) :
    return ( (true if condition else false) )