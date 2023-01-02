from __future__ import annotations
from typing import Final as const , Callable


from bleak import discover
import bleak.backends.winrt.client as BLEClient
import json

from .abstractBLE import AbsBLEConnection, IConnectedDeviceInfo, IResultConnection

class BLEConnection(AbsBLEConnection):
    
    def __init__(self) -> None:
        super()
        self.devices: list[IConnectedDeviceInfo] = []
        
    #private method
    async def __scan(self) -> list[IConnectedDeviceInfo]:
        """_summary_\n
        デバイスをスキャンするプライベートメソッド\n
        Returns:
            list[IConnectedDeviceInfo]: 検出したデバイス情報のリスト
        #todo :例外処理の追加
        """
        discovered_devices = await discover() #FIXME :Deprecated
        devices_list:list[IConnectedDeviceInfo] = []
        
        for i, device in enumerate(discovered_devices):
            info = IConnectedDeviceInfo(
                device.address, 
                device.name, 
                device.rssi
            )
            devices_list.append(info)
        
        return devices_list
    
    
    #private method
    async def __connect(self, destination:IConnectedDeviceInfo) -> IResultConnection:
        """_summary_\n
        指定のデバイスに接続するプライベートメソッド\n
        #todo :例外処理の追加
        """
        
        mac_address: const[str] = destination.MAC_address #接続先デバイスのMACアドレス

        async with BLEClient.BleakClientWinRT(mac_address) as client: #FIXME :with文抜ける（接続完了時）に切断されちゃう？：要検証
            is_connected: const[bool] = client.is_connected
            if is_connected:
                return IResultConnection.SUCCESS
            else:
                return IResultConnection.FAILED
    
    
    def save_json(self) -> None:
        """_summary_\n
        接続済みのデバイス情報をJSONファイルに保存するメソッド\n
        """
        with open("./connected_devices.json", "w") as file:
            json.dump(self.devices, file, indent=4)
    
    
    #implements abstract method
    def scan_devices(self) -> list[IConnectedDeviceInfo]:
        #TODO: 例外処理の追加
        devices: const[list[IConnectedDeviceInfo]] = self.loop.run_until_complete(self.__scan())
        
        return devices
    
    #implements abstract method
    def try_connection(self, device_info:IConnectedDeviceInfo) -> IResultConnection:
        #TODO: 例外処理の追加
        result:const[IResultConnection] = self.loop.run_until_complete(self.__connect(device_info))
        
        if result is IResultConnection.SUCCESS and device_info not in self.devices:
            self.devices.append(device_info)
            
        return result
        
        
        
        
        
        