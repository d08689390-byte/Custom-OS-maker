import tkinter as tk

from core.codeos_window import CodeOSWindow


class BrowserApp(CodeOSWindow):

    def __init__(self, os_instance):

        super().__init__(
            os_instance,
            "Browser",
            1000,
            700
        )

        tk.Label(
            self.window,
            text="Browser Engine",
            fg="#00FF00",
            bg="#002200"
        ).pack(
            pady=20
        )