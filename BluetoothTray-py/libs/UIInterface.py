from __future__ import annotations
from typing import Final as const, Callable

from pystray import Icon, MenuItem, Menu
from PIL import Image

from abstractGUI import AbsUI



"""_summary_
UI機能の実装統合クラス。
メインのUIを定義する。
"""
class MainUITray(AbsUI):
    
    ICON_SRC_PATH: const[str] = "BluetoothTray-py/libs/bin/bluetooth-b.ico"
    APP_NAME: const[str] = "BluetoothTray"
    
    def __init__(self, scran_devices: list[str]) -> None:
        super().__init__(scran_devices)
        self._icon_image = Image.open(self.ICON_SRC_PATH)
        #TODO:メニューの実装
        self._app_icon: Icon
        self._tray_menu: Menu
    
    
    def start_application(self) -> None:
        """_summary_
        run()メソッドを実行し、アプリケーションを起動する。
        """
        self._tray_menu = Menu(*self._menu_items.values())
        self._app_icon = Icon(self.APP_NAME, self._icon_image, self.APP_NAME, self._tray_menu)
        self._app_icon.run()
        
    
    def kill_application(self) -> None:
        """_summary_
        アプリケーションを終了する。
        """
        self._app_icon.stop()
        
    
    def create_item_obj(self, text: str, callback: Callable) -> None:
        self._menu_items[text] = MenuItem(text, callback)
        
    
    def remove_item_obj(self, text: str) -> None:
        self._menu_items.pop(text)
        
        
    

#TEST

if __name__ == "__main__":
    #ui = UIInterface(["test1", "test2"])
    #ui.start_application()
    test = MainUITray(["test1", "test2"])
    test.start_application()