# ThemeManager.py
# ──────────────────────────────────────────────────────────────────────────────

# Description:
# This handles managing themes and returns the value requested (yes I know Custiomtkinter has a theme manager but i wanted to have more control over it)

# Made by: Claude  (Reviewed by FutureGus yes I know ":O HOW COULD YOU USE AI TO WRITE CODE" but I reviewed it and made sure it works)

# Licensed under the CC0 1.0 Universal License - Public Domain Dedication found here: https://creativecommons.org/publicdomain/zero/1.0/

# Created: 04-18-2026

# Last Updated: 04-18-2026

# ──────────────────────────────────────────────────────────────────────────────


# ~--- Imports ---~
import json
import os
from Utils.hyd_AssetLoader import hyd_AssetLoader
# ~----------------------~

# ~--- Setup AssetLoader ---~
AL = hyd_AssetLoader()
THEMES_DIR = AL.Get_folder_path("Themes")
# ~----------------------~

# %--- Theme Manager Class ---%
class ThemeManager:
    """
    Manages themes for hȳd.
    Dynamically loads all Name_Theme.json files from the Themes folder.
    LoadingScreen_Theme.json is loaded separately and is read-only.
    """

# === Init ===
    def __init__(self):
        self._themes = {}
        self._loading_screen_theme = {}
        self._active_theme = None
        self._load_all_themes()
# =====================

#  +--- Internal Methods ---+

    def _load_all_themes(self):
        """
        Loads all Name_Theme.json files from the Themes folder.
        LoadingScreen_Theme.json is loaded separately.
        """
        for filename in os.listdir(THEMES_DIR):
            if not filename.endswith("_Theme.json"):
                continue

            path = os.path.join(THEMES_DIR, filename)

            try:
                with open(path, "r") as f:
                    data = json.load(f)
            except Exception as e:
                print(f"[ThemeManager] Failed to load theme {filename}: {e}")
                continue

            if filename == "LoadingScreen_Theme.json":
                self._loading_screen_theme = data
            else:
                theme_name = filename.replace("_Theme.json", "")
                self._themes[theme_name] = data

    def _get_theme_data(self, theme_name: str) -> dict:
        """
        Returns the raw theme data for a given theme name.
        """
        if theme_name not in self._themes:
            raise KeyError(f"Theme not found: {theme_name}")
        return self._themes[theme_name]

#  +----------------------+

#  +--- Public Methods ---+

    def Set_theme(self, theme_name: str):
        """
        Sets the active theme for live switching.
        """
        if theme_name not in self._themes:
            raise KeyError(f"Theme not found: {theme_name}")
        self._active_theme = theme_name

    def Get(self, theme_name: str, key: str, section: str) -> any:
        """
        Gets a value from a theme.

        Example:
            theme_manager.get("hyd", "BackgroundColor", "Colors")
        """
        theme = self._get_theme_data(theme_name)

        if section not in theme:
            raise KeyError(f"Section '{section}' not found in theme '{theme_name}'")

        if key not in theme[section]:
            raise KeyError(f"Key '{key}' not found in section '{section}' of theme '{theme_name}'")

        return theme[section][key]

    def Get_loading_screen(self, key: str, section: str) -> any:
        """
        Gets a value from the LoadingScreen theme.
        This theme is read-only and cannot be changed by the app.

        Example:
            theme_manager.get_loading_screen("BackgroundColor", "Colors")
        """
        if section not in self._loading_screen_theme:
            raise KeyError(f"Section '{section}' not found in LoadingScreen theme")

        if key not in self._loading_screen_theme[section]:
            raise KeyError(f"Key '{key}' not found in section '{section}' of LoadingScreen theme")

        return self._loading_screen_theme[section][key]

    def Get_active_name(self) -> str:
        """
        Returns the name of the currently active theme.
        Set_theme() must be called first.
        """
        if self._active_theme is None:
            raise RuntimeError("No active theme set. Call Set_theme() first.")
        return self._active_theme

    def List_themes(self) -> list:
        """
        Returns a list of all available theme names.
        """
        return list(self._themes.keys())

#  +----------------------+


# %----------------------%

# ~--- Singleton Instance ---~
_instance = ThemeManager()

def Get_theme_manager() -> ThemeManager:
    return _instance
# ~----------------------~