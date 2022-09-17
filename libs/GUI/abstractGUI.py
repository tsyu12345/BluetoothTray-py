from __future__ import annotations
from typing import Final as const 
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
    def show_devices(self) -> None:
        """_summary_\n
        検出したデバイスの一覧を表示する\n
        """
        pass
    
    @abstractmethod
    def connect(self) -> None:
        """_summary_\n
        指定デバイスへBluetooth接続を試みる\n
        """
        pass
    
    @abstractmethod
    def disconnect(self) -> None:
        """_summary_\n
        接続中のデバイスとのBluetooth接続を切断する\n
        """
        pass
    
    
    @abstractmethod
    def save_devices(self) -> None:
        """_summary_\n
        過去にデバイス情報を保存する\n
        """
        pass
    
    @abstractmethod
    def load_devices(self) -> None:
        """_summary_\n
        過去に保存したデバイス情報を読み込む\n
        """
        pass
    
    
    