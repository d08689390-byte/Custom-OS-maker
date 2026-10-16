class AppRegistry:

    def __init__(self):
        self.apps = {}

    def register(
        self,
        name,
        app_class
    ):
        self.apps[name] = app_class

    def launch(
        self,
        name,
        os_instance
    ):
        if name not in self.apps:
            return None

        app_factory = self.apps[name]

        if isinstance(app_factory, type):
            app = app_factory(os_instance)
        else:
            app = app_factory

        if hasattr(app, "window"):
            os_instance.window_manager.register(app)

        return app