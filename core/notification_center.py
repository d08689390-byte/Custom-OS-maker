import tkinter as tk


class NotificationCenter:

    def __init__(
        self,
        os_instance
    ):

        self.os = os_instance

        self.notifications = []

    def notify(
        self,
        title,
        message
    ):

        self.notifications.append(
            (title, message)
        )

        popup = tk.Toplevel(
            self.os.root
        )

        popup.title(title)

        popup.geometry(
            "300x100+1200+700"
        )

        tk.Label(
            popup,
            text=message
        ).pack(
            expand=True
        )

        popup.after(
            5000,
            popup.destroy
        )