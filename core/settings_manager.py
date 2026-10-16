import json


class SettingsManager:

    FILE = "settings.json"

    def load(self):

        try:

            with open(
                self.FILE
            ) as f:

                return json.load(f)

        except Exception:

            return {}

    def save(self, data):

        with open(
            self.FILE,
            "w"
        ) as f:

            json.dump(
                data,
                f,
                indent=4
            )