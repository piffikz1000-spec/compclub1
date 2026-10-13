Python 3.15.0 (tags/v3.15.0:d220409, Oct  9 2026, 11:55:56) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> @dataclass
... class User:
...     id: int
...     username: str
...     email: str
...     balance_rub: float = 0.0
...     is_active: bool = True
... 
...     def pay(self, amount: float) -> None:
...         if amount < 0:
...             raise ValueError("Сумма оплаты не может быть отрицательной.")
...         if self.balance_rub < amount:
...             raise ClubError("Недостаточно средств на балансе.")
...         self.balance_rub -= amount
... 
...     def top_up(self, amount: float) -> None:
...         if amount <= 0:
...             raise ValueError("Пополнение должно быть положительным.")
...         self.balance_rub += amount
