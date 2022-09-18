from __future__ import annotations
from typing import Final as const , Callable
from abc import ABC, abstractmethod

class AbsUI(ABC):
    
    def __init__(self, scran_devices:list[str]) -> None:
        """_summary_\n
        UIクラスの抽象クラス\n
        UI基本機能の定義\n
        Args:\n
            scran_devices (list[str]): 検出済みのbluetoothデバイス名\n #NOTE:将来的に型は変更される可能性あり
        """
    @abstractmethod
    def addEventListener(self, event: str, callback: Callable) -> None:
        """_summary_\n
        イベントリスナーの追加\n
        Args:\n
            event (str): イベント名\n
            callback (callable): コールバック関数\n
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
    
    