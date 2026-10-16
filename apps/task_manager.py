import tkinter as tk

from core.codeos_window import (
    CodeOSWindow
)


class TaskManagerApp(
    CodeOSWindow
):

    def __init__(
        self,
        os_instance
    ):

        super().__init__(
            os_instance,
            "Task Manager",
            800,
            400
        )

        self.listbox = tk.Listbox(
            self.window
        )

        self.listbox.pack(
            fill=tk.BOTH,
            expand=True
        )

        tk.Button(
            self.window,
            text="Refresh",
            command=self.refresh
        ).pack()

        tk.Button(
            self.window,
            text="Restart Explorer",
            command=self.restart_explorer
        ).pack()

        self.refresh()

    def refresh(self):

        self.listbox.delete(
            0,
            tk.END
        )

        for pid, proc in (
            self.os
            .process_manager
            .processes
            .items()
        ):
            self.listbox.insert(
                tk.END,
                f"{pid} - {proc['name']}"
            )

    def restart_explorer(self):

        self.os.explorer_service.restart()