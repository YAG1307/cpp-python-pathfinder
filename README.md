## ➡️ C++ Pathfinder Library for Python

An A* pathfinding engine written in C++, then built into a library for Python 3.14 using pybind11. Visualization through pygame in visualizer.py.

---
# IMAGE



<img width="917" height="1004" alt="image" src="https://github.com/user-attachments/assets/80dbbb0a-2fe0-445e-b197-228a2a247d1f" />


---
## Summary & Highlights

This project bridges fast C++ code with Python's simple scripting. The core pathfinding calculations, node traversal, and priority queue operations run inside compiled C++, allowing 0 path evaluation while allowing Python to handle rendering. 

* C++ Engine (cpp): node representation, grid allocation, and an A* algorithm.
* Python Binding: Using pybind11, I created a pyrpoject.toml and setup.py to bridge the C++ code directly into Python.
* Visualizer (python/visualizer.py):** Interactive grid frontend capturing mouse inputs, modifying obstacle states in C++, and rendering paths instantly.

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
