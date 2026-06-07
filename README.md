# trading-journal

![tests](https://github.com/chunyang666888/trading-journal/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![pytest](https://img.shields.io/badge/tests-pytest-0A8A4A?logo=pytest&logoColor=white)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)

**传统交易员日志与复盘工具** —— 记录每笔交易（标的 / 方向 / 买卖点 / 数量 / 理由 / 情绪），自动计算胜率、盈亏比、期望值等绩效，并生成复盘与失误归因，帮助交易员沉淀盘感、纠正纪律。零第三方依赖。

## ✨ 功能

- **交易记录** (`trade.Trade`)：结构化单笔交易，自动算盈亏与收益率（多 / 空双向）。
- **账本统计** (`ledger.Ledger`)：交易笔数、总盈亏、胜率、盈亏比（profit factor）、期望值（expectancy）。
- **复盘归因** (`review`)：最佳 / 最差交易，按情绪标签统计失误频次（贪婪 / 恐惧 / 追高 …）。

## 📦 安装

```bash
pip install -e .
pip install pytest   # 仅测试
```

## 🚀 快速开始

```python
from datetime import date
from journal.ledger import Ledger
from journal.trade import Trade
from journal.review import review

ledger = Ledger()
ledger.add(Trade("600519", "LONG", 1700, 1850, 100, date(2026, 7, 1),
                 reason="业绩超预期", emotion="纪律"))
print(review(ledger))
```

离线演示见 [`examples/journal_demo.py`](examples/journal_demo.py)。

## 🧪 测试

```bash
pytest -q
```

| 模块 | 覆盖点 |
|------|--------|
| `trade`    | 多 / 空盈亏与收益率 |
| `ledger`   | 胜率、盈亏比、期望值 |
| `review`   | 最佳 / 最差、失误归因 |

## 🗂 目录

```
journal/
├── trade.py    # 单笔交易
├── ledger.py   # 账本与绩效统计
└── review.py   # 复盘与归因
tests/          # pytest 用例
examples/       # 离线演示
```

## 📄 License

MIT — free for personal and commercial use.
