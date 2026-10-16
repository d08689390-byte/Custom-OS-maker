import os


class TaskbarManager:
    def add_app_button(self, pid, app_name):
        """Register an application button on the taskbar."""
        return pid, app_name


taskbar_manager = TaskbarManager()

taskbar_manager.add_app_button(
    os.getpid(),
    "app_name"
)