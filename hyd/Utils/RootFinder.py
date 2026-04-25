# RootFinder.py
# ──────────────────────────────────────────────────────────────────────────────

# Description:
# Utility that finds the project root by searching upward for the .approot marker file.

# Author: Claude  (Reviewed by FutureGus yes I know claude wrote this but I reviewed it and made sure it works)

# Licensed under the MIT License

# Created: 04-17-2026

# Last Updated: 04-18-2026

# ──────────────────────────────────────────────────────────────────────────────

# %--- Imports ---%
import os
import sys
# %----------------------%


# %--- Root Finder ---%
def find_root():
    """
    Searches upward from this file's location until it finds
    a folder containing a .approot marker file.
    Returns the path to that folder as the project root.
    """
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)

    current = os.path.abspath(__file__)
    while True:
        current = os.path.dirname(current)
        if os.path.exists(os.path.join(current, ".approot")):
            return current
        parent = os.path.dirname(current)
        if parent == current:
            raise FileNotFoundError(".approot marker file not found")
# %----------------------%