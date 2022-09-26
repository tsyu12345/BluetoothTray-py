from __future__ import annotations
from typing import Final as const , Callable
from abc import ABC, abstractmethod

from pystray import MenuItem

class AbsUI(ABC):
    
    def __init__(self, devices:list) -> None:
        """_summary_\n
        UIクラスの基底クラス\n
        UI基本機能の定義\n
        """
        self._menu_items: dict[str, MenuItem] = {}
        self.devices = devices
    
    
    def create_item_obj(self, text: str, bold_font:bool,callback: Callable) -> None:
        """_summary_\n
        メニュー項目のオブジェクトを生成する。\n
        同時にそのオブジェクトのクリックイベントハンドラを設定する。\n
        Args:
            text (str): 表示テキスト\n
            bold_font (bool): フォントを太字にするかどうか\n
            callback (Callable): コールバック関数\n
        """
        self._menu_items[text] = MenuItem(text, callback, checked=None, default=False, visible=True, enabled=True)
        
    
    def remove_item_obj(self, text: str) -> None:
        """_summary_\n
        指定のテキストを持つメニュー項目を削除する。\n
        """
        self._menu_items.pop(text)
    
    