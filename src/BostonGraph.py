from src.Graph import Graph
from src.Node import Node


class BostonGraph:
    """ A class which constructs a graph class which will represent the city of B
    """

    def __init__(self):
        self.bostonGraph = Graph()

        self.node0 = Node(0,
                          42.33774,
                          -71.09575,
                          ["Khoury College of Computer Science", "Northeastern University", "Museum of FineArt"])
        self.node1 = Node(1,
                          42.33844, -71.09731, ["Isabella Stewart  Gardner Museum", "Clemente Field", "Evans Way Park"])
        self.node2 = Node(2, 42.34074, -71.0998,
                          ["Simmons University", "Rose Garden", "Higginson Circle", "Clemente Field"])
        self.node3 = Node(3, 42.34269, -71.10322, ["Justine Mee Liff Park", "Roberto Clemente Park"])
        self.node4 = Node(4, 42.34328, -71.10259, ["Justine Mee Liff Park", "Roberto Clemente Park"])
        self.node5 = Node(5, 42.34891, -71.09686, ["Fenway Park"])
        self.node6 = Node(6, 42.34542, -71.09439, ["The Fenway Garden Society"])
        self.node7 = Node(7, 42.34699, -71.09248, ["Gatson Square Park", "Charlesgate Park"])
        self.node8 = Node(8, 42.34641, -71.09076, ["John Boyle O'Reilly Monument"])
        self.node9 = Node(9, 42.35085, -71.08947, ["Charles River Esplanade"])
        self.node10 = Node(10, 42.34931, -71.08871, [])
        self.node11 = Node(11, 42.34809, -71.08811, [])
        self.node12 = Node(12, 42.34731, -71.08769, ["Newcomb Square Park"])
        self.node13 = Node(13, 42.34285, -71.08504, ["Gately Square Park", "Christian Science Plaza"])
        self.node14 = Node(14, 42.34544, -71.08167, ["Prudential Center"])
        self.node15 = Node(15, 42.34057, -71.08172, ["Wellington Common Park", "William E. Carter Playground"])
        self.node16 = Node(16, 42.34317, -71.07848, ["Titus Park", "Harriet  Tubman Memorial", "Union Church"])
        self.node17 = Node(17, 42.3393, -71.08039, [])
        self.node18 = Node(18, 42.34131, -71.0765, ["South End Boston Public Library", "South End Library Park"])
        self.node19 = Node(19, 42.33735, -71.07798, ["Chester Park", "West SpringField Garden"])
        self.node20 = Node(20, 42.3396, -71.07449, ["BlackStone square Park"])

        self.node21 = Node(21, 42.3365, -71.07697, [])
        self.node22 = Node(22, 42.33887, -71.07354, ["Saint Helenas Park", "Franklin Square Park"])
        self.node23 = Node(23, 42.33498, -71.07509, [])
        self.node24 = Node(24, 42.33748, -71.07193, [])
        self.node25 = Node(25, 42.34015, -71.06865, [])
        self.node26 = Node(26, 42.34083, -71.07067,
                           ["Puerto Rican Veterans Memorial ", "Monsignor Reynolds playground"])
        self.node27 = Node(27, 42.34129, -71.07202, ["Unity Tower Garden"])
        self.node28 = Node(28, 42.34282, -71.07376, [""])
        self.node29 = Node(29, 42.34581, -71.07521, ["Childe Hassam Park"])
        self.node30 = Node(30, 42.3483, -71.07638, [])
        self.node31 = Node(31, 42.34928, -71.0769, ["Boston Public Library", "Trinity Church", "Copley Square"])
        self.node32 = Node(32, 42.35008, -71.07734,
                           ["Boston Public Library", "Trinity Church", "Copley Square", "John Singleton Copley Statue"])
        self.node33 = Node(33, 42.35087, -71.07772, [])
        self.node34 = Node(34, 42.35205, -71.07825,
                           ["William Lloyd Garrison Memorial Statue", "Boston Vendome Hotel Fire Memorial"])
        self.node35 = Node(35, 42.35365, -71.07908, ["Charles River Esplanade", "Storrow Lagoon"])
        self.node36 = Node(36, 42.3548, -71.07478, ["Charles River Esplanade"])

        self.node37 = Node(37, 42.353, -71.07391, ["Alexander Hamilton Statue"])
        self.node38 = Node(38, 42.35204, -71.07346, ["Church of the Covenant"])
        self.node39 = Node(39, 42.35122, -71.07308, [])
        self.node40 = Node(40, 42.34952, -71.07223, ["John Hancock Hall"])
        self.node41 = Node(41, 42.34865, -71.07179, ["Isabella Street Park"])
        self.node42 = Node(42, 42.3548, -71.07478,
                           ["Charles River Esplanade", "Boston Public Garden", "George Robert White Memorial"])
        self.node43 = Node(43, 42.35365, -71.07157,
                           ["Alexander Hamilton Statue", "George Washington Statue", "Boston Public Garden"])
        self.node44 = Node(44, 42.35268, -71.0711, ["Boston Public Garden", "Garden of Remembrance 9 / 11 Memorial"])
        self.node45 = Node(45, 42.35189, -71.0707,
                           ["Boston Public Garden", "Charles Sumner Statue", "Arlington Street Church"])
        self.node46 = Node(46, 42.35014, -71.06991, ["Statler Park"])
        self.node47 = Node(47, 0, 0, ["Boston Public Garden", "Boston Common", "Make Way for Ducklings"])
        self.node48 = Node(48, 0, 0, ["Boston Public Garden", "Boston Common", "Wendell Phillips Statue",
                                      "Central Burying Ground", "Edgar Allan Poe Statue"])
        self.node49 = Node(49, 42.35094, -71.06687, [])
        self.node50 = Node(50, 42.34878, -71.06662, ["Eliot Norton Park", "Bay Village Neighborhood Park"])

        self.node51 = Node(51, 42.34749, -71.06861, ["Chandler/ Tremont Plaza"])
        self.node52 = Node(52, 42.34526, -71.06984, ["Lt. Jeremiah W. Sullivan Square", "Berkeley Community Garden"])
        self.node53 = Node(53, 42.34432, -71.06704, ["Berkeley Community Garden", "Peters Park"])
        self.node54 = Node(54, 42.34396, -71.06597, ["Peters Park"])
        self.node55 = Node(55, 42.34352, -71.06436, ["jersey Liquor"])
        self.node56 = Node(56, 42.34689, -71.06586, ["100 Shawmut", "C-Mart Super Market"])
        self.node57 = Node(57, 42.34661, -71.06459, ["Board of Registration of Cosmetology and Barbering"])
        self.node58 = Node(58, 42.34634, -71.06324, ["Ink Block"])
        self.node59 = Node(59, 42.34861, -71.06555, ["Eliot Norton Park"])
        self.node60 = Node(60, 42.3511, -71.06491, ["The Wilbur", "Boxing Club The Ring"])
        self.node61 = Node(61, 42.35093, -71.06304, ["Liuyishou Hotpot Boston"])
        self.node62 = Node(62, 42.35063, -71.06154, ["China Town Gate"])
        self.node63 = Node(63, 42.35016, -71.05974, ["One Greenway Park"])
        self.node64 = Node(64, 42.3524, -71.06455, ["Boston Commons", "Emerson Colonial Theatre"])
        self.node65 = Node(65, 42.35238, -71.06261, ["China Trade Center"])
        self.node66 = Node(66, 42.3525, -71.06141, ["Phillips Square"])
        self.node67 = Node(67, 42.35235, -71.05813, ["State Street Financial Center"])
        self.node68 = Node(68, 42.35411, -71.05413, ["Rose Fitzgerald Kennedy Greenway"])
        self.node69 = Node(69, 42.3595, -71.05243, ["Boston Harbor Islands Pavilion"])
        self.node70 = Node(70, 42.35888, -71.05682,
                           ["Old State House", "Boston Massacre Site", "State Room: A Longwood Venue"])
        self.node71 = Node(71, 42.35931, -71.05963, ["Shawmut Peninsula"])
        self.node72 = Node(72, 42.35829, -71.06156, ["Boston Athenaeum"])
        self.node73 = Node(73, 42.36054, -71.05316,
                           ["Armenian Heritage Park", "The Greenway Carousel", "Boston Harbor Islands Pavilion"])
        self.node74 = Node(74, 42.36369, -71.05846, ["Haymarket"])
        self.node75 = Node(75, 42.36278, -71.05747, ["Rose Kennedy Greenway"])
        self.node76 = Node(76, 42.36218, -71.0565, ["Boston Public Market", "Corner Stalk Farm"])
        self.node77 = Node(77, 42.36715, -71.05253, [])
        self.node78 = Node(78, 42.3677, -71.05405,
                           ["Mirabella sprinklers", "Great Molasses Flood Plaque", "The Secret Boston Treasure Site"])
        self.node79 = Node(79, 42.3669, -71.05856, [])
        self.node80 = Node(80, 42.36409, -71.06343, ["The Boxer Boston"])

        self.node81 = Node(81, 42.36128, -71.06384, ["Old West Church"])
        self.node82 = Node(82, 42.3612, -71.06291, ["Cardinal Cushing Memorial Park"])
        self.node83 = Node(83, 42.36644, -71.06768, ["The Boston Synagogue", "Nashua Street Park"])
        self.node84 = Node(84, 42.36076, -71.07088, ["Hamilton Coolidge Square"])

        # Add Edges between the nodes:
        self.bostonGraph.add_edge(0, 1, 490)
        self.bostonGraph.add_edge(0, 13, 3440)
        self.bostonGraph.add_edge(1, 3, 2255)
        self.bostonGraph.add_edge(1, 8, 3725)
        self.bostonGraph.add_edge(2, 6, 2655)
        self.bostonGraph.add_edge(2, 4, 1195)
        self.bostonGraph.add_edge(3, 4, 275)
        self.bostonGraph.add_edge(4, 6, 2345)
        self.bostonGraph.add_edge(4, 5, 2570)
        self.bostonGraph.add_edge(5, 9, 2110)
        self.bostonGraph.add_edge(6, 7, 775)
        self.bostonGraph.add_edge(7, 8, 525)
        self.bostonGraph.add_edge(8, 12, 890)
        self.bostonGraph.add_edge(9, 10, 600)
        self.bostonGraph.add_edge(9, 35, 2360)
        self.bostonGraph.add_edge(10, 11, 475)
        self.bostonGraph.add_edge(10, 34, 2360)
        self.bostonGraph.add_edge(11, 12, 305)
        self.bostonGraph.add_edge(11, 33, 2355)
        self.bostonGraph.add_edge(12, 13, 1800)
        self.bostonGraph.add_edge(12, 32, 2355)
        self.bostonGraph.add_edge(13, 15, 1225)
        self.bostonGraph.add_edge(13, 14, 1310)
        self.bostonGraph.add_edge(14, 31, 1200)
        self.bostonGraph.add_edge(14, 16, 1195)
        self.bostonGraph.add_edge(15, 17, 585)
        self.bostonGraph.add_edge(15, 16, 1290)
        self.bostonGraph.add_edge(16, 29, 1305)
        self.bostonGraph.add_edge(16, 18, 835)
        self.bostonGraph.add_edge(17, 19, 965)
        self.bostonGraph.add_edge(17, 18, 1280)
        self.bostonGraph.add_edge(18, 28, 925)
        self.bostonGraph.add_edge(18, 20, 830)
        self.bostonGraph.add_edge(19, 21, 415)
        self.bostonGraph.add_edge(19, 20, 1255)
        self.bostonGraph.add_edge(20, 22, 365)
        self.bostonGraph.add_edge(20, 27, 910)
        self.bostonGraph.add_edge(21, 23, 755)
        self.bostonGraph.add_edge(21, 22, 1270)
        self.bostonGraph.add_edge(22, 24, 665)
        self.bostonGraph.add_edge(22, 26, 1055)
        self.bostonGraph.add_edge(23, 24, 1250)
        self.bostonGraph.add_edge(24, 25, 1315)
        self.bostonGraph.add_edge(25, 55, 1690)
        self.bostonGraph.add_edge(25, 26, 560)
        self.bostonGraph.add_edge(26, 27, 400)
        self.bostonGraph.add_edge(26, 54, 1745)
        self.bostonGraph.add_edge(27, 28, 730)
        self.bostonGraph.add_edge(27, 53, 1740)
        self.bostonGraph.add_edge(28, 29, 1160)
        self.bostonGraph.add_edge(28, 52, 1385)

        self.nodes_list = [
            self.node0,
            self.node1,
            self.node2,
            self.node3,
            self.node4,
            self.node5,
            self.node6,
            self.node7,
            self.node8,
            self.node9,
            self.node10,
            self.node11,
            self.node12,
            self.node13,
            self.node14,
            self.node15,
            self.node16,
            self.node17,
            self.node18,
            self.node19,
            self.node20,
            self.node21,
            self.node22,
            self.node23,
            self.node24,
            self.node25,
            self.node26,
            self.node27,
            self.node28,
            self.node29,
            self.node30,
            self.node31,
            self.node32,
            self.node33,
            self.node34,
            self.node35,
            self.node36,
            self.node37,
            self.node38,
            self.node39,
            self.node40,
            self.node41,
            self.node42,
            self.node43,
            self.node44,
            self.node45,
            self.node46,
            self.node47,
            self.node48,
            self.node49,
            self.node50,
            self.node51,
            self.node52,
            self.node53,
            self.node54,
            self.node55,
            self.node56,
            self.node57,
            self.node58,
            self.node59,
            self.node60,
            self.node61,
            self.node62,
            self.node63,
            self.node64,
            self.node65,
            self.node66,
            self.node67,
            self.node68,
            self.node69,
            self.node70,
            self.node71,
            self.node72,
            self.node73,
            self.node74,
            self.node75,
            self.node76,
            self.node77,
            self.node78,
            self.node79,
            self.node80,
            self.node81,
            self.node82,
            self.node83,
            self.node84,
        ]

        # Load Nodes
        for node in self.nodes_list:
            self.bostonGraph.add_node(node)

    """ Get the constructed graph of Boston
    """

    def get_boston_map(self) -> Graph:
        return self.bostonGraph
