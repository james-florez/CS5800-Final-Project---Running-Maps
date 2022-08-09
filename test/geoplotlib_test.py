import numpy
import pyglet
import geoplotlib
from geoplotlib.utils import read_csv
import matplotlib

dot = False
if dot:
    data = read_csv("../data/boston_test.csv")
    geoplotlib.dot(data, point_size=3)
else:
    # dict = {'src_lat': [],
    #  'src_lon': [],
    #  'dest_lat': [],
    #  'dest_lat': [],
    #  }
    data = read_csv("../data/boston_test2.csv")
    geoplotlib.graph(data,
                     src_lat='src_lat',
                     src_lon='src_lon',
                     dest_lat='dest_lat',
                     dest_lon='dest_lon',
                     color='hot_r',
                     alpha=100,
                     linewidth=20)

geoplotlib.show()
