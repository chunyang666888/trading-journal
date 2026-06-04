from datetime import date

from journal.ledger import Ledger
from journal.review import best_trade, mistake_attribution, review, worst_trade
from journal.trade import Trade


def test_review():
    l = Ledger()
    l.add_many(
        [
            Trade("A", "LONG", 100, 110, 10, date(2026, 1, 1)),
            Trade("B", "LONG", 50, 40, 10, date(2026, 1, 2), emotion="贪婪"),
        ]
    )
    r = review(l)
    assert "总盈亏" in r and "胜率" in r
    assert best_trade(l).symbol == "A"
    assert worst_trade(l).symbol == "B"
    assert mistake_attribution(l) == {"贪婪": 1}
