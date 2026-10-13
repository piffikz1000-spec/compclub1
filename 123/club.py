Python 3.15.0 (tags/v3.15.0:d220409, Oct  9 2026, 11:55:56) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> class ClubError(Exception):
...     """Общее исключение для ошибок клуба."""
...     pass
... 
... 
... class ComputerNotFoundError(ClubError):
...     """Компьютер не найден."""
...     pass
... 
... 
... class UserNotFoundError(ClubError):
...     """Пользователь не найден."""
...     pass
... 
... 
... class ReservationConflictError(ClubError):
...     """Конфликт бронирования (компьютер уже занят)."""
...     pass
