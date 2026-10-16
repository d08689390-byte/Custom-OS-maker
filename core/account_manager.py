import json
import os


class AccountManager:

    FILE = "accounts.json"

    def __init__(self):

        if not os.path.exists(
            self.FILE
        ):

            default = {

                "owner": {

                    "username":
                    "owner",

                    "password":
                    "admin"
                },

                "allow_extra_users":
                False,

                "users": {

                    "example@codeosdev.coder": {
                        "password":
                        "1234Code@"
                    }
                }
            }

            with open(
                self.FILE,
                "w"
            ) as f:

                json.dump(
                    default,
                    f,
                    indent=4
                )

    def authenticate(
        self,
        username,
        password
    ):

        with open(self.FILE) as f:

            data = json.load(f)

        owner = data["owner"]

        if (
            username == owner["username"]
            and
            password == owner["password"]
        ):
            return True

        if data[
            "allow_extra_users"
        ]:

            users = data["users"]

            if username in users:

                return (
                    users[username]
                    ["password"]
                    == password
                )

        return False