import tkinter as tk

from core.codeos_window import CodeOSWindow


class RecycleBinApp(CodeOSWindow):

    def __init__(self, os_instance):

        super().__init__(
            os_instance,
            "Recycle Bin",
            700,
            500
        )

        self.listbox = tk.Listbox(
            self.window
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

        for item in self.os.recycle_bin:
            self.listbox.insert(
                tk.END,
                item
            )