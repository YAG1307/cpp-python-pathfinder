## ➡️ C++ Pathfinder Library for Python

An A* pathfinding engine written in C++, then built into a library for Python 3.14 using pybind11. Visualization through pygame in visualizer.py.

---
# IMAGE



<p align="center">
  <img src="https://github.com/user-attachments/assets/80dbbb0a-2fe0-445e-b197-228a2a247d1f" width="500" alt="Pathfinder Visualizer Demo" />
</p>


---
## Summary & Highlights

This project combines a C++ pathfinding core with a Python interface, using pybind11 to expose the native implementation to Python. The core pathfinding calculations, node traversal, and priority queue operations run inside compiled C++, allowing path evaluation while Python handles rendering rendering. 

* C++ Engine: node representation, grid allocation, and an A* algorithm.
* Python Binding: Using pybind11, I bridged the C++ pathfinding functionality to Python and configured the package build through pyproject.toml and setup.py.
* Visualizer (python/visualizer.py): Interactive grid frontend capturing mouse inputs, modifying obstacle states in C++, and rendering paths instantly.

---

## Getting Started

### Prerequisites
* C++ compiler
* Python 3.14+

### Installation & Execution

1. **Clone the repository:**
   ```powershell
   git clone [https://github.com/YAG1307/cpp-python-pathfinder.git](https://github.com/YAG1307/cpp-python-pathfinder.git)
   cd cpp-python-pathfinder
2. Build extension into python.
   ```powershell
   pip install -e . --force-reinstall --no-cache-dir
3. Run visualizer.py

---
## Dev Notes

Ver 0.0.0

Built this as a high-performance pathfinding library to reuse in future Python/C++ projects and showcase native binding logic. Kept header (.h) and source (.cpp) files  separated for clean exports when compiling with pybind11. Developed entirely in PyCharm. I used pygame-ce for a clean visual with Python 3.14 build tools.
