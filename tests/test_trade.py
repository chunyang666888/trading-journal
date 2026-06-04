from datetime import date

from journal.trade import Trade


def test_long_pnl():
    t = Trade("600519", "LONG", 1000, 1100, 10, date(2026, 8, 1))
    assert t.pnl == 1000.0
    assert abs(t.return_pct - 0.1) < 1e-9


def test_short_pnl():
    t = Trade("600519", "SHORT", 1000, 900, 10, date(2026, 8, 1))
    assert t.pnl == 1000.0
