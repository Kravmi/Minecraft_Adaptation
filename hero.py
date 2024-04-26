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
        base.accept('arrow_left', self.left)
        base.accept('arrow_left' + '-repeat', self.left)
        base.accept('arrow_right', self.right)
        base.accept('arrow_right' + '-repeat', self.right)
        base.accept('arrow_up', self.forward)
        base.accept('arrow_up' + '-repeat', self.forward)
        base.accept('arrow_down', self.back)
        base.accept('arrow_down' + '-repeat', self.back)
        base.accept('space', self.up)
        base.accept('space' + '-repeat', self.up)
        base.accept('control', self.down)
        base.accept('control' + '-repeat', self.down)
        base.accept('g', self.changeMode)
        base.accept('g' + '-repeat', self.changeMode)
        base.accept('1', self.destroy)
        base.accept('2', self.build)
        base.accept('control-s', self.land.save_map)
        base.accept('control-u', self.land.load_map)

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
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    # Определяет движение игрока в основном режиме
    def try_move(self, angle):
        pos = self.look_at(angle)
        if self.land.isEmpty(pos):
            pos = self.land.findHighestEmpty(pos)
            self.hero.setPos(pos)
        else:
            pos = pos[0], pos[1], pos[2] + 1
            if self.land.isEmpty(pos):
               self.hero.setPos(pos) 

    # определяет вид движения 
    # в зависимости от свойства self.mode
    # если равно true то вызываем just_move
    # иначе try_move
    def move_to(self, angle):
        if self.mode == True:
            self.just_move(angle)
        else:
            self.try_move(angle)

    def look_at(self, angle):
        from_x = round(self.hero.getX())
        from_z = round(self.hero.getZ())
        from_y = round(self.hero.getY())
        dx, dy = self.check_dir(angle)
        return from_x+dx, from_y+dy, from_z

    def check_dir(self, angle):
        if angle >= 0 and angle <= 20:
            return 0, -1
        elif angle > 20 and angle <= 65:
            return 1, -1
        elif angle > 65 and angle <= 110:
            return 1, 0
        elif angle > 110 and angle <= 155:
            return 1, 1
        elif angle > 155 and angle <= 200:
            return 0, 1
        elif angle > 200 and angle <= 245:
            return -1, 1
        elif angle > 245 and angle <= 290:
            return -1, 0
        elif angle > 290 and angle <= 335:
            return -1, -1
        else: 
            return 0, -1

    def back(self):
        angle = (self.hero.getH()+180) % 360
        self.move_to(angle)

    def forward(self):
        angle = (self.hero.getH()+0) % 360
        self.move_to(angle)
        
    def left(self):
        angle = (self.hero.getH() + 90) % 360
        self.move_to(angle)

    def right(self):
        angle = (self.hero.getH()+270) % 360
        self.move_to(angle)

    def up(self):
        if self.mode == True:
            self.hero.setZ(self.hero.getZ() + 1)

    def down(self):
        if self.mode == True and self.hero.getZ() > 1:
            self.hero.setZ(self.hero.getZ() - 1)

    def changeMode(self):
        if self.mode == True:
            self.mode = False
        else:
            self.mode = True

    def build(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.add_block(pos)
        else:
            self.land.build_block(pos)

    def destroy(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.del_block(pos)
        else:
            self.land.del_block_from(pos)