class Node:
    """A class used to represent a Node (street intersection) in a Graph (city map).

    Attributes:
        index (str): a number used to reference the Node
        latitude (float): latitude of the street intersection
        longitude (float): longitude of the street intersection
    """

    def __init__(self, index: int, latitude: float, longitude: float, points_of_interest: [str]):
        """Initializes a Node object.

        Args:
            index (str): a number used to reference the Node
            latitude (float): latitude of the street intersection
            longitude (float): longitude of the street intersection
            points_of_interest ([str]): names of the points of interest visible from this street intersection
        """

        self.index = index
        self.latitude = latitude
        self.longitude = longitude
        self.points_of_interest = points_of_interest

    def get_index(self) -> int:
        """Gets the index of the Node.

        Returns:
            int: the index value
        """
        return self.index

    def get_latitude(self) -> float:
        """Gets the latitude of the street intersection.

        Returns:
            float: the latitude value
        """
        return self.latitude

    def get_longitude(self) -> float:
        """Gets the longitude of the street intersection.

        Returns:
            float: the longitude value
        """
        return self.longitude

    def get_num_points_of_interest(self) -> int:
        """Gets the number of the points of interest visible from the street intersection.

        Returns:
            int: number of the points of interest
        """
        return len(self.points_of_interest)

    def get_points_of_interest(self) -> [str]:
        """Gets the names of the points of interest visible from the street intersection.

        Returns:
            [str]: names of the points of interest
        """
        return self.points_of_interest
