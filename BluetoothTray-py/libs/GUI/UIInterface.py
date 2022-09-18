from __future__ import annotations
from typing import Final as const, Callable

from pystray import Icon
from PIL import Image

from abstractGUI import AbsUI



"""_summary_
UI機能の実装統合クラス。
メインのUIを定義する。
"""
class UIInterface(AbsUI):
    
    def __init__(self, scran_devices: list[str]) -> None:
        super().__init__(scran_devices)
        self._icon_image = Image.open("BluetoothTray-py/libs/bin/bluetooth-b.ico")
        #TODO:メニューの実装
        self._app_icon = Icon("BluetoothTray", self._icon_image, "BluetoothTray")
    
    
    def start_application(self) -> None:
        """_summary_
        run()メソッドを実行し、アプリケーションを起動する。
        """
        self._app_icon.run()
        
    def addEventListener(self, event: str, callback: Callable) -> None:
        pass


#TEST

if __name__ == "__main__":
    ui = UIInterface(["test1", "test2"])
    ui.start_application()