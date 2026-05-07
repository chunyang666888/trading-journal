"""单笔交易记录。"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Trade:
    symbol: str
    side: str  # "LONG" / "SHORT"
    entry: float
    exit: float
    qty: float
    trade_date: date
    reason: str = ""
    emotion: str = ""  # 纪律 / 恐惧 / 贪婪 / 追高 ...

    @property
    def pnl(self) -> float:
        direction = 1 if self.side.upper() == "LONG" else -1
        return direction * (self.exit - self.entry) * self.qty

    @property
    def return_pct(self) -> float:
        direction = 1 if self.side.upper() == "LONG" else -1
        return direction * (self.exit - self.entry) / self.entry
