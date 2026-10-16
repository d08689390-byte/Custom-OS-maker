import os


class VirtualFileSystem:

    ROOT = "user"

    def __init__(self):

        self.setup()

    def setup(self):

        folders = [
            "user",
            "user/documents",
            "user/downloads",
            "user/desktop",
            "user/recycle_bin"
        ]

        for path in folders:
            os.makedirs(path, exist_ok=True)

    def list_directory(self, path):

        return os.listdir(path)

    def create_file(
        self,
        path,
        content=""
    ):

        with open(path, "w") as f:
            f.write(content)

    def read_file(self, path):

        with open(path) as f:
            return f.read()
        shutil.move(
    path,
    "user/recycle_bin"
)