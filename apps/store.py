import tkinter as tk

from core.codeos_window import (
    CodeOSWindow
)


class StoreApp(
    CodeOSWindow
):

    def __init__(
        self,
        os_instance
    ):

        super().__init__(
            os_instance,
            "Store"
        )

        self.packages = {

            "Matrix Screensaver":
                "matrix",

            "Retro Clock":
                "clock",

            "Text Viewer":
                "viewer"
        }

        for app in self.packages:

            tk.Button(
                self.window,
                text=app
            ).pack(
                fill=tk.X,
                padx=10,
                pady=4
            )