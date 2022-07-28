class Node:
    def __init__(self, index, x, y, points_of_interest):
        self.index = index
        self.x = x
        self.y = y
        self.points_of_interest = points_of_interest

    def get_index(self):
        return self.index

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_num_points_of_interest(self):
        return len(self.points_of_interest)

    def get_points_of_interest(self):
        return self.points_of_interest
