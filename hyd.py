# hyd.py
#  ──────────────────────────────────────────────────────────────────────────────

# Description:
# hȳd is a secure offline-first note-taking application designed to keep your secrets hidden.
# This file is the main entry point for the application, responsible for initializing and launching the app.

# Copyright (C) 2026 Futuregus.
# hȳd is licensed under the GNU General Public License v3.0
# You are free to modify and distribute hȳd as long as you comply with the license terms.
# hȳd is provided "as is" without any warranty, use at your own risk.
# For full license details, see the COPYING file included with hȳd or visit https://www.gnu.org/licenses/licenses.html

# Created: 04-17-2026

# Last Updated: 04-17-2026

# App Version: 0.0.1 test

#  ──────────────────────────────────────────────────────────────────────────────

# ~--- Imports ---~
from UI.LoadingScreen import LoadingScreen
from UI.MainWindow import MainWindow
from Utils.StartUpManager import StartUpManager, log as log
# ~----------------------~

# %--- Run StartUpManager ---%

def _main():

    window = MainWindow()
    loading = LoadingScreen(window)

    try:
        StartUpManager().Run(loading, window)
    except Exception as e:
        log(F"A fatal error occurred during startup: {e}", tag="ERROR", color="red")
        loading.destroy()
        window.deiconify()

    window.mainloop()

if __name__ == "__main__":
    _main()

# %----------------------%