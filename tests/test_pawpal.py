from pawpal_system import Pet, Task


def test_mark_complete_sets_completed():
    task = Task(title="Walk", description="08:00 AM | Exercise", due_date="2026-07-02")
    task.mark_complete()
    assert task.completed is True


def test_add_task_increases_task_count():
    pet = Pet(name="Buddy", species="Dog", breed="Labrador", age=3)
    task = Task(title="Walk", description="08:00 AM | Exercise", due_date="2026-07-02")
    before = len(pet.get_tasks())
    pet.add_task(task)
    assert len(pet.get_tasks()) == before + 1
