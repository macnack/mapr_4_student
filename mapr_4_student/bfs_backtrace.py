import rclpy
import time
from mapr_4_student.grid_map import GridMap
import numpy as np


class BFS(GridMap):
    def __init__(self):
        super(BFS, self).__init__()
        ###  IF YOU NEED SOME ADDITIONAL FILEDS IN BFS OBJECT YOU CAN INITIALIZED TEHM HERE

    def search(self):
        ### YOUR CODE GOES BELOW
        #
        #
        #
        #
        # IMPLEMENT BREADTH FIRST SEARCH WITH BACKTRACE:
        # * save your search in self.map.data
        # * use self.publish_visited() to publish the map every time you visited a new cell
        # * let 100 represent walls, 50 visited cells (useful for visualization)
        # * save the path to the goal fund by the algorithm to list of tuples: [(x_n, y_n), ..., (x_2, y_2), (x_1, y_1)]
        # * use self.publish_path(path) to publish the path at the very end
        # * start point is in self.start
        # * end point is in self.end
        #
        #
        ### YOUR CODE GOES ABOVE
        visited = set()
        q = queue.Queue()
        q.put(self.start)
        parent = {}
        for x in range(self.map.info.height):
            for y in range(self.map.info.width):
                parent[(x,y)] = None
            
        action = [ (0,-1), (-1,0), (0,1), (1,0)]
        while not q.empty():
            cur_n = q.get()
            visited.add(cur_n)
            self.map.data[cur_n[0] + cur_n[1] * self.map.info.width] = 50
            self.get_logger().info(f"cur_n:={cur_n}")
            if cur_n == self.end:
                break

            for u in action:
                next_n = (cur_n[0]+u[0], cur_n[1]+u[1])
                self.get_logger().info(f"next_n:={next_n}")
                if next_n not in visited:
                    if self.map.data[next_n[0] + next_n[1] * self.map.info.width] < 50:
                        if next_n not in list(q.queue):
                            parent[next_n] = cur_n
                            q.put(next_n)
            self.publish_visited()
        
        path = []
        while cur_n != None:
            path.append(cur_n)
            cur_n = parent[cur_n]
        self.publish_path(reversed(path))


def main(args=None):
    rclpy.init(args=args)
    bfs = BFS()
    while not bfs.data_received():
        bfs.get_logger().info("Waiting for data...")
        rclpy.spin_once(bfs)
        time.sleep(0.5)

    bfs.get_logger().info("Start graph searching!")
    bfs.publish_visited()
    time.sleep(1)
    bfs.search()

if __name__ == '__main__':
    main()
