import tkinter as tk

from window_manager import WindowManager
from process_manager import ProcessManager
from virtual_filesystem import VirtualFileSystem
from theme_manager import ThemeManager
from package_manager import PackageManager
from account_manager import AccountManager
from network_manager import NetworkManager
from sound_manager import SoundManager
from notification_center import NotificationCenter
from wallpaper_manager import WallpaperManager
from app_registry import AppRegistry
from explorer_service import ExplorerService



class CodeOS:

    def __init__(self):

        self.root = tk.Tk()

        self.window_manager = WindowManager()
        self.process_manager = ProcessManager()
        self.filesystem = VirtualFileSystem()
        self.theme_manager = ThemeManager()
        self.package_manager = PackageManager()
        self.account_manager = AccountManager()

        self.network_manager = NetworkManager()
        self.sound_manager = SoundManager()

        self.notification_center = (
            NotificationCenter(self)
        )

        self.wallpaper_manager = (
            WallpaperManager()
        )

        self.explorer_service = ExplorerService(self)

        self.registry = AppRegistry()

        self.register_apps()

    def register_apps(self):
        """Register applications with the application registry."""
        return None