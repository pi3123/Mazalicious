import pygame


class Tile:
    age =0
    width = 50
    color = (0, 0, 0)

    def __init__(self, age,width):
        self.age = age
        self.width = width

        if age == 0:
            self.color = (0, 0, 0)
        elif age >= 1:
            self.color = (120, 120, 120)

    def getstatus(self):
        if self.age > 0:
            return True
        else:
            return False

    def getRect(self, row, col):
        return [self.width * row, self.width * col, self.width, self.width]

    def getColor(self):
        return self.color

#    def getActiveNeighbors(self):

