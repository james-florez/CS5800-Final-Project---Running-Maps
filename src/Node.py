class Node:
    def __init__(self, index, x, y, num_points_of_interest, descriptions):
        self.index = index
        self.x = x
        self.y = y
        self.numPointsOfInterest = num_points_of_interest
        self.descriptions = descriptions

    def get_index(self):
        return self.index

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_num_points_of_interest(self):
        return self.numPointsOfInterest

    def get_descriptions(self):
        return self.descriptions
