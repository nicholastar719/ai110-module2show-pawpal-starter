import datetime
from dataclasses import dataclass, field
from typing import Optional

_PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}

# -----------------------
# TASK
# -----------------------

@dataclass
class Task:
    title: str
    description: str  # format: "HH:MM AM/PM | TaskType"
    due_date: str     # ISO format "YYYY-MM-DD"
    priority: str = "medium"
    completed: bool = False
    recurring: bool = False
    recur_interval_days: int = 0

    def mark_complete(self) -> None:
        self.completed = True

    def next_occurrence(self) -> Optional["Task"]:
        """Return next recurring instance or None."""
        if not self.recurring or self.recur_interval_days <= 0:
            return None

        next_date = (
            datetime.date.fromisoformat(self.due_date)
            + datetime.timedelta(days=self.recur_interval_days)
        )

        return Task(
            title=self.title,
            description=self.description,
            due_date=next_date.isoformat(),
            priority=self.priority,
            recurring=self.recurring,
            recur_interval_days=self.recur_interval_days,
        )

    def is_overdue(self) -> bool:
        today = datetime.date.today().isoformat()
        return (not self.completed) and (self.due_date < today)

    def get_details(self) -> str:
        return f"{self.title} | {self.due_date} | {self.priority}"


# -----------------------
# PET
# -----------------------

@dataclass
class Pet:
    name: str
    species: str
    breed: str = ""
    age: int = 0

    _tasks: list[Task] = field(default_factory=list, init=False)

    def add_task(self, task: Task) -> None:
        self._tasks.append(task)

    def remove_task(self, task: Task) -> None:
        if task in self._tasks:
            self._tasks.remove(task)

    def get_tasks(self) -> list[Task]:
        return list(self._tasks)

    def get_info(self) -> str:
        return f"{self.name} ({self.species})"


# -----------------------
# OWNER
# -----------------------

@dataclass
class Owner:
    name: str
    email: str = ""
    phone: str = ""

    _pets: list[Pet] = field(default_factory=list, init=False)

    def add_pet(self, pet: Pet) -> None:
        self._pets.append(pet)

    def remove_pet(self, pet: Pet) -> None:
        if pet in self._pets:
            self._pets.remove(pet)

    def get_pets(self) -> list[Pet]:
        return list(self._pets)

    def view_schedule(self) -> None:
        for pet in self._pets:
            for task in pet.get_tasks():
                print(f"{pet.name}: {task.title} ({task.due_date})")


# -----------------------
# SCHEDULER
# -----------------------

@dataclass
class Scheduler:
    _pets: list[Pet] = field(default_factory=list, init=False)
    _tasks: list[Task] = field(default_factory=list, init=False)

    def schedule_task(self, pet: Pet, task: Task) -> None:
        self._pets.append(pet)
        self._tasks.append(task)
        pet.add_task(task)

    def get_upcoming_tasks(self) -> list[Task]:
        return self._tasks

    def get_tasks_by_pet(self, pet: Pet) -> list[Task]:
        return pet.get_tasks()

    def send_reminders(self) -> None:
        for task in self._tasks:
            if not task.completed:
                print(f"Reminder: {task.title}")

    # -----------------------
    # SORTING
    # -----------------------

    def get_tasks_sorted(self, by: str = "priority") -> list[Task]:
        if by == "date":
            return sorted(self._tasks, key=lambda t: t.due_date)

        if by == "time":
            return sorted(
                self._tasks,
                key=lambda t: datetime.datetime.strptime(
                    t.description.split(" | ")[0].strip(),
                    "%I:%M %p"
                ).time()
            )

        return sorted(
            self._tasks,
            key=lambda t: _PRIORITY_ORDER.get(t.priority, 1)
        )

    # -----------------------
    # FILTERING
    # -----------------------

    def get_pending_tasks(self) -> list[Task]:
        return self.filter_tasks(completed=False)

    def get_tasks_by_priority(self, priority: str) -> list[Task]:
        return [t for t in self._tasks if t.priority == priority]

    def filter_tasks(self, completed: bool = False, pet: Pet | None = None) -> list[Task]:
        source = pet.get_tasks() if pet else self._tasks
        return [t for t in source if t.completed == completed]

    # -----------------------
    # CONFLICT DETECTION
    # -----------------------

    def detect_conflicts(self) -> list[str]:
        slots: dict[tuple[str, str], list[tuple[Pet, Task]]] = {}

        for pet in self._pets:
            for task in pet.get_tasks():
                time_str = task.description.split(" | ")[0].strip()
                key = (task.due_date, time_str)

                slots.setdefault(key, []).append((pet, task))

        warnings = []

        for (date, time_str), entries in slots.items():
            if len(entries) < 2:
                continue

            labels = [f"{pet.name} '{task.title}'" for pet, task in entries]
            warnings.append(
                f"Conflict on {date} at {time_str}: {', '.join(labels)}"
            )

        return warnings

    # -----------------------
    # RECURRING TASKS
    # -----------------------

    def complete_task(self, pet: Pet, task: Task) -> Optional[Task]:
        task.mark_complete()

        next_task = task.next_occurrence()
        if next_task:
            self.schedule_task(pet, next_task)

        return next_task

    def generate_recurring_tasks(self, pet: Pet, task: Task, occurrences: int = 3) -> None:
        current = task

        for _ in range(occurrences):
            current = current.next_occurrence()
            if current is None:
                break
            self.schedule_task(pet, current)