# напиши здесь код создания и управления картой
class Mapmanager():
    def __init__(self):
        self.model = 'block.egg'
        self.texture = 'block.png'
        self.colors = [(0, 1, 0.949, 1),
                      (0.102, 1, 0, 1),
                      (1, 0.816, 0, 1),
                      (1, 0.082, 0, 1)]
        self.start_new()

    def add_block(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.color = self.get_color(position[2])
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)

    def start_new(self):
        self.land = render.attachNewNode('Land')

    def loadLand(self, filename):
        self.clear()
        with open(filename) as file:
            y = 0
            for string in file:
                x = 0
                int_list = map(int, string.split())
                for number in int_list:
                    for cube in range(number + 1):
                        new_block = self.add_block((x, y, cube))
                    x += 1
                y += 1
        return x, y
                
    def clear(self):
        self.land.removeNode()
        self.start_new()

    def get_color(self, z):
        if z < len(self.colors):
            return self.colors[z]
        else: 
            return self.colors[-1]
            