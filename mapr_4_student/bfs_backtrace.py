import rclpy
import time
from mapr_4_student.grid_map import GridMap
import numpy as np
import queue


class BFS(GridMap):
    def __init__(self):
        super(BFS, self).__init__()
        # IF YOU NEED SOME ADDITIONAL FILEDS IN BFS OBJECT YOU CAN INITIALIZED
        # TEHM HERE

    def down(self):
        return (0, -1)

    def up(self):
        return (0, 1)

    def left(self):
        return (-1, 0)

    def right(self):
        return (1, 0)

    def find_goal(self, node):
        return node == self.end

    def is_valid(self, pose):
        return pose[1] < self.map.info.width and pose[0] < self.map.info.height and \
            pose[0] > 0 and pose[1] > 0

    def search(self):
        visited = set()
        node_stack = queue.Queue()
        node_stack.put(self.start)
        parent = {}
        parent[self.start] = None
        action = [self.down(), self.left(), self.up(), self.right()]
        while not node_stack.empty():
            # Zabierz z kolejki element
            cur_n = node_stack.get()
            
            if cur_n in visited:
                continue
            # zaznacz jako odwiedzony
            visited.add(cur_n)
            self.map.data[cur_n[0] + cur_n[1] * self.map.info.width] = 50
            # sprawdz czy nie jest docelowym
            if self.find_goal(cur_n):
                break

            neighbors = [(cur_n[0] + u[0], cur_n[1] + u[1]) for u in action]
            for next_n in neighbors:
                if self.is_valid(next_n) and \
                        next_n not in visited:
                    if self.map.data[next_n[0] + next_n[1]
                                     * self.map.info.width] < 50:
                        parent[next_n] = cur_n
                        node_stack.put(next_n)
            self.publish_visited()

        path = []
        while cur_n is not None:
            path.append(cur_n)
            cur_n = parent[cur_n]
        self.publish_path(path)


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
