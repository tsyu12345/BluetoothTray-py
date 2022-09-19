from __future__ import annotations
from typing import Final as const , Callable
from abc import ABC, abstractmethod

from pystray import MenuItem

class AbsUI(ABC):
    
    def __init__(self, devices:list) -> None:
        """_summary_\n
        UIクラスの抽象クラス\n
        UI基本機能の定義\n
        """
        self._menu_items: dict[str, MenuItem] = {}
        self.devices = devices
    
    
    @abstractmethod
    def create_item_obj(self, text:str, callback:Callable) -> None:
        """_summary_\n
        クラスで使用するMenuItemオブジェクトを生成する。\n
        """
        pass
    
    @abstractmethod
    def remove_item_obj(self, text:str) -> None:
        """_summary_\n
        クラスで使用するMenuItemオブジェクトを削除する。\n
        """
        pass
    """
    @abstractmethod
    def show_devices(self) -> None:
        
    
    @abstractmethod
    def connect(self) -> None:
    
    
    @abstractmethod
    def disconnect(self) -> None:
        
    
    
    @abstractmethod
    def save_devices(self) -> None:

    
    @abstractmethod
    def load_devices(self) -> None:
    
    """
    
    