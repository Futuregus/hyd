# SettingsManager.py
# ──────────────────────────────────────────────────────────────────────────────

# Description:
# This is the settings manager for hȳd, it handles loading and saving settings to a JSON file.

# Copyright (C) 2026 Futuregus
# This file is part of hȳd Which is licensed under the GNU General Public License v3.0
# You are free to modify and distribute hȳd as long as you comply with the license terms.
# hȳd is provided "as is" without any warranty, use at your own risk.
# For full license details, see the COPYING file included with hȳd or visit https://www.gnu.org/licenses/licenses.html

# Created: 04-22-2026

# Last Updated: 04-24-2026

# ──────────────────────────────────────────────────────────────────────────────

# %--- Imports ---%
import json
import os
from Core import Config
# %----------------------%

# %--- Settings Manager Class ---%

class SettingsManager:
    """Manages application settings, including loading and saving settings to a JSON file."""

# ~--- Init ---~
    def __init__(self):
        self.settings_file = os.path.join(Config.DATA_DIR, "settings.json")
        self.default_settings = Config.DEFAULT_SETTINGS
# ~----------------------~

# +--- Internal Methods ---+

    def _save_settings(self, settings):
        """Internal Method to save all settings to a JSON file"""
        os.makedirs(os.path.dirname(self.settings_file), exist_ok=True)
        with open(self.settings_file, "w") as f:
            json.dump(settings, f, indent=4)

# +----------------------+

#  +--- Public Methods ---+

    def Init_settings(self):
        """Create settings file with defaults if it doesn't exist."""
        if not os.path.exists(self.settings_file):
            self._save_settings(self.default_settings)

    def Get_setting(self, key):
        """Get a setting from the JSON file."""
        with open(self.settings_file, "r") as f:
            settings = json.load(f)
        return settings.get(key)

    def Set_setting(self, key, value):
        """Update a single setting in the JSON file."""
        with open(self.settings_file, "r") as f:
            settings = json.load(f)
        settings[key] = value
        self._save_settings(settings)

    def Reset_settings(self):
        """Reset settings to default values."""
        self._save_settings(self.default_settings)

#  +----------------------+

# %----------------------%

# %--- Singleton Instance ---%

_instance = SettingsManager()

def Get_settings_manager() -> SettingsManager:
    return _instance

# %----------------------%