import tkinter as tk
from tkinter import scrolledtext

from core.codeos_window import (
    CodeOSWindow
)


class IDEApp(
    CodeOSWindow
):

    def __init__(
        self,
        os_instance
    ):

        super().__init__(
            os_instance,
            "IDE",
            900,
            600
        )

        self.editor = (
            scrolledtext
            .ScrolledText(
                self.window,
                bg="black",
                fg="#00FF00"
            )
        )

        self.editor.pack(
            fill=tk.BOTH,
            expand=True
        )