Python 3.15.0 (tags/v3.15.0:d220409, Oct  9 2026, 11:55:56) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> @dataclass
... class Session:
...     computer_id: int
...     user_id: int
...     start_time: datetime
...     duration_minutes: int
...     end_time: datetime = field(init=False)
...     cost_rub: float = field(default=0.0)
... 
...     def __post_init__(self):
...         self.end_time = self.start_time + timedelta(minutes=self.duration_minutes)
... 
...     def finalize(self, tariff: Tariff) -> float:
...         minutes_used = (self.end_time - self.start_time).total_seconds() // 60
...         self.cost_rub = tariff.calculate_cost(int(minutes_used))
...         return self.cost_rub
