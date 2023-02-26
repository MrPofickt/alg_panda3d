# напиши здесь
import pickle
class Mapmanager():
    def __init__(self):
        self.model = "block"
        self.texture = "block.png"
        self.color = ((0.2, 8.3, 8.35, 1))
        self.startNew()

    def startNew(self):
        self.land = render.attachNewNode('Land')

    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)
        self.block.setTag("coord", str(position))

    def findBlocks(self, position):
        return self.land.findAllMatches('=coord='+str(position))

    def isEmpty(self, position):
        blocks = self.findBlocks(position)
        if blocks:
            return False
        else:
            return True

    def destroi_block(self, position):
        for i in self.findBlocks(position):
            i.removeNode()
    
    def getAllBlocks(self):
        return self.land.getChildren()

    
    def highestEmpty(self, position):
        x,y,z = position
        z = 1
        while not self.isEmpty((x,y,z)):
            z +=1
        return (x,y,z)

    def loadLand(self, filename):
        #with open(filename) as file:
        #    y = 0
        #    for line in file:
        #        x = 0
        #        line = line.split()
        #        for z in line:
        #            for i in range(int(z)+1):
        #                block = self.addBlock((x, y, i))
        #            x += 1
        #        y += 1
        with open("map.dat", "rb") as file:
            dlina = pickle.load(file)
            for i in range(dlina):
                position = pickle.load(file)
                self.addBlock(position)
