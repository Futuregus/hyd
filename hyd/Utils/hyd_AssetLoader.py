# hyd_AssetLoader.py
# ──────────────────────────────────────────────────────────────────────────────

# Description:
# This is a adaptation of a script I made for other projects (the original was made by me )
# It is a simple asset loader that helps to load assets from a specific folder structure.

# Made by: ChatGPT ( Yeah I know "YOU CAN'T USE CHATGPT TO WRITE CODE" but I (futuregus) reviewed it and made sure it works and is up to my standards :D )

# Licensed under the CC0 1.0 Universal License - Public Domain Dedication found here: https://creativecommons.org/publicdomain/zero/1.0/

# Created: 04-17-2026

# Last Updated: 04-19-2026

# ──────────────────────────────────────────────────────────────────────────────

# ~--- Imports ---~
import os
import sys
from Utils.RootFinder import find_root
# ~----------------------~

# %--- hyd Asset Loader  Class ---%

class hyd_AssetLoader:
    """
    StealthNote-specific asset loader.

    Structure expected:
    Assets/
        Icons/
        Misc/
        Themes/
        etc...
    """

# ~--- Init ---~
    def __init__(self, assets_folder_name="Assets"):
        self.base_dir = self._get_app_root()
        self.assets_dir = os.path.join(self.base_dir, assets_folder_name)
# ~----------------------~

# +--- Internal Methods ---+

    def _get_app_root(self):
        """
        Returns the project root by:
        - .exe folder (PyInstaller)
        - .approot marker file (dev mode)
        """

        if getattr(sys, "frozen", False):
            return os.path.dirname(sys.executable)
        return find_root()

    def _get_category_path(self, category: str):
        path = os.path.join(self.assets_dir, category)

        if not os.path.exists(path):
            raise FileNotFoundError(f"Asset category not found: {category}")

        return path

# +----------------------+

# +--- Public Methods ---+

    def Get_asset_path(self, filename: str, category: str = "Misc"):
        """
        Returns full path to an asset file.

        Example:
            loader.Get("hydlogo.ico", "Icons")
        """

        category_path = self._get_category_path(category)
        full_path = os.path.join(category_path, filename)

        if not os.path.exists(full_path):
            raise FileNotFoundError(
                f"Asset not found: {filename} in {category}"
            )

        return full_path

    def Get_folder_path(self, folder_name: str):
        """
        Returns full path to an asset folder.

        Example:
            loader.Get_folder("Icons")
        """

        return self._get_category_path(folder_name)

# +----------------------+

# %----------------------%