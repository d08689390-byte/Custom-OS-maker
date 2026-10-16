import json
import os


class PackageManager:

    PACKAGE_DIR = "packages"

    def __init__(self):
        os.makedirs(
            self.PACKAGE_DIR,
            exist_ok=True
        )

    def install_coi(self, filepath):

        with open(filepath) as f:
            data = json.load(f)

        return data

    def verify_package(self, package):

        return package.get(
            "signed",
            False
        )