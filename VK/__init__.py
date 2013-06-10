__all__ = ["Base", "Root", "Collection", "Error"]

import VK.User
import VK.Group

"""
All submodules have __init.py with:
- __all__ where listed all modules
- commands "import" one by one module for exporting out classes, nor modules.

Therefore import VK.Module_name will import all classes from this module.

-----------------------------

The Collection imports:
- import base Collection class (from VK.Collection import Collection)
- import items' classes: (from VK.User import User)
- import collections' clasess (from VK.User import Friends)

The Object imports:
- import base Root class (from VK.Root import Root)
- import all own submodule (import VK.User)
-----------------------------

"""