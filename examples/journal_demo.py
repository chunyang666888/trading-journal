"""离线演示：用 trading-journal 记录并复盘一段交易。"""
from datetime import date

from journal.ledger import Ledger
from journal.review import review
from journal.trade import Trade


def main():
    ledger = Ledger()
    ledger.add_many(
        [
            Trade("600519", "LONG", 1700, 1850, 100, date(2026, 7, 1), reason="业绩超预期", emotion="纪律"),
            Trade("000858", "LONG", 150, 138, 200, date(2026, 7, 8), reason="追高", emotion="贪婪"),
            Trade("300750", "SHORT", 220, 205, 150, date(2026, 7, 15), reason="技术破位", emotion="纪律"),
        ]
    )
    print(review(ledger))


if __name__ == "__main__":
    main()
