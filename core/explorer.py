import tkinter as tk

from core.desktop_icon import DesktopIcon


class CodeOSExplorer:

    def __init__(self, os_instance):

        self.os = os_instance

        self.desktop_icons = []

        self.build_desktop()

        self.build_taskbar()

        self.load_default_icons()

    def build_desktop(self):

        theme = self.os.theme_manager.get()

        self.desktop = tk.Canvas(
            self.os.root,
            bg=theme["background"],
            highlightthickness=0
        )

        self.desktop.pack(
            fill=tk.BOTH,
            expand=True
        )

    def build_taskbar(self):

        theme = self.os.theme_manager.get()

        self.taskbar = tk.Frame(
            self.os.root,
            bg=theme["taskbar"],
            height=40
        )

        self.taskbar.pack(
            side=tk.BOTTOM,
            fill=tk.X
        )

        tk.Button(
            self.taskbar,
            text="START",
            command=self.open_start_menu
        ).pack(
            side=tk.LEFT,
            padx=5
        )

        self.clock_label = tk.Label(
            self.taskbar,
            text="00:00",
            bg=theme["taskbar"],
            fg=theme["foreground"]
        )

        self.clock_label.pack(
            side=tk.RIGHT,
            padx=10
        )

        self.update_clock()

    def update_clock(self):

        import time

        self.clock_label.config(
            text=time.strftime("%H:%M:%S")
        )

        self.clock_label.after(
            1000,
            self.update_clock
        )

    def open_start_menu(self):

        profile = tk.Menubutton(
            self.taskbar,
            text=self.os.current_user
        )

        profile.pack(
            side=tk.RIGHT,
            padx=5
        )

        menu = tk.Toplevel(self.os.root)

        menu.title("Start")

        menu.geometry("250x400")

        apps = sorted(
            self.os.registry.apps.keys()
        )

        for app in apps:

            tk.Button(
                menu,
                text=app,
                command=lambda a=app:
                    self.os.registry.launch(
                        a,
                        self.os
                    )
            ).pack(
                fill=tk.X,
                padx=5,
                pady=2
            )

    def create_shortcut(
        self,
        x,
        y,
        name,
        app_name
    ):

        icon = DesktopIcon(
            self.desktop,
            x,
            y,
            name,
            lambda:
                self.os.registry.launch(
                    app_name,
                    self.os
                )
        )

        self.desktop_icons.append(
            icon
        )

    def load_default_icons(self):

        self.create_shortcut(
            80,
            60,
            "Browser",
            "Browser"
        )

        self.create_shortcut(
            80,
            130,
            "Store",
            "Store"
        )

        self.create_shortcut(
            80,
            200,
            "Terminal",
            "Terminal"
        )

        self.create_shortcut(
            80,
            270,
            "Files",
            "File Manager"
        )

        self.create_shortcut(
            80,
            340,
            "Settings",
            "Settings"
        )