import rclpy
import time
from mapr_4_student.grid_map import GridMap
import queue

class DFS(GridMap):
    def __init__(self):
        super(DFS, self).__init__()
        ###  IF YOU NEED SOME ADDITIONAL FIELDS IN DFS OBJECT YOU CAN INITIALIZE THEM HERE

    def search(self):
        q = queue.LifoQueue()
        visited = set()
        q.put(self.start)
        action = [(0,-1), (-1,0), (0,1), (1,0)]
        while not q.empty():
            #odczytaj
            cur_n = q.queue[-1]
            #zaznacz jako odwiedzony
            visited.add(cur_n)
            self.map.data[cur_n[0] + cur_n[1] * self.map.info.width] = 50

            #Sprawdź, czy ten wierzchołek jest poszukiwanym wierzchołkiem końcowym
            if cur_n == self.end:
                break
            else:
                for u in action:
                    next_n = (cur_n[0]+u[0], cur_n[1]+u[1])
                    if (next_n not in visited) and self.map.data[next_n[0] + next_n[1] * self.map.info.width] < 50:
                        q.put(next_n)
                        break
                    else:
                        if( u == action[-1]):
                            q.get()
            
            self.publish_visited()

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
