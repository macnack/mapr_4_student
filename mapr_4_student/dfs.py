import rclpy
import time
from mapr_4_student.grid_map import GridMap
import queue


class DFS(GridMap):
    def __init__(self):
        super(DFS, self).__init__()
        # IF YOU NEED SOME ADDITIONAL FIELDS IN DFS OBJECT YOU CAN INITIALIZE
        # THEM HERE

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
        node_stack = queue.LifoQueue()
        visited_nodes = set()
        node_stack.put(self.start)
        action = [self.down(), self.left(), self.up(), self.right()]
        while not node_stack.empty():
            # odczytaj
            cur_n = node_stack.queue[-1]
            # zaznacz jako odwiedzony
            visited_nodes.add(cur_n)
            self.map.data[cur_n[0] + cur_n[1] * self.map.info.width] = 50

            # Sprawdź, czy ten wierzchołek jest poszukiwanym wierzchołkiem
            # końcowym
            if self.find_goal(cur_n):
                break
            # Oblicz sąsiadów
            neighbors = [(cur_n[0] + u[0], cur_n[1] + u[1]) for u in action]
            for next_n in neighbors:
                # sprawdz spelnienie warunkow
                if self.is_valid(next_n) and \
                        next_n not in visited_nodes:
                    if self.map.data[next_n[0] + next_n[1]
                                     * self.map.info.width] < 50:
                        node_stack.put(next_n)
                        break

            # jesli brak sąsiadów
            if node_stack.queue[-1] == cur_n:
                node_stack.get()

            self.publish_visited()


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
