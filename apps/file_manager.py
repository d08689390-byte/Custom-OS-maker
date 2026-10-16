import tkinter as tk

from core.codeos_window import (
    CodeOSWindow
)


class FileManagerApp(
    CodeOSWindow
):

    def __init__(
        self,
        os_instance
    ):

        super().__init__(
            os_instance,
            "File Manager",
            800,
            500
        )

        self.listbox = tk.Listbox(
            self.window,
            bg="black",
            fg="#00FF00"
        )

        self.listbox.pack(
            fill=tk.BOTH,
            expand=True
        )

        self.refresh()

    def refresh(self):

        self.listbox.delete(
            0,
            tk.END
        )

        files = (
            self.os.filesystem
            .list_directory(
                "user"
            )
        )

        for item in files:
            self.listbox.insert(
                tk.END,
                item
            )