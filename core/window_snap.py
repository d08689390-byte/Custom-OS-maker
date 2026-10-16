class WindowSnap:

    @staticmethod
    def snap_left(window):

        width = (
            window.winfo_screenwidth()
        )

        height = (
            window.winfo_screenheight()
        )

        window.geometry(
            f"{width//2}x{height}+0+0"
        )

    @staticmethod
    def snap_right(window):

        width = (
            window.winfo_screenwidth()
        )

        height = (
            window.winfo_screenheight()
        )

        window.geometry(
            f"{width//2}x{height}+"
            f"{width//2}+0"
        )

    @staticmethod
    def snap_top(window):

        width = (
            window.winfo_screenwidth()
        )

        height = (
            window.winfo_screenheight()
        )

        window.geometry(
            f"{width}x{height//2}+0+0"
        )

    @staticmethod
    def maximise(window):

        try:
            window.state("zoomed")

        except Exception:

            width = (
                window.winfo_screenwidth()
            )

            height = (
                window.winfo_screenheight()
            )

            window.geometry(
                f"{width}x{height}+0+0"
            )

    @staticmethod
    def minimise(window):

        window.iconify()

    @staticmethod
    def restore(window):

        window.state("normal")

    @staticmethod
    def toggle_always_on_top(window):

        current = bool(
            window.attributes(
                "-topmost"
            )
        )

        window.attributes(
            "-topmost",
            not current
        )