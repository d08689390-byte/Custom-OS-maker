import tkinter as tk

from core.codeos_window import (
    CodeOSWindow
)


class QuickSettingsApp(
    CodeOSWindow
):

    def __init__(
        self,
        os_instance
    ):

        super().__init__(
            os_instance,
            "Quick Settings",
            350,
            400
        )

        self.build_ui()

    def build_ui(self):

        tk.Label(
            self.window,
            text="Volume"
        ).pack()

        slider = tk.Scale(
            self.window,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL
        )

        slider.set(
            self.os.sound_manager.volume
        )

        slider.pack(
            fill=tk.X
        )

        tk.Button(
            self.window,
            text="Toggle Mute",
            command=
                self.os.sound_manager
                .toggle_mute
        ).pack(
            fill=tk.X
        )

        tk.Button(
            self.window,
            text="Dark Theme",
            command=lambda:
                self.os.theme_manager
                .set_theme(
                    "dark"
                )
        ).pack(
            fill=tk.X
        )