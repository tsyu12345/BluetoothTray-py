from __future__ import annotations
from typing import Final as const

from abstractGUI import AbsUI

"""_summary_
UI機能の実装統合クラス。
"""
class UIInterface(AbsUI):
    
    def __init__(self, scran_devices: list[str]) -> None:
        super().__init__(scran_devices)
    

