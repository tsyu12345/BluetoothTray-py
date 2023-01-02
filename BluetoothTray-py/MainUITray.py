from __future__ import annotations
from typing import Final as const, Callable
from pystray import Icon, MenuItem, Menu
from PIL import Image

from .UIInterface import AbsUI
from .libs.BLE.abstractBLE import IConnectedDeviceInfo, IResultConnection
from .libs.BLE.BluetoothConnection import BLEConnection



"""_summary_
UI機能の実装統合クラス。
メインのUIを定義する。
"""
class MainUITray(AbsUI):
    
    ICON_SRC_PATH: const[str] = "BluetoothTray-py/libs/bin/bluetooth-b.ico"
    APP_NAME: const[str] = "BluetoothTray"
    
    def __init__(self) -> None: #TODO:デバイス情報の型定義を読む
        super().__init__()
        self._icon_image = Image.open(self.ICON_SRC_PATH)
        #TODO:メニューの実装
        self._app_icon: Icon
        self._tray_menu: Menu
        
        self.scanned_devices: list[IConnectedDeviceInfo]
        
        self.BLE = BLEConnection()
        
        
        
    
    def __init_event_handlers(self) -> None:
        """_summary_
        各イベントハンドラの初期化ラッパー関数
        """
        #self.create_item_obj("test", False, self.test)
        self.create_item_obj("Quit BluetoothTray", True, self.kill_application_event) #アプリケーション終了用
        
        

    def start_application(self) -> None:
        """_summary_
        run()メソッドを実行し、アプリケーションを起動する。
        各種初期化をおこなう。
        """ 
        #init icon and UI
        self._tray_menu = Menu(*self._menu_items.values())
        self._app_icon = Icon(name=self.APP_NAME, icon=self._icon_image, title=self.APP_NAME, menu=self._tray_menu)
        
        #run app
        self._app_icon.run()
        
        #scan devices
        self.scanned_devices = self.BLE.scan_devices()
        print(self.scanned_devices)
        #init UI Event handlers
        self.__init_event_handlers()
        #self.connection_event()
        
    
    def kill_application_event(self) -> None:
        """_summary_
        アプリケーションを終了する。
        また、その時のイベントハンドラ。        
        """
        self._app_icon.stop()
        #todo:接続済み情報を保持
    
    
    def connection_event(self, device_info:IConnectedDeviceInfo) -> None:
        """_summary_
        指定のデバイスに接続する。
        """
        result:IResultConnection = self.BLE.try_connection(device_info)
        
        match result:
            
            case IResultConnection.SUCCESS:
                #todo:指定のデバイス名があるUI部分に接続済みアイコンを表示させる。
                print("CONNECTION OK")
            
            case IResultConnection.FAILED:
                print("CONNECTION FAILED")
            
            case IResultConnection.TIMEOUT:
                print("CONNECTION TIMEOUT")
                
                
    def create_device_menu(self) -> None:
        """_summary_\n
        検出したデバイス、ペアリング済みデバイスのメニューを生成する。
        """
        for device in self.scanned_devices:
            super().create_item_obj(device.name, False, self.connection_event) #todo:デバイス情報の受け渡し
    