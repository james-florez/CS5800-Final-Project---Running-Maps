class Node:
    """This class represents a Node in a Graph."""

    def __init__(self, index: int, latitude: float, longitude: float, points_of_interest: [str]):
        self.index = index
        self.latitude = latitude
        self.longitude = longitude
        self.points_of_interest = points_of_interest

    def get_index(self) -> int:
        return self.index

    def get_latitude(self) -> float:
        return self.latitude

    def get_longitude(self) -> float:
        return self.longitude

    def get_num_points_of_interest(self) -> int:
        return len(self.points_of_interest)

    def get_points_of_interest(self) -> [str]:
        return self.points_of_interest
