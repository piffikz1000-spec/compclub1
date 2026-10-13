Python 3.15.0 (tags/v3.15.0:d220409, Oct  9 2026, 11:55:56) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> from enum import Enum, auto
... from dataclasses import dataclass, field
... from datetime import datetime, timedelta
... from typing import Optional, List
... 
... 
... class ComputerStatus(Enum):
...     FREE = auto()
...     BUSY = auto()
...     MAINTENANCE = auto()
... 
... 
... @dataclass
... class Computer:
...     id: int
...     name: str
...     specs: str  # например, "i7-13700K, RTX 4070, 32GB"
...     status: ComputerStatus = ComputerStatus.FREE
...     reserved_until: Optional[datetime] = None
...     current_user_id: Optional[int] = None
... 
...     def is_free_at(self, time: datetime) -> bool:
...         if self.status == ComputerStatus.MAINTENANCE:
...             return False
...         if self.status != ComputerStatus.BUSY:
...             return True
...         # Если занят, проверяем, освободится ли к этому времени
...         return self.reserved_until is not None and self.reserved_until <= time
... 
...     def reserve(self, user_id: int, duration_minutes: int) -> None:
...         if not self.is_free_at(datetime.now()):
...             raise ReservationConflictError(f"Компьютер {self.id} ({self.name}) занят.")
...         self.status = ComputerStatus.BUSY
...         self.current_user_id = user_id
...         self.reserved_until = datetime.now() + timedelta(minutes=duration_minutes)

    def release(self) -> None:
        self.status = ComputerStatus.FREE
        self.current_user_id = None
        self.reserved_until = None
