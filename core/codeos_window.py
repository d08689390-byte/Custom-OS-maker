import tkinter as tk


class CodeOSWindow:
    def __init__(
        self,
        os_instance,
        title,
        width=800,
        height=600
    ):
        self.os = os_instance

        self.window = tk.Toplevel(
            self.os.root
        )

        self.window.title(title)

        self.window.geometry(
            f"{width}x{height}"
        )

        self.window.configure(
            bg="#002200"
        )

        self.window.protocol(
            "WM_DELETE_WINDOW",
            self.close
        )

    def close(self):
        self.window.destroy()