# Helpers.py
# ──────────────────────────────────────────────────────────────────────────────

# Description:
# This file contains helper functions and classes used throughout StealthNote.

# Copyright (C) 2026 Futuregus.
# This file is part of hȳd Which is licensed under the GNU General Public License v3.0
# You are free to modify and distribute hȳd as long as you comply with the license terms.
# hȳd is provided "as is" without any warranty, use at your own risk.
# For full license details, see the COPYING file included with hȳd or visit https://www.gnu.org/licenses/licenses.html

# Last Updated: 04-20-2026

# ──────────────────────────────────────────────────────────────────────────────

# %--- Imports ---%
import re
import requests
from packaging.version import Version
from Core import Config
# %----------------------%

# %--- CustomTkinter Helpers Class---%

class CTkHelpers:
    """
    Helper functions for customtkinter widgets.
    """

    def Center_window(window, width=None, height=None):
        """
        Centers a tkinter window on the screen.
        """
        window.update_idletasks()
        width = width or window.winfo_width()
        height = height or window.winfo_height()
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")

# %----------------------%

# +--- Utilities Class ---+

class Utilities:
    """
    A collection of utility functions used throughout hȳd.
    """

    update_check_url = "https://api.github.com/repos/Futuregus/hyd/releases/latest"

    def Check_for_updates(self, enabled: bool):
        """
        Checks GitHub API for the latest release and compares it to the current version.
        Returns a tuple (is_update_available, latest_version, release_url).
        """
        if not enabled:
            return False, None, None

        try:
            response = requests.get(Utilities.update_check_url, timeout=5)
            response.raise_for_status()
            data = response.json()

            latest_version = re.sub(r'^[^\d]+', '', data["tag_name"])
            current_version = re.sub(r'^[^\d]+', '', Config.VERSION)
            release_url = data["html_url"]

            is_update_available = Version(latest_version) > Version(current_version)

            return is_update_available, latest_version, release_url

        except Exception as e:
            print(f"[Utilities] Failed to check for updates: {e}")
            return False, None, None

