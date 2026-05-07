"""交易账本与绩效统计。"""
from __future__ import annotations

from typing import List

from .trade import Trade


class Ledger:
    def __init__(self) -> None:
        self.trades: List[Trade] = []

    def add(self, trade: Trade) -> None:
        self.trades.append(trade)

    def add_many(self, trades: List[Trade]) -> None:
        self.trades.extend(trades)

    @property
    def num_trades(self) -> int:
        return len(self.trades)

    @property
    def total_pnl(self) -> float:
        return sum(t.pnl for t in self.trades)

    @property
    def win_rate(self) -> float:
        if not self.trades:
            return 0.0
        wins = sum(1 for t in self.trades if t.pnl > 0)
        return wins / len(self.trades)

    @property
    def gross_profit(self) -> float:
        return sum(t.pnl for t in self.trades if t.pnl > 0)

    @property
    def gross_loss(self) -> float:
        return sum(-t.pnl for t in self.trades if t.pnl < 0)

    @property
    def profit_factor(self) -> float:
        gl = self.gross_loss
        if gl == 0:
            return float("inf") if self.gross_profit > 0 else 0.0
        return self.gross_profit / gl

    @property
    def expectancy(self) -> float:
        if not self.trades:
            return 0.0
        return self.total_pnl / len(self.trades)
