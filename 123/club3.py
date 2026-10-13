Python 3.15.0 (tags/v3.15.0:d220409, Oct  9 2026, 11:55:56) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> class Tariff:
...     """Тарифная сетка: цена за минуту, скидки по длительности и т.п."""
... 
...     def __init__(self, price_per_minute: float, discount_rules: dict | None = None):
...         """
...         price_per_minute — стоимость одной минуты.
...         discount_rules — словарь вида {min_minutes: percent_discount}
...         Пример: {60: 5, 180: 10} — от 60 минут скидка 5%, от 180 — 10%.
...         """
...         self.price_per_minute = price_per_minute
...         self.discount_rules = discount_rules or {}
... 
...     def calculate_cost(self, minutes: int) -> float:
...         base = minutes * self.price_per_minute
...         discount = 0.0
...         for min_minutes, percent in sorted(self.discount_rules.items(), reverse=True):
...             if minutes >= min_minutes:
...                 discount = percent / 100.0
...                 break
...         return base * (1 - discount)
