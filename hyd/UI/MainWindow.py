# MainWindow.py
# ──────────────────────────────────────────────────────────────────────────────

# Description:
# This is the the main window of hȳd, it is responsible for displaying the main interface of the application and handling user interactions.

# Copyright (C) 2026 Futuregus
# This file is part of hȳd Which is licensed under the GNU General Public License v3.0
# You are free to modify and distribute hȳd as long as you comply with the license terms.
# hȳd is provided "as is" without any warranty, use at your own risk.
# For full license details, see the COPYING file included with hȳd or visit https://www.gnu.org/licenses/licenses.html

# Created: 04-20-2026

# Last Updated: 04-24-2026

# ──────────────────────────────────────────────────────────────────────────────

# ~--- Imports ---~
import customtkinter as ctk
from CTkMenuBarPlus import *
from Utils.SettingsManager import Get_settings_manager
from Utils.ThemeManager import Get_theme_manager
from Core import Config
from Utils.Helpers import CTkHelpers
# ~----------------------~

# ~--- Setup Stuff---~
tm = Get_theme_manager()
sm = Get_settings_manager()
# ~----------------------~

# %--- Main Window Class ---%

class MainWindow(ctk.CTk):

#  +--- Create Main Window ---+
    def __init__(self):
        super().__init__()
        self.withdraw() # Hide the window during setup

# === Setup Main Window Properties ===

        self.title(f"hȳd {Config.VERSION}")
        self.geometry("800x600")
        self.minsize(width=800, height=600)
        self.update_idletasks()
        CTkHelpers.Center_window(self, 800, 600)

# =====================

# === Setup Menu Bar ===

        self.menu_bar = CTkMenuBar(master=self)

        self.settings_menu = self.menu_bar.add_cascade(text="Settings")

        self.file_menu = self.menu_bar.add_cascade(text="File")

        self.keybinds_menu = self.menu_bar.add_cascade(text="Keybinds")

        self.plugins_menu = self.menu_bar.add_cascade(text="Plugins")

        self.about_menu = self.menu_bar.add_cascade(text="About")

        self.help_menu = self.menu_bar.add_cascade(text="Help")

        self.settings_dropdown = CustomDropdownMenu(widget=self.settings_menu)

        self.file_dropdown = CustomDropdownMenu(widget=self.file_menu)

        self.keybinds_dropdown = CustomDropdownMenu(widget=self.keybinds_menu)

        self.plugins_dropdown = CustomDropdownMenu(widget=self.plugins_menu)

        self.about_dropdown = CustomDropdownMenu(widget=self.about_menu)

        self.help_dropdown = CustomDropdownMenu(widget=self.help_menu)

# =====================

# === Setup Settings Menu ===

# @---Setup Theme Menu ---@

        thememenu = self.settings_dropdown.add_submenu("Set Theme")

        for theme in tm.List_themes():
            thememenu.add_option(option=theme, command=lambda t=theme: self._on_set_theme(t))

# @-----------------------@

# @--- Setup Buttons ---@

        self.settings_dropdown.add_option(option="Font Size", command=self._on_set_font_size)

        self.settings_dropdown.add_separator()

        self.settings_dropdown.add_option(option="Reset To Default Settings", command=sm.Reset_settings)

# @-----------------------@

# ========================

# === Setup File Menu ===

        self.read_only_button = self.file_dropdown.add_option(option="Read Only Mode", command=self._on_menu_button1, checkable=True, checked=False, accelerator="Ctrl+R")

        self.file_dropdown.add_separator()

        self.file_dropdown.add_option(option="Open Note", command=lambda: print("Open Note"), accelerator="Ctrl+O")

        self.file_dropdown.add_option(option="Save Note", command=lambda: print("Save Note"), accelerator="Ctrl+S")

        self.file_dropdown.add_option(option="Save Note As", command=lambda: print("Save Note As"), accelerator="Ctrl+Shift+S")

        self.file_dropdown.add_separator()

        self.file_dropdown.add_option(option="Print Note", command=lambda: print("Print Note"), accelerator="Ctrl+P")

