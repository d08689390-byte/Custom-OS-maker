import json
import os


class IconLayoutManager:

    FILE_PATH = "user/icon_layout.json"

    def __init__(self):

        os.makedirs(
            "user",
            exist_ok=True
        )

        if not os.path.exists(
            self.FILE_PATH
        ):
            self.save_layout({})

    def load_layout(self):

        try:
            with open(
                self.FILE_PATH,
                "r"
            ) as file:

                return json.load(file)

        except Exception:

            return {}

    def save_layout(
        self,
        layout
    ):

        with open(
            self.FILE_PATH,
            "w"
        ) as file:

            json.dump(
                layout,
                file,
                indent=4
            )

    def get_position(
        self,
        icon_name
    ):

        layout = self.load_layout()

        return layout.get(
            icon_name,
            {
                "x": 50,
                "y": 50
            }
        )

    def update_position(
        self,
        icon_name,
        x,
        y
    ):

        layout = self.load_layout()

        layout[icon_name] = {
            "x": x,
            "y": y
        }

        self.save_layout(layout)

    def remove_icon(
        self,
        icon_name
    ):

        layout = self.load_layout()

        if icon_name in layout:
            del layout[icon_name]

        self.save_layout(layout)