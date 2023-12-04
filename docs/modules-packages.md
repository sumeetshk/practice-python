# Modules

A module is basically a container filled with functions that we want to distribute
The initialization of a module happens only once
The name variable makes it easy for us to detect in which context the code has been activated
Package: group of modules

PyPI:
- Python Package Index
- pypi.org
- PyPI is also referred as Cheese Shop
- maintained by Packaging Working Group
- can access using PIP(pip install packages)

PIP commands:
```bash
pip --version
pip list # list all local packages
pip search pygame # search locally and in repo
pip install pygame # install specific version depending upon Python Version
pip install pygame==2.0.1 # install specific version
pip show pygame
```

`__pycache__` directory contains files of compiled python code
`.pyc` files contain compiled code

```python
import sys
sys.path.append()
```

name variable:
