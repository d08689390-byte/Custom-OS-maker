class WindowManager:

    def __init__(self):
        self.windows = []

    def register(self, app):
        self.windows.append(app)

    def unregister(self, app):
        if app in self.windows:
            self.windows.remove(app)

    def close_all(self):
        for app in self.windows[:]:
            if hasattr(app, "window") and app.window.winfo_exists():
                app.window.destroy()
        self.windows.clear()

    def close_all_windows(self):
        self.close_all()

    def minimise(self, window):
        window.iconify()

    def maximise(self, window):
        window.state("zoomed")

    def restore(self, window):
        window.state("normal")
