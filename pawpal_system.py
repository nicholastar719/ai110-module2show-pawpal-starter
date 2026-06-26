from datetime import date


class Task:
    def __init__(self, title: str, description: str, due_date: date, completed: bool = False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def mark_complete(self) -> None:
        pass

    def is_overdue(self) -> bool:
        pass

    def get_details(self) -> str:
        pass


class Pet:
    def __init__(self, name: str, species: str, breed: str, age: int):
        self.name = name
        self.species = species
        self.breed = breed
        self.age = age
        self._tasks: list[Task] = []

    def add_task(self, task: Task) -> None:
        pass

    def remove_task(self, task: Task) -> None:
        pass

    def get_tasks(self) -> list[Task]:
        pass

    def get_info(self) -> str:
        pass


class Owner:
    def __init__(self, name: str, email: str, phone: str):
        self.name = name
        self.email = email
        self.phone = phone
        self._pets: list[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        pass

    def remove_pet(self, pet: Pet) -> None:
        pass

    def get_pets(self) -> list[Pet]:
        pass

    def view_schedule(self) -> None:
        pass


class Scheduler:
    def __init__(self):
        self._pets: list[Pet] = []
        self._tasks: list[Task] = []

    def schedule_task(self, pet: Pet, task: Task) -> None:
        pass

    def get_upcoming_tasks(self) -> list[Task]:
        pass

    def get_tasks_by_pet(self, pet: Pet) -> list[Task]:
        pass

    def send_reminders(self) -> None:
        pass
