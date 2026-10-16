import tkinter as tk
import json
import os


class SetupWizard:

    def __init__(
        self,
        root
    ):

        self.root = root

        self.window = tk.Toplevel(
            root
        )

        self.window.title(
            "CodeOS Setup Wizard"
        )

        self.window.geometry(
            "600x400"
        )

        self.window.resizable(
            False,
            False
        )

        self.page = 0

        self.owner_username = ""
        self.owner_password = ""

        self.allow_extra_users = False

        self.theme = "matrix"

        self.container = tk.Frame(
            self.window
        )

        self.container.pack(
            fill=tk.BOTH,
            expand=True
        )

        self.show_page_0()

    def clear(self):

        for widget in (
            self.container.winfo_children()
        ):
            widget.destroy()

    def next_page(self):

        self.page += 1

        {
            1: self.show_page_1,
            2: self.show_page_2,
            3: self.show_page_3,
            4: self.show_page_4
        }[self.page]()

    def show_page_0(self):

        self.clear()

        tk.Label(
            self.container,
            text="Welcome to CodeOS",
            font=("Arial", 24)
        ).pack(
            pady=30
        )

        tk.Label(
            self.container,
            text=
            "Let's prepare your desktop."
        ).pack()

        tk.Button(
            self.container,
            text="Start Setup",
            command=self.next_page
        ).pack(
            pady=20
        )

    def show_page_1(self):

        self.clear()

        tk.Label(
            self.container,
            text="Owner Account",
            font=("Arial", 20)
        ).pack(
            pady=10
        )

        tk.Label(
            self.container,
            text="Username"
        ).pack()

        username = tk.Entry(
            self.container
        )

        username.pack()

        tk.Label(
            self.container,
            text="Password"
        ).pack()

        password = tk.Entry(
            self.container,
            show="*"
        )

        password.pack()

        def continue_setup():

            self.owner_username = (
                username.get()
            )

            self.owner_password = (
                password.get()
            )

            self.next_page()

        tk.Button(
            self.container,
            text="Continue",
            command=continue_setup
        ).pack(
            pady=15
        )

    def show_page_2(self):

        self.clear()

        tk.Label(
            self.container,
            text="Additional Users"
        ).pack(
            pady=20
        )

        allow_var = tk.BooleanVar()

        tk.Checkbutton(
            self.container,
            text=
            "Allow additional accounts",
            variable=allow_var
        ).pack()

        def continue_setup():

            self.allow_extra_users = (
                allow_var.get()
            )

            self.next_page()

        tk.Button(
            self.container,
            text="Continue",
            command=continue_setup
        ).pack(
            pady=20
        )

    def show_page_3(self):

        self.clear()

        tk.Label(
            self.container,
            text="Choose Theme"
        ).pack(
            pady=20
        )

        theme_var = tk.StringVar(
            value="matrix"
        )

        for theme in [
            "matrix",
            "dark",
            "light"
        ]:

            tk.Radiobutton(
                self.container,
                text=theme.title(),
                variable=theme_var,
                value=theme
            ).pack()

        def continue_setup():

            self.theme = (
                theme_var.get()
            )

            self.next_page()

        tk.Button(
            self.container,
            text="Continue",
            command=continue_setup
        ).pack(
            pady=20
        )

    def show_page_4(self):

        self.clear()

        tk.Label(
            self.container,
            text="Setup Complete",
            font=("Arial", 22)
        ).pack(
            pady=25
        )

        tk.Label(
            self.container,
            text=
            "CodeOS is ready."
        ).pack()

        def finish():

            self.save_accounts()

            self.window.destroy()

        tk.Button(
            self.container,
            text="Launch CodeOS",
            command=finish
        ).pack(
            pady=20
        )

    def save_accounts(self):

        data = {

            "owner": {

                "username":
                self.owner_username,

                "password":
                self.owner_password
            },

            "allow_extra_users":
            self.allow_extra_users,

            "users": {}
        }

        with open(
            "accounts.json",
            "w"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

        os.makedirs(
            "user",
            exist_ok=True
        )

        with open(
            "settings.json",
            "w"
        ) as file:

            json.dump(
                {
                    "theme":
                    self.theme
                },
                file,
                indent=4
            )