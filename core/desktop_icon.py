import tkinter as tk


class DesktopIcon:

    def __init__(
        self,
        canvas,
        x,
        y,
        text,
        command
    ):

        self.canvas = canvas

        self.text = canvas.create_text(
            x,
            y,
            text=text,
            fill="#00FF00"
        )

        self.command = command

        canvas.tag_bind(
            self.text,
            "<Double-1>",
            self.launch
        )

    def launch(
            self,
        event
    ):
        self.command()