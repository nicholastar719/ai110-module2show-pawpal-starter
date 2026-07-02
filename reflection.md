# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design?
- What classes did you include, and what responsibilities did you assign to each?

I designed four classes: Owner, Pet, Task, and Scheduler. The Owner manages pets, while each Pet stores basic information and maintains a list of tasks. The Task class represents individual care activities such as feeding, walking, and medication, including relevant scheduling details. The Scheduler class is responsible for organizing and filtering tasks, including handling scheduling and detecting conflicts.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

I added a recurring attribute to the Task class because many pet care activities happen regularly. I also kept the scheduling logic in a separate Scheduler class to improve organization and separate task management from scheduling logic.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

The scheduler considers task priority, due date, and completion status. Priority is used to determine how important a task is (either high, medium, or low), while due date is used to organize tasks chronologically. Completion status is used to filter out finished tasks from active scheduling.
**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

One major tradeoff in the scheduler is simplicity versus realism. Conflict detection is implemented using exact time matching rather than detecting overlapping time intervals. This simplifies implementation but does not fully model real-world scheduling conflicts.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

AI tools were used for brainstorming scheduling algorithms, debugging dataclass structure issues, and improving filtering and sorting logic. The most useful prompts were those that asked for direct code implementation of features like conflict detection and recurring task handling.
**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

One instance where AI output was modified was in conflict detection logic. The initial suggestion was overly complex and used time range comparisons. It was simplified to exact time matching to align with the project scope and Streamlit structure. Verification was done by manually testing multiple tasks with identical timestamps.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested task creation, sorting by priority and time, filtering by completion status, conflict detection for overlapping time slots, and recurring task generation. These tests were important because I made sure that scheduling logic behaved consistently under different input conditions.
**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I am moderately confident the scheduler works correctly for the intended scope. If I had more time, I would test overlapping time ranges, invalid date formats, and edge cases involving multiple recurring tasks generating large chains.
---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
