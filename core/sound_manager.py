class SoundManager:

    def __init__(self):

        self.volume = 75

        self.muted = False

    def set_volume(
        self,
        value
    ):

        self.volume = value

    def toggle_mute(self):

        self.muted = (
            not self.muted
        )