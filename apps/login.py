import tkinter as tk


class LoginWindow:

    def __init__(
        self,
        root,
        account_manager,
        success_callback
    ):

        self.root = root

        self.accounts = (
            account_manager
        )

        self.success = (
            success_callback
        )

        self.frame = tk.Frame(
            root
        )

        self.frame.pack(
            expand=True
        )

        tk.Label(
            self.frame,
            text="CodeOS Login"
        ).pack()

        self.username = tk.Entry(
            self.frame
        )

        self.username.pack()

        self.password = tk.Entry(
            self.frame,
            show="*"
        )

        self.password.pack()

        tk.Button(
            self.frame,
            text="Login",
            command=self.login
        ).pack()

    def login(self):

        if self.accounts.authenticate(
            self.username.get(),
            self.password.get()
        ):

            self.frame.destroy()

            self.success()