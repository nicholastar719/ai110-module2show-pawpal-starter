    # PawPal+ (Module 2 Project)

    You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

    ## Scenario

    A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

    - Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
    - Consider constraints (time available, priority, owner preferences)
    - Produce a daily plan and explain why it chose that plan

    Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

    ## What you will build

    Your final app should:

    - Let a user enter basic owner + pet info
    - Let a user add/edit tasks (duration + priority at minimum)
    - Generate a daily schedule/plan based on constraints and priorities
    - Display the plan clearly (and ideally explain the reasoning)
    - Include tests for the most important scheduling behaviors

    ## Getting started

    ### Setup

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Windows: .venv\Scripts\activate
    pip install -r requirements.txt
    ```

    ### Suggested workflow

    1. Read the scenario carefully and identify requirements and edge cases.
    2. Draft a UML diagram (classes, attributes, methods, relationships).
    3. Convert UML into Python class stubs (no logic yet).
    4. Implement scheduling logic in small increments.
    5. Add tests to verify key behaviors.
    6. Connect your logic to the Streamlit UI in `app.py`.
    7. Refine UML so it matches what you actually built.

    ## 🖥️ Sample Output

    Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

    ```
    # e.g.:
    # Daily plan for Biscuit (Golden Retriever):
    #   08:00 — Morning walk (30 min) [priority: high]
    #   09:00 — Feeding (10 min) [priority: high]
    #   ...
    ```

    ## 🧪 Testing PawPal+

    ```bash
    # Run the full test suite:
    pytest

    # Run with coverage:
    pytest --cov
    ```

    Sample test output:
    Buddy (Dog, Labrador)
    ------------------------------------
        -    [Exercise  ]  Morning Walk          08:00 AM
        -    [Nutrition ]  Lunch Feeding         12:00 PM

    Whiskers (Cat, Siamese)
    ------------------------------------
        -    [Health    ]  Vet Checkup           03:00 PM

    ==========================================

    # Paste your pytest output here
    ============================================================== test session starts ===============================================================
    platform win32 -- Python 3.13.0, pytest-9.0.3, pluggy-1.6.0
    rootdir: C:\Users\teacl\ai110-module2show-pawpal-starter
    plugins: anyio-4.13.0
    collected 2 items                                                                                                                                 

    tests\test_pawpal.py ..                                                                                                                     [100%]

    =============================================================== 2 passed in 0.11s ================================================================

    ## 📐 Smarter Scheduling

    ## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | Scheduler.get_tasks_sorted() | Sorts by priority, date, or time |
| Filtering | Scheduler.filter_tasks(), get_pending_tasks(), get_tasks_by_priority() | Filters by completion, pet, or priority |
| Conflict handling | Scheduler.detect_conflicts() | Detects tasks scheduled at the same date/time and returns warnings |
| Recurring tasks | Task.next_occurrence(), Scheduler.complete_task(), Scheduler.generate_recurring_tasks() | Supports daily/weekly task regeneration after completion |

    ## 📸 Demo Walkthrough

    Describe your app in numbered steps so a reader can follow along without watching a video:

1. Launch the Streamlit app using "streamlit run app.py".
2. Enter owner and pet information in the input fields.
3. Add tasks with title, duration, and priority.
4. View tasks displayed in real time using session state.
5. Generate or review scheduling output using the scheduler features.