# ========================

# === Setup Keybinds Menu ===

        self.keybinds_dropdown.add_option(option="Save Note", accelerator="Ctrl+s")

        self.keybinds_dropdown.add_option(option="Open Note", accelerator="Ctrl+o")

        self.keybinds_dropdown.add_option(option="Save Note As", accelerator="Ctrl+Shift+s")

        self.keybinds_dropdown.add_option(option="Toggle Read Only", accelerator="Ctrl+r")

        self.keybinds_dropdown.add_option(option="Print note", accelerator="Ctrl+p")
# ========================

# === Setup Text Area ===

        self.textarea = ctk.CTkTextbox(self, fg_color="transparent")

        self.textarea.pack(expand=True, fill="both")

        self.textarea.configure(state="normal")

        self.read_only = "normal"

# =====================

# === Setup Keybinds ===

        self.bind("<Control-r>", lambda e: self._on_menu_button1())

        self.bind("<Control-o>", lambda e: print("Open Note"))

        self.bind("<Control-s>", lambda e: print("Save Note"))

        self.bind("<Control-Shift-s>", lambda e: print("Save Note As"))

        self.bind("<Control-p>", lambda e: print("Print Note"))

# ========================

#  +----------------------+

#  +--- Button Handlers ---+

    def _on_menu_button1(self):

        if self.read_only == "normal":
            self.read_only = "disabled"
            self.read_only_button.set_checked(checked=True)
        else:
            self.read_only = "normal"
            self.read_only_button.set_checked(checked=False)
        self.textarea.configure(state=self.read_only)

    def _on_set_theme(self, theme_name):

        tm.Set_theme(theme_name)
        sm.Set_setting(key="theme", value=theme_name)
        self.Apply_theme()

    def _on_set_font_size(self):
        font_size_window = ctk.CTkInputDialog(text="Input Font Size",title="Set Font Size")
        value = font_size_window.get_input()

        if value is None:
            return

        try:
            value = int(value)
        except ValueError:
            return

        theme_name = tm.Get_active_name()
        self.textarea.configure(font=(tm.Get(theme_name, "Family", "Fonts"), value))
        sm.Set_setting(key="font_size", value=value)

#  +----------------------+

# +--- Public Methods ---+

    def Apply_theme(self):

        theme_name = tm.Get_active_name()

        self.configure(fg_color=tm.Get(theme_name, "BackgroundColor", "Colors")) # this has to be set first or everything will break, no idea why

        self.menu_bar.configure(bg_color=tm.Get(theme_name, "AccentColor", "Colors"))

        self.textarea.configure(text_color=tm.Get(theme_name, "TextColor", "Colors"))

        self.settings_menu.configure(bg_color=tm.Get(theme_name, "ButtonColor", "Colors"), text_color=tm.Get(theme_name, "TextColor", "Colors"))

        self.file_menu.configure(bg_color=tm.Get(theme_name, "ButtonColor", "Colors"), text_color=tm.Get(theme_name, "TextColor", "Colors"))

        self.keybinds_menu.configure(bg_color=tm.Get(theme_name, "ButtonColor", "Colors"), text_color=tm.Get(theme_name, "TextColor", "Colors"))

        self.plugins_menu.configure(bg_color=tm.Get(theme_name, "ButtonColor", "Colors"), text_color=tm.Get(theme_name, "TextColor", "Colors"))

        self.about_menu.configure(bg_color=tm.Get(theme_name, "ButtonColor", "Colors"), text_color=tm.Get(theme_name, "TextColor", "Colors"))

        self.help_menu.configure(bg_color=tm.Get(theme_name, "ButtonColor", "Colors"), text_color=tm.Get(theme_name, "TextColor", "Colors"))

# +----------------------+


# %----------------------%