import datetime
from pawpal_system import Owner, Pet, Task

today = datetime.date.today().isoformat()

# --- Setup ---
owner = Owner(name="Alex Rivera", email="alex@example.com", phone="555-0100")

buddy    = Pet(name="Buddy",    species="Dog", breed="Labrador", age=3)
whiskers = Pet(name="Whiskers", species="Cat", breed="Siamese",  age=5)

buddy.add_task(Task("Morning Walk",    "08:00 AM | Exercise",  today))
buddy.add_task(Task("Lunch Feeding",   "12:00 PM | Nutrition", today))
whiskers.add_task(Task("Vet Checkup",  "03:00 PM | Health",    today))

owner.add_pet(buddy)
owner.add_pet(whiskers)

# --- Display ---
print(f"\n{'=' * 42}")
print(f"  PawPal+  |  Today's Schedule")
print(f"  Owner : {owner.name}")
print(f"  Date  : {today}")
print(f"{'=' * 42}")

for pet in owner.get_pets():
    tasks = pet.get_tasks()
    if not tasks:
        continue
    print(f"\n  {pet.name} ({pet.species}, {pet.breed})")
    print(f"  {'-' * 36}")
    for task in tasks:
        time, task_type = task.description.split(" | ")
        status = "[done]" if task.completed else "  -  "
        print(f"    {status}  [{task_type:<10}]  {task.title:<20}  {time}")

print(f"\n{'=' * 42}\n")
