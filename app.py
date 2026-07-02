from pawpal_system import Owner, Pet, Task, Scheduler
import streamlit as st

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

# -----------------------
# SESSION STATE INIT
# -----------------------

if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Default Owner")

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler()

if "tasks" not in st.session_state:
    st.session_state.tasks = []

# -----------------------
# TITLE
# -----------------------

st.title("🐾 PawPal+")

st.markdown("Pet care scheduling assistant with smart task management.")

st.divider()

# -----------------------
# OWNER + PET INPUT
# -----------------------

st.subheader("Owner & Pet Setup")

owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

if st.button("Create Owner"):
    st.session_state.owner = Owner(name=owner_name)
    st.success("Owner created")

if st.button("Add Pet"):
    pet = Pet(name=pet_name, species=species)
    st.session_state.owner.add_pet(pet)
    st.success("Pet added")

st.divider()

# -----------------------
# ADD TASKS
# -----------------------

st.subheader("Add Task")

task_title = st.text_input("Task title", value="Morning walk")
task_desc = st.text_input("Description (HH:MM AM/PM | Type)", value="08:00 AM | Walk")
due_date = st.date_input("Due date")
priority = st.selectbox("Priority", ["low", "medium", "high"])
recurring = st.checkbox("Recurring task")
interval = st.number_input("Recur interval (days)", min_value=0, max_value=30, value=0)

if st.button("Add Task"):
    task = Task(
        title=task_title,
        description=task_desc,
        due_date=str(due_date),
        priority=priority,
        recurring=recurring,
        recur_interval_days=int(interval)
    )

    # attach task to first pet (simple demo assumption)
    pets = st.session_state.owner.get_pets()

    if pets:
        pets[0].add_task(task)
        st.session_state.scheduler.schedule_task(pets[0], task)
        st.success("Task added")
    else:
        st.warning("Add a pet first")

st.divider()

# -----------------------
# VIEW TASKS
# -----------------------

st.subheader("Current Tasks")

pets = st.session_state.owner.get_pets()

all_tasks = []
for pet in pets:
    for task in pet.get_tasks():
        all_tasks.append({
            "Pet": pet.name,
            "Title": task.title,
            "Priority": task.priority,
            "Due Date": task.due_date,
            "Completed": task.completed
        })

if all_tasks:
    st.table(all_tasks)
else:
    st.info("No tasks yet")

st.divider()

# -----------------------
# SMART FEATURES (PHASE 6)
# -----------------------

st.subheader("Smart Scheduling Tools")

col1, col2, col3 = st.columns(3)

# SORTING
with col1:
    if st.button("Sort by Priority"):
        sorted_tasks = st.session_state.scheduler.get_tasks_sorted(by="priority")
        st.table([t.get_details() for t in sorted_tasks])

# FILTERING
with col2:
    if st.button("Show Pending Tasks"):
        pending = st.session_state.scheduler.get_pending_tasks()
        st.table([t.get_details() for t in pending])

# CONFLICTS
with col3:
    if st.button("Check Conflicts"):
        conflicts = st.session_state.scheduler.detect_conflicts()

        if conflicts:
            for c in conflicts:
                st.warning(c)
        else:
            st.success("No conflicts detected")

st.divider()

# -----------------------
# SCHEDULE BUTTON
# -----------------------

st.subheader("Generate Schedule")

if st.button("Generate Schedule"):
    st.info("Schedule generated using priority + due date ordering.")

    sorted_tasks = st.session_state.scheduler.get_tasks_sorted(by="date")

    for t in sorted_tasks:
        st.write(f"• {t.title} ({t.due_date}) - {t.priority}")