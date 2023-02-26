import pickle

class Hero():
    def __init__(self, pos, land):
        self.land = land
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(1, 0.5, 0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()
        self.mode = "survival"
    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.setP(270)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 15)
    def turn_left(self):
        a = self.hero.getH()
        a += 5
        self.hero.setH(a%360)
    def turn_right(self):
        a = self.hero.getH()
        a -= 5
        self.hero.setH(a%360)

    def survival_move(self, angle):
        next_pos = self.look_at(angle)
        if self.land.isEmpty(next_pos):
            next_pos = self.land.highestEmpty(next_pos)
            self.hero.setPos(next_pos)
        else:
            next_pos = (next_pos[0], next_pos[1], next_pos[2] + 1)
            if self.land.isEmpty(next_pos):
                self.hero.setPos(next_pos)


    def forward(self):
        angle = self.hero.getH()%360
        if self.mode == "survival":
            self.survival_move(angle)
        else:
            self.hero.setPos(self.look_at(angle))
    def back(self):
        angle = (self.hero.getH() + 180) % 360
        self.survival_move(angle)
    def right(self):
        angle = (self.hero.getH()+ 270) % 360
        self.survival_move(angle)
    def left(self):
        angle = (self.hero.getH() + 90) % 360
        self.survival_move(angle)
    def up(self):
        self.setZ(self.getZ()+1)
    def down(self):
        self.setZ(self.getZ()-1)


    def look_at(self, angle):
        x1 = self.hero.getX()
        y1 = self.hero.getY()
        z1 = self.hero.getZ()

        dx, dy = self.check_dir(angle)

        x2 = x1 + dx
        y2 = y1 + dy
        return int(x2), int(y2), int(z1)

    def check_dir(self, angle):
        print(angle)
        if angle >= 0 and angle <= 20:
           return (0, -1)
        elif angle <= 65:
            return (1, -1)
        elif angle <= 110:
            return (1, 0)
        elif angle <= 155:
            return (1, 1)
        elif angle <= 200:
            return (0, 1)
        elif angle <= 245:
            return (-1, 1)
        elif angle <= 290:
            return (-1, 0)
        elif angle <= 335:
            return (-1, -1)
        else:
            return (0, -1)

    def build(self):
        angle = self.hero.getH()%360
        position = self.look_at(angle)
        self.land.addBlock(position)
    def destroi(self):
        angle = self.hero.getH()%360
        position = self.look_at(angle)
        self.land.destroi_block(position)



    def creativ(self):
        self.mode = "creative"
    def surv(self):
        self.mode = "survival"

    def save(self):
        all_blocks = self.land.getAllBlocks()
        with open("map.dat", "wb") as file:
            pickle.dump(len(all_blocks), file)
            for i in all_blocks:
                x, y, z = i.getPos()
                x = int(x)
                y = int(y)
                z = int(z)
                position = (x,y,z)
                pickle.dump(position, file)


    def accept_events(self):
        base.accept('d', self.turn_right)
        base.accept('a', self.turn_left)
        base.accept('d' + '-repeat', self.turn_right)
        base.accept('a' + '-repeat', self.turn_left)
        base.accept('w', self.forward)
        base.accept('w' + '-repeat', self.forward)
        base.accept('s', self.back)
        base.accept('s' + '-repeat', self.back)
        base.accept('e', self.right)
        base.accept('e' + '-repeat', self.right)
        base.accept('q', self.left)
        base.accept('q' + '-repeat', self.left)
        base.accept('1', self.creativ)
        base.accept('2', self.surv)
        base.accept('f', self.build)
        base.accept('r', self.destroi)
        base.accept('m', self.save)

