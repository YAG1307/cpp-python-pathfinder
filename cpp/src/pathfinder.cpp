#include "pathfinder.h"
#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

struct CompareNode {
    bool operator()(const Node2D* a, const Node2D* b) const {
        return a->f() > b->f();
    }
};

std::vector<std::pair<int, int>> PathFinder::find_path(Grid& grid, int startX, int startY, int targetX, int targetY) {
    std::vector<std::pair<int, int>> path;

    if (!grid.isValid(startX, startY) || !grid.isValid(targetX, targetY)) {
        return path;
    }

    // Reset grid costs
    for (int y = 0; y < grid.height; ++y) {
        for (int x = 0; x < grid.width; ++x) {
            grid.nodes[y][x].g = 1e9;
            grid.nodes[y][x].h = 0.0;
            grid.nodes[y][x].parentX = -1;
            grid.nodes[y][x].parentY = -1;
        }
    }

    std::priority_queue<Node2D*, std::vector<Node2D*>, CompareNode> openSet;

    Node2D* startNode = &grid.nodes[startY][startX];
    startNode->g = 0.0;
    startNode->h = calculate_h(startX, startY, targetX, targetY);
    openSet.push(startNode);

    std::vector<std::vector<bool>> closedSet(grid.height, std::vector<bool>(grid.width, false));

    while (!openSet.empty()) {
        Node2D* current = openSet.top();
        openSet.pop();

        if (current->x == targetX && current->y == targetY) {
            Node2D* curr = current;
            while (curr != nullptr) {
                path.push_back({curr->x, curr->y});
                if (curr->parentX == -1 || curr->parentY == -1) break;
                curr = &grid.nodes[curr->parentY][curr->parentX];
            }
            std::reverse(path.begin(), path.end());
            return path;
        }

        closedSet[current->y][current->x] = true;

        std::vector<Node2D> neighbors = grid.get_neighbors(*current);
        for (auto& n : neighbors) {
            if (closedSet[n.y][n.x]) continue;

            Node2D* neighborNode = &grid.nodes[n.y][n.x];
            double tentativeG = current->g + 1.0;

            if (tentativeG < neighborNode->g) {
                neighborNode->parentX = current->x;
                neighborNode->parentY = current->y;
                neighborNode->g = tentativeG;
                neighborNode->h = calculate_h(neighborNode->x, neighborNode->y, targetX, targetY);

                openSet.push(neighborNode);
            }
        }
    }
    return path;
}

namespace py = pybind11;

PYBIND11_MODULE(cpp_pathfinder, m) {
    m.doc() = "C++ A* Pathfinder";

    py::class_<Node2D>(m, "Node2D")
        .def(py::init<int, int, bool>(), py::arg("gridX") = 0, py::arg("gridY") = 0, py::arg("obstacle") = false)
        .def_readwrite("x", &Node2D::x)
        .def_readwrite("y", &Node2D::y)
        .def_readwrite("is_obstacle", &Node2D::isObstacle);

    py::class_<Grid>(m, "Grid")
        .def(py::init<int, int>(), py::arg("w"), py::arg("h"))
        .def_readwrite("width", &Grid::width)
        .def_readwrite("height", &Grid::height)
        .def("is_valid", &Grid::isValid)
        .def("set_obstacle", &Grid::set_obstacle);

    py::class_<PathFinder>(m, "PathFinder")
        .def_static("find_path", &PathFinder::find_path);
}