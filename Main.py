from os import system
from random import randint as ran

x, y = 7, 3 * round(21 / 3)


class ship:
    def __init__(self, length, First_x, Final_x, First_y, Final_y):
        self.length = length  #sounds pointless but is important
        self.x, self.y = [], []
        for i in range(self.length):
            self.x.append(First_x + ((Final_x - First_x) / self.length) * i)
            self.y.append(First_y + ((Final_y - First_y) / self.length) * i)

    def details(self):
        coords = []
        for i in self.x:
            coords.append([i])
        for i in range(len(self.y)):
            coords[i].append(self.y[i])
        return coords


class grid:
    def __init__(self, x, y, shots, owned, owner):
        self.x = x
        self.y = 3 * round(y / 3)
        self.shots, self.owned, self.owner = shots, owned, owner
        self.shot()
        if self.owner == 0:
            self.draw()
        else:
            self.edraw()

    def shot(self):
        print(self.owned, "shot1")
        for i in range(len(self.shots)):
            for s in range(len(self.shots[i])):
                self.shots[i][s][1] = round((self.shots[i][s][1] * 3) / 3)
        for i in range(len(self.owned)):
            for s in range(len(self.owned[i])):
                self.owned[i][s][1] = int(round((self.owned[i][s][1] * 3) / 3))
                self.owned[i][s][0] = int(self.owned[i][s][0])
        print(self.owned, "shot2")

    def draw(self):
        display, column = [], "|"
        for i in range(self.y):
            for s in range(self.x):
                if (i + 1) % 3 == 0 and (i + 1) != self.y:
                    HSM = "___|"  #___|
                elif (i + 1) % 3 == 1:
                    HSM = "   |"  #   |
                else:
                    for y in self.owned:
                        if [s, i] in y:
                            HSM = " ■ |"
                        elif [s, i] in y:
                            HSM = " ☼ |"
                        else:
                            HSM = "   |"
                column += HSM
            display.append(column)
            column = "|"
        for i in display:
            print(i)

    def edraw(self):
        display, column = [], "|"
        for i in range(self.y):
            for s in range(self.x):
                if (i + 1) % 3 == 0 and (i + 1) != self.y:
                    HSM = "___|"  #___|
                elif (i + 1) % 3 == 1:
                    HSM = "   |"  #   |
                else:
                    if [s, i] in self.shots:
                        HSM = " @ |"  # @ |
                    elif [s, i] in self.shots:
                        HSM = " + |"  # + |
                    else:
                        HSM = "   |"
                column += HSM
            display.append(column)
            column = "|"
        for i in display:
            print(i)


class fleet:
    def __init__(self, number, lengths, owner, final, x, y):
        self.number, self.lengths, self.owner, self.final = number, lengths, owner, final  #stuff for the fleet
        self.x, self.y = x, y  #grid size
        self.build()  #remove later, just a test for now

    def details(self):
        return self.final, self.owner

    def build(self):
        Ship = []
        while self.number > 0:
            current_ship = self.lengths[self.number - 1]
            up_down = ran(0, 1)
            fail = True
            if up_down == 0:
                while fail == True:
                    while True:
                        x, y = ran(0, self.x), ran(0, self.y)
                        y = 3 * round(y / 3) +1
                        if (x + current_ship > self.x) != True:
                            break
                    Ship = (ship(current_ship, x, x + current_ship, y,
                                 y).details())
                    if len(self.final) == 0:
                        fail = False
                    else:
                        for i in self.final:
                            for s in i:
                                if s in Ship:
                                    fail = True
                                    break
                                else:
                                    fail = False
                            if fail == True:
                                break
                self.final.append(Ship)

            elif up_down == 1:
                while fail == True:
                    while True:
                        x, y = ran(0, self.x), ran(0, self.y)
                        y = 3 * round(y / 3) +1
                        if (y + (current_ship * 3) > self.y) != True:
                            break
                    Ship = (ship(current_ship, x, x, y,
                                 y + current_ship).details())
                    if len(self.final) == 0:
                        fail = False
                    else:
                        for i in self.final:
                            for s in i:
                                if s in Ship:
                                    fail = True
                                    break
                                else:
                                    fail = False
                            if fail == True:
                                break
                for i in range(len(Ship)):
                    Ship[i][1] = Ship[i][1] + (i * 2)
                self.final.append(Ship)
            self.number -= 1
            if self.number == 0:
                break


player_fleet = fleet(2, [3, 3], 0, [], x, y)
f = player_fleet.details()
p1_grid = grid(x, y, [], f[0], f[1])

#system("clear")
#p2_grid = grid(
#    x, y,
#    [[2, 4, False], [5, 3, True], [3, 5, True], [3, 4, True], [3, 6, True]],
#    [])  #[[2,2,True],[6,2,False],[5,2,False],[4,2,False],[3,2,False]])
#print()
#p1_grid = grid(
#    x,y,[  #[[2,4,False],[5,3,True],[3,5,True],[3,7,True],[3,6,True]
#    ],[[2, 2, True], [6, 2, False], [5, 2, False], [4, 2, False], [3, 2, False]])

