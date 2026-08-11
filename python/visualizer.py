import sys
import pygame
import cpp_pathfinder

# Constants
GRID_SIZE = 25
TILE_SIZE = 24
GAP = 1
WINDOW_SIZE = GRID_SIZE * (TILE_SIZE + GAP)
HEADER_HEIGHT = 40  # Extra space at the top for UI text

# Colors (RGB)
WHITE = (240, 240, 240)
BLACK = (30, 30, 30)
GREEN = (46, 204, 113)
RED = (231, 76, 60)
BLUE = (52, 152, 219)
GRAY = (180, 180, 180)


def main():
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + HEADER_HEIGHT))
    pygame.display.set_caption("C++ A* Pathfinder Visualizer")

    font = pygame.font.SysFont("Arial", 18)

    grid = cpp_pathfinder.Grid(GRID_SIZE, GRID_SIZE)

    start = (2, 2) # Cords
    target = (GRID_SIZE - 3, GRID_SIZE - 3)
    obstacles = set()

    running = True
    drawing_wall = False
    erasing_wall = False

    while running:
        raw_path = cpp_pathfinder.PathFinder.find_path(
            grid, start[0], start[1], target[0], target[1]
        )
        path = set(raw_path)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                y_grid = y - HEADER_HEIGHT
                col = x // (TILE_SIZE + GAP)
                row = y_grid // (TILE_SIZE + GAP)

                if 0 <= col < GRID_SIZE and 0 <= row < GRID_SIZE:
                    if (col, row) != start and (col, row) != target:
                        if event.button == 1:
                            drawing_wall = True
                            grid.set_obstacle(col, row, True)
                            obstacles.add((col, row))
                        elif event.button == 3:
                            erasing_wall = True
                            grid.set_obstacle(col, row, False)
                            obstacles.discard((col, row))

            elif event.type == pygame.MOUSEBUTTONUP:
                drawing_wall = False
                erasing_wall = False

            elif event.type == pygame.MOUSEMOTION:
                x, y = pygame.mouse.get_pos()
                y_grid = y - HEADER_HEIGHT
                col = x // (TILE_SIZE + GAP)
                row = y_grid // (TILE_SIZE + GAP)

                if 0 <= col < GRID_SIZE and 0 <= row < GRID_SIZE:
                    if (col, row) != start and (col, row) != target:
                        if drawing_wall:
                            grid.set_obstacle(col, row, True)
                            obstacles.add((col, row))
                        elif erasing_wall:
                            grid.set_obstacle(col, row, False)
                            obstacles.discard((col, row))

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    for ox, oy in list(obstacles):
                        grid.set_obstacle(ox, oy, False)
                    obstacles.clear()

        screen.fill(BLACK)

        path_length = len(raw_path)
        status_text = (
            f"Path Length: {path_length} steps"
            if path_length > 0
            else "No Path Available"
        )
        text_surface = font.render(
            f"{status_text} | Left-Click: Wall | Right-Click: Erase | C: Clear",
            True,
            WHITE,
        )
        screen.blit(text_surface, (10, 10))

        # Render Grid below header
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                color = WHITE
                pos = (col, row)

                if pos in obstacles:
                    color = BLACK
                elif pos == start:
                    color = GREEN
                elif pos == target:
                    color = RED
                elif pos in path:
                    color = BLUE

                pygame.draw.rect(
                    screen,
                    color,
                    (
                        col * (TILE_SIZE + GAP),
                        row * (TILE_SIZE + GAP) + HEADER_HEIGHT,
                        TILE_SIZE,
                        TILE_SIZE,
                    ),
                )

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()