import pytest
from pawpal_system import Owner, Pet, Task, Scheduler


# -----------------------
# FIXTURE SETUP
# -----------------------

def setup_scheduler():
    scheduler = Scheduler()
    pet = Pet(name="Mochi", species="cat")

    task1 = Task(
        title="Morning Walk",
        description="08:00 AM | Exercise",
        due_date="2026-07-02",
        priority="high"
    )

    task2 = Task(
        title="Feed Cat",
        description="09:00 AM | Food",
        due_date="2026-07-02",
        priority="medium"
    )

    scheduler.schedule_task(pet, task1)
    scheduler.schedule_task(pet, task2)

    return scheduler, pet, task1, task2


# -----------------------
# 1. SORTING TEST
# -----------------------

def test_sorting_by_priority():
    scheduler, _, _, _ = setup_scheduler()

    sorted_tasks = scheduler.get_tasks_sorted(by="priority")

    priorities = [t.priority for t in sorted_tasks]
    assert priorities[0] == "high"


# -----------------------
# 2. FILTERING TEST
# -----------------------

def test_filtering_completed_tasks():
    scheduler, _, task1, _ = setup_scheduler()

    task1.mark_complete()

    pending = scheduler.get_pending_tasks()

    assert task1 not in pending


# -----------------------
# 3. CONFLICT DETECTION TEST
# -----------------------

def test_conflict_detection():
    scheduler = Scheduler()
    pet = Pet(name="Buddy", species="dog")

    t1 = Task("Walk", "10:00 AM | Exercise", "2026-07-02")
    t2 = Task("Feed", "10:00 AM | Food", "2026-07-02")

    scheduler.schedule_task(pet, t1)
    scheduler.schedule_task(pet, t2)

    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) > 0


# -----------------------
# 4. RECURRING TASK TEST
# -----------------------

def test_recurring_task_generation():
    scheduler = Scheduler()
    pet = Pet(name="Luna", species="cat")

    task = Task(
        title="Daily Feed",
        description="08:00 AM | Food",
        due_date="2026-07-02",
        recurring=True,
        recur_interval_days=1
    )

    scheduler.schedule_task(pet, task)

    scheduler.complete_task(pet, task)

    assert len(pet.get_tasks()) >= 1  # new recurring task created