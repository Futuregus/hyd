# Config.py
# ──────────────────────────────────────────────────────────────────────────────

# Description:
# This is the configuration file for hȳd, containing constants and settings used throughout the application.
# (not for user configuration, just for internal use)

# Copyright (C) 2026 Futuregus.
# This file is part of hȳd Which is licensed under the GNU General Public License v3.0
# You are free to modify and distribute hȳd as long as you comply with the license terms.
# hȳd is provided "as is" without any warranty, use at your own risk.
# For full license details, see the COPYING file included with hȳd or visit https://www.gnu.org/licenses/licenses.html

# Created: 04-17-2026

# Last Updated: 04-21-2026

# ──────────────────────────────────────────────────────────────────────────────

# ~--- Imports ---~
import os
from Utils.RootFinder import find_root
# ~----------------------~


# ~--- Filelogr Dependencies ---~
_ROOT = find_root()
DATA_DIR = os.path.join(_ROOT, "Data")
LOG_FILE = "hyd.log"
# ~----------------------~


# %--- Constants ---%

# +--- Misc ---+

VERSION = "V-0.0.1"

STORAGE_DIR = os.path.join(DATA_DIR, "Misc")

# +----------------------+

# +--- Intervals ---+

QUOTES_INTERVAL = 5000
# Time in milliseconds between quote changes on the loading screen

MIN_LOAD_TIME = 2
# Minimum time a task must take before it can go to the next task, this is to prevent the loading screen from flashing too quickly and looking bad. Time is in seconds.

# +----------------------+

# +--- Tables ---+

QUOTES = [
        "Nothing is more important than your secrets.",
        "Your secrets are safe with hȳd.",
        "I can't afford to buy another quote.... wait this is one NOOOOOO I WASTED IT",
        "Hello",
        "Save me I'm trapped in a loading screen :(",
        "You're proof not everyone deserves internet access.",
        "Fun fact: Spartan Scytale (Ancient Greece) Messages were wrapped around a rod; without the right rod size, the message was unreadable.",
        "Fun fact: Modern internet depends on cryptography Everything from banking to messaging apps uses encryption to keep data safe.",
        "Viruses on your computer? Get a scan for only $19.99 your second scan is free! Enter your credit card information to claim this limited time offer!",
        "Never gonna give you up, never gonna let you down, never gonna sell your data.. wait wait wrong song.",
        "Import: scripts.delete.system32()",
        "Did you hear that? sounded like a chicken?",
        "No No NO STOP don't write that, don't even think about writing that, just don't. pls 🥺",
        "Isaiah 41:10 - So do not fear, for I am with you; do not be dismayed, for I am your God. I will strengthen you and help you; I will uphold you with my righteous right hand.",
        "I have a secret to tell you... but I can't, because it's a secret.",
        "Honestly, I'm just impressed you could read this",
        "I'd love to help you out. Which way did you get in?",
        "IT'S BEHIND YOU!!!!",
        "If you set your password to 'Invalid' you will always get a reminder of what your password is when you forget it.",
        "Listen to Mr. Blue Sky by Electric Light Orchestra, it's a good song.",
        "In 1945 a world war ended the world was spilt into two sides, the east and the west this marked the beginning of the cold war, a war of secrets and espionage that lasted for decades."
    ]

DEFAULT_SETTINGS = {
    "theme": "hyd Dark",
    "default_save_location": os.path.join(STORAGE_DIR, "Notes"),
    "update_check": True,
    "word_wrap": True,
    "font_size": 12,
    "quick_hyd_save_directory": os.path.join(STORAGE_DIR, "Quick_hyd"),
    "password_manager_save_location": os.path.join(STORAGE_DIR, "Password_Manager"),
}

# +----------------------+


# %----------------------%