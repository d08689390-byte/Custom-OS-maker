class ThemeManager:

    THEMES = {

        "matrix": {
            "background": "#001100",
            "foreground": "#00FF00",
            "taskbar": "#002200"
        },

        "dark": {
            "background": "#1e1e1e",
            "foreground": "#ffffff",
            "taskbar": "#333333"
        }
    }

    def __init__(self):

        self.current_theme = "matrix"

    def get(self):

        return self.THEMES[
            self.current_theme
        ]

    def set_theme(self, name):

        if name in self.THEMES:
            self.current_theme = name