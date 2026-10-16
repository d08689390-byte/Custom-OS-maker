import tkinter as tk
from tkinter import scrolledtext

from core.codeos_window import CodeOSWindow


class TerminalApp(CodeOSWindow):

    def __init__(self, os_instance):

        super().__init__(
            os_instance,
            "Terminal",
            700,
            500
        )

        self.output = scrolledtext.ScrolledText(
            self.window,
            bg="black",
            fg="#00FF00"
        )

        self.output.pack(
            fill=tk.BOTH,
            expand=True
        )

        self.output.insert(
            tk.END,
            "CodeOS Terminal\n"
        )