import os

from core.desktop import CodeOS
from apps.setup_wizard import SetupWizard


if __name__ == "__main__":

    os_app = CodeOS()

    if not os.path.exists(
        "accounts.json"
    ):

        SetupWizard(
            os_app.root
        )

def run(self):
        self.root.mainloop()




        os_app.run()