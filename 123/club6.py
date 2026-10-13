Python 3.15.0 (tags/v3.15.0:d220409, Oct  9 2026, 11:55:56) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def demo():
...     # Тариф: 5 руб/мин, скидки: от 60 мин — 5%, от 180 мин — 10%
...     tariff = Tariff(
...         price_per_minute=5.0,
...         discount_rules={60: 5, 180: 10},
...     )
... 
...     manager = ClubManager(tariff)
... 
...     # Добавляем компьютеры
...     manager.add_computer(Computer(id=1, name="Gaming-01", specs="i7-13700K, RTX 4070, 32GB"))
...     manager.add_computer(Computer(id=2, name="Gaming-02", specs="i5-12400F, RTX 3060, 16GB"))
...     manager.add_computer(Computer(id=3, name="Work-01", specs="Ryzen 5 5600, GTX 1660, 16GB"))
... 
...     # Добавляем пользователей
...     manager.add_user(User(id=101, username="alice", email="alice@example.com", balance_rub=500.0))
...     manager.add_user(User(id=102, username="bob", email="bob@example.com", balance_rub=200.0))
... 
...     # Пополняем баланс
...     manager.top_up_user(102, 300.0)
... 
...     # Бронируем компьютер
...     session = manager.book_computer(computer_id=1, user_id=101, duration_minutes=90)
...     print(f"Сессия создана: компьютер {session.computer_id}, старт {session.start_time}")
... 
...     # Имитируем окончание сессии (в реальном коде это будет позже)
...     session.end_time = datetime.now() + timedelta(minutes=85)  # чуть меньше забронированного
...     final_cost = manager.end_session(session)
...     print(f"Сессия завершена. Итоговая стоимость: {final_cost:.2f} руб.")

    # Свободные компьютеры
    free = manager.get_free_computers()
    print("Свободные компьютеры:", [c.name for c in free])

    # Выручка за сегодня
    revenue = manager.get_revenue_today()
    print(f"Выручка за сегодня: {revenue:.2f} руб.")


if __name__ == "__main__":
    demo()
