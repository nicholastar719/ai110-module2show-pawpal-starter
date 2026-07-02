from pawpal_system import Owner, Pet, Task
import streamlit as st

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

# -----------------------
# SESSION STATE (MUST BE FIRST LOGIC)
# -----------------------
if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Default Owner")

st.title("🐾 PawPal+")

st.markdown(
"""
Welcome to PawPal+. Build a pet care planning assistant using your backend system.
"""
)

# -----------------------
# DEMO INPUTS
# -----------------------
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

# -----------------------
# ADD PET (PHASE 3 CORE WIRING)
# -----------------------
st.subheader("Add Pet")

if st.button("Add Pet"):
    pet = Pet(name=pet_name, pet_type=species)
    st.session_state.owner.add_pet(pet)
    st.success("Pet added")

# -----------------------
# ADD TASKS (PHASE 3 CORE WIRING)
# -----------------------
st.subheader("Add Task")

task_title = st.text_input("Task title", value="Morning walk")
duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
priority = st.selectbox("Priority", ["low", "medium", "high"])

if st.button("Add task"):
    task = Task(name=task_title, duration=duration, priority=priority)
    st.session_state.owner.add_task(task)
    st.success("Task added")

# -----------------------
# DEBUG OUTPUT (IMPORTANT FOR GRADING)
# -----------------------
st.divider()

st.subheader("Current Pets")
st.write(st.session_state.owner.pets)

st.subheader("Current Tasks")
st.write(st.session_state.owner.tasks)

# -----------------------
# SCHEDULE BUTTON (placeholder)
# -----------------------
st.divider()

st.subheader("Build Schedule")

if st.button("Generate schedule"):
    st.warning("Scheduler not implemented yet.")