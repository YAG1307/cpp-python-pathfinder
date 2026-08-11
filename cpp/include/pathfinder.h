#ifndef PATHFINDER_H
#define PATHFINDER_H

#include <vector>
#include <cmath>

struct Node2D {
    int x;
    int y;
    bool isObstacle;

    double g;
    double h;

    int parentX;
    int parentY;

    Node2D(int gridX = 0, int gridY = 0, bool obstacle = false)
        : x(gridX),
          y(gridY),
          isObstacle(obstacle),
          g(1e9),
          h(0.0),
          parentX(-1),
          parentY(-1) {}

    double f() const {
        return g + h;
    }
};

inline double calculate_h(int x1, int y1, int x2, int y2) {
    double resultX = static_cast<double>(x2 - x1);
    double resultY = static_cast<double>(y2 - y1);
    return std::sqrt((resultX * resultX) + (resultY * resultY));
}

class Grid {
public:
    int width;
    int height;
    std::vector<std::vector<Node2D>> nodes;

    Grid(int w, int h) : width(w), height(h) {
        nodes.resize(height);
        for (int y = 0; y < height; y++) {
            nodes[y].resize(width);
            for (int x = 0; x < width; x++) {
                nodes[y][x] = Node2D(x, y, false);
            }
        }
    }

    void set_obstacle(int x, int y, bool obstacle) {
        if (isValid(x, y)) {
            nodes[y][x].isObstacle = obstacle;
        }
    }

    bool isValid(int x, int y) const {
        return (x >= 0 && x < width && y >= 0 && y < height);
    }

    std::vector<Node2D> get_neighbors(const Node2D& node) const {
        std::vector<Node2D> neighbors;
        int dx[] = {0, 0, -1, 1};
        int dy[] = {1, -1, 0, 0};

        for (int i = 0; i < 4; ++i) {
            int neighborX = node.x + dx[i];
            int neighborY = node.y + dy[i];

            if (isValid(neighborX, neighborY)) {
                const Node2D& neighbor = nodes[neighborY][neighborX];
                if (!neighbor.isObstacle) {
                    neighbors.push_back(neighbor);
                }
            }
        }
        return neighbors;
    }
};

class PathFinder {
public:
    static std::vector<std::pair<int, int>> find_path(Grid& grid, int startX, int startY, int targetX, int targetY);
};

#endif