from __future__ import annotations
from typing import Final as const, Callable

from pystray import Icon, MenuItem, Menu
from PIL import Image

from UIInterface import AbsUI



"""_summary_
UI機能の実装統合クラス。
メインのUIを定義する。
"""
class MainUITray(AbsUI):
    
    ICON_SRC_PATH: const[str] = "BluetoothTray-py/libs/bin/bluetooth-b.ico"
    APP_NAME: const[str] = "BluetoothTray"
    
    def __init__(self) -> None: #TODO:デバイス情報の型定義を読む
        #super().__init__(scran_devices)
        self._icon_image = Image.open(self.ICON_SRC_PATH)
        #TODO:メニューの実装
        self._app_icon: Icon
        self._tray_menu: Menu 
        
    
    def __init_event_handlers(self) -> None:
        """_summary_
        各イベントハンドラの初期化ラッパー関数
        """
        #self.create_item_obj("test", False, self.test)
        self.create_item_obj("Quit BluetoothTray", True, self.kill_application) #アプリケーション終了用
        
        
    
    
    def start_application(self) -> None:
        """_summary_
        run()メソッドを実行し、アプリケーションを起動する。
        """
        self.__init_event_handlers()
        self._tray_menu = Menu(*self._menu_items.values())
        self._app_icon = Icon(name=self.APP_NAME, icon=self._icon_image, title=self.APP_NAME, menu=self._tray_menu)
        self._app_icon.run()
        
    
    def kill_application(self) -> None:
        """_summary_
        アプリケーションを終了する。
        また、その時のイベントハンドラ。        
        """
        self._app_icon.stop()
    
    
    def connection_to_device(self, device_name: str) -> None:
        """_summary_
        指定のデバイスに接続する。
        """
        #TODO:BLE側での実装を呼び出す形にする。
        pass
    

#TEST

if __name__ == "__main__":
    #ui = UIInterface(["test1", "test2"])
    #ui.start_application()
    pass