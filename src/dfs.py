#!/usr/bin/env python
import rospy as rp
from grid_map import GridMap


class DFS(GridMap):
    def __init__(self):
        super(DFS, self).__init__()
        ###  IF YOU NEED SOME ADDITIONAL FILEDS IN DFS OBJECT YOU CAN INITIALIZED TEHM HERE

    def search(self):
        ### YOUR CODE GOES BELOW
        #
        #
        # IMPLEMENT DEPTH FIRST SEARCH:
        # * save your search in self.map.data
        # * use self.publish_visited() to publish the map every time you visited a new cell
        # * let 100 represent walls, 50 visited cells (useful for visualization)
        # * start point is in self.start
        # * end point is in self.end
        #
        #
        ### YOUR CODE GOES ABOVE
        pass  # DELETE THIS LINE IF THE CODE INSERTED


if __name__ == '__main__':
    dfs = DFS()
    dfs.search()
