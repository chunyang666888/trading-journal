"""复盘与失误归因。"""
from __future__ import annotations

from typing import Dict, Optional

from .ledger import Ledger
from .trade import Trade


def best_trade(ledger: Ledger) -> Optional[Trade]:
    if not ledger.trades:
        return None
    return max(ledger.trades, key=lambda t: t.pnl)


def worst_trade(ledger: Ledger) -> Optional[Trade]:
    if not ledger.trades:
        return None
    return min(ledger.trades, key=lambda t: t.pnl)


def mistake_attribution(ledger: Ledger) -> Dict[str, int]:
    """按亏损交易的情绪 / 错误标签统计失误频次。"""
    counts: Dict[str, int] = {}
    for t in ledger.trades:
        if t.pnl < 0 and t.emotion:
            counts[t.emotion] = counts.get(t.emotion, 0) + 1
    return counts


def review(ledger: Ledger) -> str:
    b, w = best_trade(ledger), worst_trade(ledger)
    lines = [
        f"交易笔数: {ledger.num_trades}",
        f"总盈亏: {ledger.total_pnl:.2f}",
        f"胜率: {ledger.win_rate:.1%}",
        f"盈亏比: {ledger.profit_factor}",
        f"期望值: {ledger.expectancy:.2f}",
        f"最佳交易: {b.symbol if b else '-'} ({b.pnl:.2f})",
        f"最差交易: {w.symbol if w else '-'} ({w.pnl:.2f})",
    ]
    ma = mistake_attribution(ledger)
    if ma:
        lines.append("失误归因: " + ", ".join(f"{k}×{v}" for k, v in ma.items()))
    return "\n".join(lines)
