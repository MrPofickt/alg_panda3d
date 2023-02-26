# напиши здесь код осн
from direct.showbase.ShowBase import ShowBase
from mapmanager import *
from hero import *

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        self.land.loadLand('map.dat')
        base.camLens.setFov(90)
        self.hero = Hero((15, 1, 1), self.land)
game = Game()
game.run()