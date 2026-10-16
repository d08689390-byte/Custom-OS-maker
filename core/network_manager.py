class NetworkManager:

    def __init__(self):

        self.connected = True

        self.network_name = (
            "CodeOS Ethernet"
        )

    def get_status(self):

        return {
            "connected":
                self.connected,

            "name":
                self.network_name
        }