import tkinter as tk
from tkinter import ttk

from core.codeos_window import (
    CodeOSWindow
)


class AboutApp(CodeOSWindow):

    VERSION = "3.0"
    ENGINE = "CodeOS Desktop Framework"

    def __init__(self, os_instance):

        super().__init__(
            os_instance,
            "About CodeOS",
            500,
            450
        )

        title = tk.Label(
            self.window,
            text="CodeOS",
            font=("Courier", 28, "bold"),
            fg="#00FF00",
            bg="#002200"
        )

        title.pack(
            pady=(20, 5)
        )

        subtitle = tk.Label(
            self.window,
            text="Developer Edition",
            font=("Courier", 12),
            fg="#00FF00",
            bg="#002200"
        )

        subtitle.pack()

        tk.Frame(
            self.window,
            bg="#00AA00",
            height=2
        ).pack(
            fill=tk.X,
            padx=20,
            pady=15
        )

        info = f"""
Version: {self.VERSION}

Engine:
{self.ENGINE}

Python:
Running through Tkinter

Installed Apps:
{len(self.os.registry.apps)}

Running Processes:
{len(self.os.process_manager.processes)}

Filesystem:
Virtual User Storage Enabled

Theme:
{self.os.theme_manager.current_theme}
"""

        tk.Label(
            self.window,
            text=info,
            justify="left",
            anchor="w",
            font=("Courier", 10),
            fg="#00FF00",
            bg="#002200"
        ).pack(
            fill=tk.BOTH,
            expand=True,
            padx=20
        )

        tk.Button(
            self.window,
            text="System Information",
            command=self.show_system_info
        ).pack(
            pady=10
        )

    def show_system_info(self):

        message = (
            f"CodeOS Version {self.VERSION}\n\n"
            f"Registered Apps: {len(self.os.registry.apps)}\n"
            f"Running Processes: {len(self.os.process_manager.processes)}\n"
            f"Current Theme: {self.os.theme_manager.current_theme}"
        )

        tk.messagebox.showinfo(
            "System Information",
            message
        )

        tabs = ttk.Notebook(
            self.window
        )

        tabs.pack(
            fill="both",
            expand=True
        )

        overview = ttk.Frame(
            tabs
        )

        developer = ttk.Frame(
            tabs
        )

        tabs.add(
            overview,
            text="Overview"
        )

        tabs.add(
            developer,
            text="Developer Mode"
        )

        tk.Label(
            developer,
            text=f"""
Running Processes:
{len(self.os.process_manager.processes)}

Installed Apps:
{len(self.os.registry.apps)}

Theme:
{self.os.theme_manager.current_theme}

Filesystem:
Mounted

Developer Account:
{self.os.current_user}
"""
        ).pack(
            anchor="w",
            padx=10,
            pady=10
        )

    def kill_selected(self):

        selection = self.listbox.curselection()

        if not selection:
            return

        pid = int(
            self.listbox.get(selection[0]).split()[0]
        )

        self.os.process_manager.kill_process(pid)
        self.refresh()