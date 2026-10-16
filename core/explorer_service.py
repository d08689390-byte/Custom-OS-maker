class ExplorerService:

    PROCESS_NAME = "CodeOS Explorer"

    def __init__(
        self,
        os_instance
    ):

        self.os = os_instance

        self.explorer = None

    def start(self):

        from core.explorer import (
            CodeOSExplorer
        )

        self.explorer = (
            CodeOSExplorer(
                self.os
            )
        )

    def restart(self):

        if self.explorer:

            self.explorer.desktop.destroy()

            self.explorer.taskbar.destroy()

        self.start()