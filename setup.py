from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Pybind11Extension(
        "cpp_pathfinder",
        ["cpp/src/pathfinder.cpp"],
        include_dirs=["cpp/include"],
        cxx_std=17,
    ),
]

setup(
    name="pathfinder_cpp",
    version="0.0.0",
    description="C++ A* Pathfinder Python Extension",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
)