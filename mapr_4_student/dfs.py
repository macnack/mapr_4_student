import rclpy
import time
from mapr_4_student.grid_map import GridMap


class DFS(GridMap):
    def __init__(self):
        super(DFS, self).__init__()
        ###  IF YOU NEED SOME ADDITIONAL FIELDS IN DFS OBJECT YOU CAN INITIALIZE THEM HERE

    def search(self):
        ### YOUR CODE GOES BELOW
        #
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
        pass  # DELETE THIS LINE IF THE CODE IS INSERTED


def main(args=None):
    rclpy.init(args=args)
    dfs = DFS()
    while not dfs.data_received():
        dfs.get_logger().info("Waiting for data...")
        rclpy.spin_once(dfs)
        time.sleep(0.5)

    dfs.get_logger().info("Start graph searching!")
    dfs.publish_visited()
    time.sleep(1)
    dfs.search()

if __name__ == '__main__':
    main()
