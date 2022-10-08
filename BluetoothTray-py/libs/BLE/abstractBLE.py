from __future__ import annotations
from typing import Final as const , Callable
from abc import ABC, abstractmethod

from enum import Enum
import asyncio
from asyncio import AbstractEventLoop



class IConnectedDeviceInfo:
    
    def __init__(self, MAC_address:str, device_name:str, RSSI_value: int|None = None) -> None:
        """_summary_\n
        接続されたBluetoothデバイスから得られる情報を提供するインタフェース\n
        Args:
            mac_address (str): デバイスのMACアドレス\n
            device_name (str): デバイスの名前\n
            RSSI_value (str|None): デバイスのRSSI値\n
        """
        self.MAC_address: str      = MAC_address
        self.name: str             = device_name 
        self.RSSI_value:  int|None = RSSI_value
        
class IResultConnection(Enum):
    """_summary_\n
    接続結果を表す列挙型\n
    """
    SUCCESS: const  = 1
    FAILED: const   = -1
    TIMEOUT: const  = 0


class AbsBLEConnection(ABC):
    
    def __init__(self) -> None:
        """_summary_\n
        BLEを行う、抽象基底クラス\n
        """
        self.loop: AbstractEventLoop = asyncio.get_event_loop()
        
    
    
    @abstractmethod
    def scan_devices(self) -> list[IConnectedDeviceInfo]:
        """_summary_\n
        付近のBluetoothデバイスをスキャンする。\n
        return: list[IConnectedDeviceInfo]\n
        """
        pass
        
    @abstractmethod
    def try_connection(self, device_info:IConnectedDeviceInfo) -> IResultConnection:
        """_summary_\n
        指定のデバイスに接続を試みる。\n
        Args:\n
            device_info (IConnectedDeviceInfo): 接続を試みるデバイスの情報\n
        
        Returns:\n
            IResultConnection: 接続結果のオブジェクト\n
        """
        pass