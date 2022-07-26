class Node:
    def __init__(self, index, x, y, numPOI, descriptions):
        self.index = index
        self.x = x
        self.y = y
        self.numPOI = numPOI
        self.descriptions = descriptions

    def get_index(self):
        return self.index

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_num_POI(self):
        return self.numPOI

    def get_descriptions(self):
        return self.descriptions
