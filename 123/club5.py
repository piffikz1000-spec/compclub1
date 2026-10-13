Python 3.15.0 (tags/v3.15.0:d220409, Oct  9 2026, 11:55:56) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> class ClubManager:
...     def __init__(self, tariff: Tariff):
...         self.computers: dict[int, Computer] = {}
...         self.users: dict[int, User] = {}
...         self.sessions: List[Session] = []
...         self.tariff = tariff
... 
...     # --- Управление компьютерами ---
...     def add_computer(self, computer: Computer) -> None:
...         self.computers[computer.id] = computer
... 
...     def get_computer(self, computer_id: int) -> Computer:
...         try:
...             return self.computers[computer_id]
...         except KeyError:
...             raise ComputerNotFoundError(f"Компьютер с ID {computer_id} не найден.")
... 
...     def set_maintenance(self, computer_id: int) -> None:
...         comp = self.get_computer(computer_id)
...         if comp.status == ComputerStatus.BUSY:
...             # Можно принудительно освободить или выбросить ошибку — здесь освобождаем
...             comp.release()
...         comp.status = ComputerStatus.MAINTENANCE
... 
...     def return_from_maintenance(self, computer_id: int) -> None:
...         comp = self.get_computer(computer_id)
...         comp.status = ComputerStatus.FREE
... 
...     # --- Управление пользователями ---
...     def add_user(self, user: User) -> None:
...         self.users[user.id] = user
... 
...     def get_user(self, user_id: int) -> User:
...         try:
...             return self.users[user_id]
        except KeyError:
            raise UserNotFoundError(f"Пользователь с ID {user_id} не найден.")

    def top_up_user(self, user_id: int, amount: float) -> None:
        user = self.get_user(user_id)
        user.top_up(amount)

    # --- Бронирование и сессии ---
    def book_computer(
        self,
        computer_id: int,
        user_id: int,
        duration_minutes: int,
    ) -> Session:
        """Создаёт сессию, резервирует компьютер, списывает средства."""
        comp = self.get_computer(computer_id)
        user = self.get_user(user_id)

        if not user.is_active:
            raise ClubError("Пользователь неактивен.")

        cost = self.tariff.calculate_cost(duration_minutes)
        if user.balance_rub < cost:
            raise ClubError(
                f"Недостаточно средств. Требуется {cost:.2f} руб., доступно {user.balance_rub:.2f} руб."
            )

        # Резервируем
        comp.reserve(user_id, duration_minutes)
        user.pay(cost)

        session = Session(
            computer_id=computer_id,
            user_id=user_id,
            start_time=datetime.now(),
            duration_minutes=duration_minutes,
        )
        self.sessions.append(session)
        return session

    def end_session(self, session: Session) -> float:
        """Завершает сессию, освобождает компьютер, пересчитывает стоимость."""
        comp = self.get_computer(session.computer_id)
        # Освобождаем компьютер
        comp.release()
        # Пересчитываем стоимость по фактическому времени
        actual_cost = session.finalize(self.tariff)
        return actual_cost

    # --- Отчёты и статистика ---
    def get_free_computers(self) -> List[Computer]:
        now = datetime.now()
        return [c for c in self.computers.values() if c.is_free_at(now)]

    def get_revenue_today(self) -> float:
        today_start = datetime.combine(datetime.today(), datetime.min.time())
        revenue = 0.0
        for s in self.sessions:
            if s.start_time >= today_start:
                revenue += s.cost_rub
        return revenue
