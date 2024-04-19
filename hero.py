# напиши свой код здесь
class Hero():
    def __init__(self, pos, land):
        self.land = land
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(0.102, 0, 1, 1)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.acceptEvents()
        self.mode = True

    def cameraBind(self):
        self.camera_on = True
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)

    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2] -3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.camera_on = False

    def acceptEvents(self):
        base.accept('v', self.changeView)
        base.accept('d', self.turn_right)
        base.accept('d' + '-repeat', self.turn_right)
        base.accept('a', self.turn_left)
        base.accept('a' + '-repeat', self.turn_left)

    def changeView(self):
        if self.camera_on == True:
            self.cameraUp()
        else:
            self.cameraBind()
        
    def turn_right(self):
        self.hero.setH((self.hero.getH() -5) % 360)

    def turn_left(self):
        self.hero.setH((self.hero.getH() +5) % 360)

    # определяет движение игрока в режиме наблюдателя
    def just_move(self, angle):
        pass

    # Определяет движение игрока в основном режиме
    def try_move(self, angle):
        pass

    # определяет вид движения 
    # в зависимости от свойства self.mode
    # если равно true то вызываем just_move
    # иначе try_move
    def move_to(self, angle):
        pass

    def look_at(self, angle):
        from_x = round(self.hero.getX())
        from_z = round(self.hero.getZ())
        from_y = round(self.hero.getY())
        dx, dy = self.hero.check_dir(self, angle)
        return from_x+dx, from_y+dy, from_z

    def check_dir(self, angle):
        pass