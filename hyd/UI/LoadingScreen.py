# LoadingScreen.py
# ──────────────────────────────────────────────────────────────────────────────

# Description:
# This is the UI for the loading screen

# Copyright (C) 2026 Futuregus.
# This file is part of hȳd Which is licensed under the GNU General Public License v3.0
# You are free to modify and distribute hȳd as long as you comply with the license terms.
# hȳd is provided "as is" without any warranty, use at your own risk.
# For full license details, see the COPYING file included with hȳd or visit https://www.gnu.org/licenses/licenses.html

# Created: 04-17-2026

# Last Updated: 04-21-2026

# ──────────────────────────────────────────────────────────────────────────────


# ~--- Imports ---~
import customtkinter as ctk
import random
from PIL import Image
import pywinstyles
from Core import Config
from Utils.Helpers import CTkHelpers
from Utils.ThemeManager import Get_theme_manager
from Utils.hyd_AssetLoader import hyd_AssetLoader
# ~----------------------~


# %--- Loading Screen Class ---%

class LoadingScreen(ctk.CTkToplevel):
    """UI for the loading screen."""

#  +--- Create Window ---+

    def __init__(self, parent):
        super().__init__(parent)
        al = hyd_AssetLoader()
        self.theme = Get_theme_manager()

# === Main Loading Screen Window Setup ===

# @--- Setup Window properties ---@

        self.overrideredirect(True) # Remove window controls and title bar

        self.title(f"hȳd {Config.VERSION}") # Just set the title so it shows up in the task manager, it won't actually be visible on the window

        self.geometry("900x350") # Set the size of the loading screen

        self.resizable(False, False)

        self.update_idletasks() # force update to get correct window size for centering

        CTkHelpers.Center_window(self)

# @-----------------------@

# @--- Setup the frame ---@

        self.frame = ctk.CTkFrame(self, fg_color="transparent", bg_color="transparent")

        bg_path = al.Get_asset_path("hydloading.png", "Icons")

        bg_image = ctk.CTkImage(Image.open(bg_path), size=(900, 350))

        self.bg_label = ctk.CTkLabel(self.frame, image=bg_image, text="")

        self.bg_label.place(x=0, y=0)

        self.frame.pack(expand=True, fill="both", padx=0, pady=0)

# @-----------------------@

# =====================

# === Screen Title Spacer ===

        self.screen_title = ctk.CTkLabel(self.frame, text=" ") # Just a space so that the elements don't overlap with the title on the background image

        self.screen_title.pack(pady=30)

# =====================

# === Quote Label ===

        self.quote_label = ctk.CTkLabel(self.frame, text=" ")

        self.quote_label.pack(pady=20)

        self.quote_label.configure(

            fg_color="#A7A7A7",

            text_color=self.theme.Get_loading_screen("TextColor", "Colors"),

            font=(self.theme.Get_loading_screen("Family", "Fonts"),

            self.theme.Get_loading_screen("QuoteSize", "Fonts")), wraplength=850
            )

        self.last_quote = None

        pywinstyles.set_opacity(self.quote_label, color="#A7A7A7") # Makes the text not have a background

# =====================

# === Progress Bar ===

        self.progress_bar = ctk.CTkProgressBar(self.frame, width=400)

        self.progress_bar.set(0)

        self.progress_bar.pack(pady=20)

        self.progress_bar.configure(

            fg_color= self.theme.Get_loading_screen("AccentColor", "Colors"),

            progress_color=self.theme.Get_loading_screen("LoadingBarColor", "Colors"),

            corner_radius=self.theme.Get_loading_screen("LoadingBarRadius", "Others"),

            height=self.theme.Get_loading_screen("LoadingBarHeight", "Others"),

            width=self.theme.Get_loading_screen("LoadingBarWidth", "Others")

            )

# =====================

# === Status Label ===

        self.status_label = ctk.CTkLabel(self.frame, text=" ")

        self.status_label.pack(pady=10)

        self.status_label.configure(

            fg_color="#A7A7A7",

            text_color=self.theme.Get_loading_screen("TextColor", "Colors"),

            font=(self.theme.Get_loading_screen("Family", "Fonts"),

            self.theme.Get_loading_screen("MessageSize", "Fonts")))

        pywinstyles.set_opacity(self.status_label, color="#A7A7A7")

# =====================

# === Setup Quote Rotation ===

        self.quotes = Config.QUOTES

        self._rotate_quotes()

# =====================

#  +----------------------+

#  +--- Public Methods ---+

    def Update_progress(self, message: str, progress: float):
        """Updates the loading screen with a message and progress percentage."""
        self.progress_bar.set(progress)

        self.status_label.configure(text=message)

        self.update_idletasks()

    def _rotate_quotes(self):
        """ Rotates the quotes on the loading screen every few seconds."""

        quote = random.choice(self.quotes)

        while quote == self.last_quote and len(self.quotes) > 1:
            quote = random.choice(self.quotes)

        self.last_quote = quote

        self.quote_label.configure(text=quote)

        self.after(Config.QUOTES_INTERVAL, self._rotate_quotes)

#  +----------------------+

# %----------------------%