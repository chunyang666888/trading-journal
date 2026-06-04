from datetime import date

from journal.ledger import Ledger
from journal.trade import Trade


def _ledger() -> Ledger:
    l = Ledger()
    l.add_many(
        [
            Trade("A", "LONG", 100, 110, 10, date(2026, 1, 1)),
            Trade("B", "LONG", 50, 40, 10, date(2026, 1, 2), emotion="贪婪"),
            Trade("C", "SHORT", 200, 180, 5, date(2026, 1, 3)),
        ]
    )
    return l


def test_stats():
    l = _ledger()
    assert l.num_trades == 3
    assert l.total_pnl == 100.0  # A:100, B:-100, C:100
    assert abs(l.win_rate - 2 / 3) < 1e-9


def test_profit_factor():
    l = _ledger()
    # 毛利 200，毛损 100 -> 盈亏比 2
    assert abs(l.profit_factor - 2.0) < 1e-9


def test_expectancy():
    l = _ledger()
    assert abs(l.expectancy - 100 / 3) < 1e-9
