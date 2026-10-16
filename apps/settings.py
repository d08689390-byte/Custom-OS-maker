import tkinter as tk

from core.codeos_window import (
    CodeOSWindow
)


class SettingsApp(
    CodeOSWindow
):

    def __init__(
        self,
        os_instance
    ):

        super().__init__(
            os_instance,
            "Settings"
        )

        tk.Label(
            self.window,
            text="Theme"
        ).pack()

        tk.Button(
            self.window,
            text="Matrix"
        ).pack(
            fill=tk.X
        )

        tk.Button(
            self.window,
            text="Dark"
        ).pack(
            fill=tk.X
        )