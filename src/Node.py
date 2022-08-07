class Node:
    def __init__(self, index, latitude, longitude, points_of_interest):
        self.index = index
        self.latitude = latitude
        self.longitude = longitude
        self.points_of_interest = points_of_interest

    def get_index(self):
        return self.index

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude

    def get_num_points_of_interest(self):
        return len(self.points_of_interest)

    def get_points_of_interest(self):
        return self.points_of_interest
