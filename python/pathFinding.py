import time
from typing import List, Tuple
import cpp_pathfinder

# test file

class PathNotFoundError(Exception):
    pass


class PathfindingEngine:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = cpp_pathfinder.Grid(width, height)

    def add_obstacle(self, x: int, y: int) -> None:
        self.grid.set_obstacle(x, y, True)

    def find_path(self, start: Tuple[int, int], target: Tuple[int, int]) -> List[Tuple[int, int]]:
        path = cpp_pathfinder.PathFinder.find_path(
            self.grid,
            start[0], start[1],
            target[0], target[1]
        )

        if not path:
            raise PathNotFoundError(f"No valid path found from {start} to {target}.")

        return path

if __name__ == "__main__":
    engine = PathfindingEngine(20, 20)

    for y in range(20):
        if y != 15:
            engine.add_obstacle(10, y)

    # Measure execution time
    start_time = time.perf_counter()
    try:
        found_path = engine.find_path((0, 0), (19, 19))
        end_time = time.perf_counter()

        elapsed_ms = (end_time - start_time) * 1000
        print(f"Path found with {len(found_path)} steps.")
        print(f"Time taken: {elapsed_ms:.4f} ms")
    except PathNotFoundError as e:
        print(e)