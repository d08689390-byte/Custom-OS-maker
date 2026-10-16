import os
import shutil
from pathlib import Path


class VirtualFileSystem:

    ROOT = Path("user")

    def __init__(self):
        self.setup()

    def setup(self):
        folders = [
            self.ROOT,
            self.ROOT / "desktop",
            self.ROOT / "documents",
            self.ROOT / "downloads",
            self.ROOT / "recycle_bin",
            self.ROOT / "pictures",
            self.ROOT / "music",
            self.ROOT / "videos"
        ]

        for folder in folders:
            folder.mkdir(
                parents=True,
                exist_ok=True
            )

    # -------------------------
    # Directory Operations
    # -------------------------

    def list_directory(self, path="user"):
        try:
            return os.listdir(path)
        except FileNotFoundError:
            return []

    def create_directory(self, path):
        os.makedirs(
            path,
            exist_ok=True
        )

    def delete_directory(self, path):
        shutil.rmtree(
            path,
            ignore_errors=True
        )

    # -------------------------
    # File Operations
    # -------------------------

    def create_file(
        self,
        path,
        content=""
    ):
        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:
            file.write(content)

    def read_file(self, path):
        try:
            with open(
                path,
                "r",
                encoding="utf-8"
            ) as file:
                return file.read()

        except FileNotFoundError:
            return ""

    def write_file(
        self,
        path,
        content
    ):
        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:
            file.write(content)

    def append_file(
        self,
        path,
        content
    ):
        with open(
            path,
            "a",
            encoding="utf-8"
        ) as file:
            file.write(content)

    def delete_file(
        self,
        path
    ):
        recycle_bin = (
            self.ROOT /
            "recycle_bin"
        )

        if os.path.exists(path):

            filename = os.path.basename(
                path
            )

            destination = (
                recycle_bin /
                filename
            )

            shutil.move(
                path,
                destination
            )

    def delete_forever(
        self,
        path
    ):
        if os.path.exists(path):
            os.remove(path)

    # -------------------------
    # Recycle Bin
    # -------------------------

    def restore_file(
        self,
        filename,
        destination="user/documents"
    ):

        source = (
            self.ROOT /
            "recycle_bin" /
            filename
        )

        target = (
            Path(destination) /
            filename
        )

        if source.exists():
            shutil.move(
                source,
                target
            )

    def empty_recycle_bin(self):

        recycle = (
            self.ROOT /
            "recycle_bin"
        )

        for item in recycle.iterdir():

            if item.is_file():
                item.unlink()

            elif item.is_dir():
                shutil.rmtree(item)

    # -------------------------
    # Info
    # -------------------------

    def file_exists(
        self,
        path
    ):
        return os.path.exists(path)

    def get_file_size(
        self,
        path
    ):
        if os.path.exists(path):
            return os.path.getsize(path)

        return 0

    def get_recycle_bin_items(self):

        recycle = (
            self.ROOT /
            "recycle_bin"
        )

        return [
            item.name
            for item in recycle.iterdir()
        ]