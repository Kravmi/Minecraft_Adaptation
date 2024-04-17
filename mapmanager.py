# напиши здесь код создания и управления картой
class Mapmanager():
    def __init__(self):
        self.model = 'block.egg'
        self.texture = 'block.png'
        self.color = ((0, 0.153, 0, 1))
        self.start_new()
        self.add_block((0, 10, 0))
        self.add_block((20, 40, -10))

    def add_block(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)

    def start_new(self):
        self.land = render.attachNewNode('Land')