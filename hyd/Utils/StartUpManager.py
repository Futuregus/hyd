# StartUpManager.py
# ──────────────────────────────────────────────────────────────────────────────

# Description:
# Handles starting up hȳd by running a series of tasks with progress tracking and updating the loading screen accordingly.

# Copyright (C) 2026 Futuregus.
# This file is part of hȳd Which is licensed under the GNU General Public License v3.0
# You are free to modify and distribute hȳd as long as you comply with the license terms.
# hȳd is provided "as is" without any warranty, use at your own risk.
# For full license details, see the COPYING file included with hȳd or visit https://www.gnu.org/licenses/licenses.html

# Created: 04-17-2026

# Last Updated: 04-22-2026

# ──────────────────────────────────────────────────────────────────────────────


# ~--- Imports ---~
import re

from CTkMessagebox import CTkMessagebox
import webbrowser
import threading
from Utils.Helpers import Utilities
from Utils.SettingsManager import Get_settings_manager
from Utils.ThemeManager import Get_theme_manager
from filelogr import Logger
from Core import Config
# ~----------------------~


# ~--- Setup Filelogr ---~

Logger.configure(data_dir=Config.DATA_DIR, log_file=Config.LOG_FILE)

log = Logger.log_action

log("~~~~~~~~~~~~~~~~~~~~~~~~~", separator=True, color="yellow")

log(f"Starting hȳd, {Config.VERSION}", tag="STARTUP", color="blue")

# ~----------------------~


# %--- Task Scheduler ---%
class Task_Scheduler:
    """
    Task_Scheduler manages the execution of startup tasks in order,
    ensuring that each task takes a minimum amount of time to complete for a smooth loading screen experience.
    It also handles progress updates and completion callbacks.
    """

# ~--- Initialize ---~
    def __init__(self, on_complete=None, update_method=None):

        self.Tasks = []

        self.IsTaskRunning = False

        self.Current_Task = 0

        self.On_Complete = on_complete

        self.update_method = update_method

        self._lock = threading.Lock()

        self._method_done = False

        self._time_done = False

        self.on_error = None

# ~----------------------~

#  +--- Internal Methods ---+

    def _run_task(self):

        self.IsTaskRunning = True
        method, message, progress = self.Tasks[self.Current_Task]
        log(f"Running Task:{self.Current_Task}", tag="STARTUP", color="blue")

        self._method_done = False
        self._time_done = False

        if self.update_method:
            self.update_method(message, progress)

        def _run_method():
            try:
                method()
            except Exception as e:
                log(f"Task: {self.Current_Task} has failed with an error of: {e}", tag="ERROR", color="red")
                if self.on_error:
                    self.on_error(e)
            finally:
                with self._lock:
                    self._method_done = True
            self._check_done()



        def _run_timer():
            with self._lock:
                self._time_done = True
            self._check_done()

        threading.Thread(target=_run_method, daemon=True).start()
        threading.Timer(Config.MIN_LOAD_TIME, _run_timer).start()

    def _check_done(self):
        with self._lock:
            if not self._method_done:
                return # Do nothing until the method is done
            if self._method_done and self._time_done:
                self.IsTaskRunning = False
                self.Current_Task += 1
                self._Schedule_Task()

    def _Schedule_Task(self):

        if self.Current_Task >= len(self.Tasks):
            log("Everything seems to have loaded :D", tag="STARTUP", color="green")
            log("*************************", separator=True, color="yellow")
            if self.On_Complete:
                self.On_Complete()
        else:
            self._run_task()

#  +----------------------+

#  +--- Public Methods ---+

    def Add_task(self, method, message, progress):
        """Add a task to the scheduler."""
        self.Tasks.append((method, message, progress))

    def Start(self):
        """Start the task scheduler."""
        self._Schedule_Task()

#  +----------------------+

# %----------------------%


# %--- Start Up Manager Class ---%

class StartUpManager:
    """
    StartUpManager handles the startup process of the application by running a series of tasks with progress tracking and updating the loading screen accordingly.
    It uses the Task_Scheduler to manage the tasks and their execution order.
    """

# ~--- Init ---~
    def __init__(self):
        self.sm = Get_settings_manager()
        self.tm = Get_theme_manager()
        self.utils = Utilities()

# ~----------------------~


# +--- Public Methods ---+

    def Run(self, loading_screen, main_window):
        """ Runs the startup manager, it will execute the tasks in order and update the loading screen with the progress."""

        self.loading_screen = loading_screen

        self.main_window = main_window

        thread = threading.Thread(target=self._run_scheduler)

        thread.daemon = True

        thread.start()

# +-------------------+

# +--- Tasks ---+

    def load_settings(self):
        log("Loading settings...", True, tag="Loading Settings", color="blue")
        self.sm.Init_settings()

    def apply_theme(self):
        log("Applying Theme...", True, tag="STARTUP", color="blue")
        self.tm.Set_theme(theme_name=self.sm.Get_setting("theme"))
        self.main_window.Apply_theme()

    def check_for_updates(self):
        if not self.sm.Get_setting("update_check"):
            log("Skipping update check...", True, tag="STARTUP", color="blue")
            return

        if self.sm.Get_setting("update_check"):
            log("Checking for updates...", True, tag="STARTUP", color="blue")
            self._show_update_notification()


# +----------------------+

# +--- Internal Methods ---+

    def _run_scheduler(self):
        """ Internal method to run the task scheduler"""
        scheduler = Task_Scheduler(on_complete=lambda: self.loading_screen.after(0, self._finish), update_method=self._update)

    # @--- Add Tasks ---@

        scheduler.Add_task(self.load_settings, "Loading settings", 0.25)

        scheduler.Add_task(self.apply_theme, "Loading themes", 0.5)

        scheduler.Add_task(self.check_for_updates, "Checking for updates", 0.75)

        scheduler.Start()

    # @-----------------------@

    def _finish(self):
        """Method to call when all tasks are complete"""

        self.loading_screen.destroy()

        self.main_window.deiconify()

    def _update(self, message, progress):
        """Internal method to update the loading screen with the given message and progress."""
        self.loading_screen.after(0, lambda m=message, p=progress: self.loading_screen.Update_progress(m, p))

    def _show_update_notification(self):

        if not self.sm.Get_setting("update_check"):
            return

        result = self.utils.Check_for_updates(enabled=True)

        if not result[0]:
            return
        msg = CTkMessagebox(
            title="Update Available!",
            message="A new version of hȳd is available. Would you like to open the release page?",
            option_1="Yes",
            option_2="No"
            )
        response = msg.get()

        if response == "Yes":
            webbrowser.open(self.utils.Check_for_updates(enabled=True)[2])

# +-------------------+

# %----------------------%