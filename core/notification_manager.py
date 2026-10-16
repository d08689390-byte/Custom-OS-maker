from tkinter import messagebox


class NotificationManager:

    def notify(
        self,
        title,
        message
    ):

        messagebox.showinfo(
            title,
            message
        )