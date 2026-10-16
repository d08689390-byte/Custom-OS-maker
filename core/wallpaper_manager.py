class WallpaperManager:

    def __init__(self):

        self.current_wallpaper = (
            "matrix"
        )

    def set_wallpaper(
        self,
        name
    ):

        self.current_wallpaper = name