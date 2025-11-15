# Copyright (c) 2024, creqit Technologies and contributors
# License: MIT. See LICENSE

import os
import sys
import importlib.util

# Add the current directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

# Import dashboard module
spec = importlib.util.spec_from_file_location("dashboard", os.path.join(current_dir, "dashboard.py"))
dashboard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dashboard)

# Make dashboard available in creqit namespace
from . import dashboard 