import tkinter as tk


class StartMenu:

    def __init__(
        self,
        os_instance
    ):

        self.os = os_instance

    def show(self):

        win = tk.Toplevel(
            self.os.root
        )

        win.title(
            "Start Menu"
        )

        win.geometry(
            "300x450"
        )

        for app in sorted(
            self.os.registry.apps
        ):

            tk.Button(
                win,
                text=app,
                command=lambda a=app:
                    self.os.registry.launch(
                        a,
                        self.os
                    )
            ).pack(
                fill=tk.X
            )