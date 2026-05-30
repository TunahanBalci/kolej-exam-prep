# CMPE382 Mock Midterm Generation Guide

## Purpose

Generate CMPE382 mock midterm exams that closely match the expected style of the real exam.

The exam should test:

- Conceptual understanding
- Scenario analysis
- Algorithm application
- Calculation ability
- Synchronization reasoning
- Deadlock analysis
- Ability to recall important definitions without being over-guided

The final mock exam must always be visually readable, well-structured, and add up to exactly **100 points**.

---

# 1. Overall Exam Structure

## Required Total Point Value

Every generated mock midterm must add up to exactly:

```text
100 points
```

Do not produce exams with raw totals such as 120, 150, or 160 points unless explicitly asked.

A good default structure is:

| Section | Topic | Suggested Points |
|---|---|---:|
| Question 1 | Classical definitions | 10 |
| Question 2 | CPU scheduling algorithm | 15 |
| Question 3 | Synchronization concepts | 10 |
| Question 4 | Semaphore / bounded buffer / readers-writers | 15 |
| Question 5 | Deadlock characterization / prevention | 10 |
| Question 6 | Resource-allocation graph | 10 |
| Question 7 | Banker’s Algorithm | 20 |
| Question 8 | Short conceptual / code-output / OS topic | 10 |
| **Total** |  | **100** |

The exact topic distribution can change, but the total must always be 100.

---

# 2. Visual Formatting Rules

The exam must be easy to read.

Use:

- Clear main question titles
- Short paragraphs
- Tables for process/resource data
- Code blocks for code
- Bullet points only when they improve readability
- Horizontal separators between major questions
- Simple Markdown formatting

Avoid:

- Dense walls of text
- Too many nested headings
- Long explanations inside the question statement
- Excessive bold formatting
- A separate heading for every sub-question

---

# 3. Sub-Question Formatting Rule

Do **not** create a separate Markdown heading for every sub-question.

Good format:

```md
## Question 3 — Synchronization Concepts

**10 Points**

Answer the following:

**(a) [4 points]** Define a race condition and give a short example.

**(b) [6 points]** A correct critical-section solution must satisfy three requirements. Explain these requirements and what can go wrong if each one is violated.
```

Bad format:

```md
## 3(a) Race Condition

...

## 3(b) Critical-Section Problem

...
```

Sub-questions should usually be written as:

```md
**(a) [x points]** ...
**(b) [x points]** ...
**(c) [x points]** ...
```

This makes the exam visually cleaner and closer to a real printed exam.

---

# 4. Recall-Based Question Rule

Do not over-reveal the answer inside the question.

For definition questions, avoid listing the exact terms that the student is supposed to remember.

## Example: Critical-Section Requirements

Good:

```md
**(b) [6 points]** A correct solution to the critical-section problem must satisfy three requirements. Name and explain these requirements.
```

Bad:

```md
**(b) [6 points]** Explain mutual exclusion, progress, and bounded waiting.
```

The student should recall:

- The names of the requirements
- Their meanings
- Their consequences

This rule applies especially to topics such as:

- Critical-section requirements
- Deadlock conditions
- Scheduling criteria
- Deadlock handling methods
- Semaphore usage mistakes
- Page replacement algorithms
- I/O methods
- Memory allocation methods

---

# 5. Code Question Rule

For questions that include code, prefer asking for the **output** or behavior, not just explanation.

Good:

```md
**(c) [5 points]** What is the output of the following code? Explain briefly why that output occurs.

```c
int x = 5;

void f() {
    static int y = 0;
    y++;
    printf("%d %d\n", x, y);
}

int main() {
    f();
    f();
}
```
```

Bad:

```md
Explain this code.
```

Code questions should usually ask one of the following:

- What is the output?
- Is there a race condition?
- Can this deadlock?
- Which line causes the issue?
- What happens if the order of operations changes?
- Which process enters the critical section first?
- Which page is replaced?
- Which request can be granted?

For operating systems exams, code snippets should be short and focused.

---

# 6. CPU Scheduling Question Style

CPU scheduling calculation questions are important and should be included.

The previous generated **Question 2 — Algorithmic CPU Scheduling** style was good.

A strong CPU scheduling question should include:

- A process table
- Arrival times
- CPU burst times
- A specific scheduling algorithm
- Gantt chart requirement
- Waiting time calculation
- Turnaround time calculation when appropriate
- Average waiting time

Recommended algorithms:

- FCFS
- Nonpreemptive SJF
- Preemptive SJF / SRTF
- Round Robin
- Priority scheduling
- Priority scheduling with Round Robin for same priority

A good CPU scheduling question may ask students to compare two or three algorithms on the same process set.

Example structure:

```md
## Question 2 — CPU Scheduling Algorithms

**15 Points**

Consider the following processes:

| Process | Arrival Time | Burst Time |
|---|---:|---:|
| P1 | 0 | 7 |
| P2 | 2 | 4 |
| P3 | 4 | 1 |
| P4 | 5 | 4 |

**(a) [5 points]** Draw the Gantt chart for FCFS and calculate the average waiting time.

**(b) [5 points]** Draw the Gantt chart for nonpreemptive SJF and calculate the average waiting time.

**(c) [5 points]** Draw the Gantt chart for SRTF and calculate the average waiting time.
```

---

# 7. Deadlock Prevention Question Style

Deadlock prevention matching questions are good and should appear often.

The teacher likes questions where a prevention technique must be matched to the deadlock condition it breaks.

Good format:

```md
**(b) [5 points]** For each prevention strategy, state which deadlock condition is broken.

| Prevention Strategy | Deadlock Condition Broken |
|---|---|
| Require all resources before execution starts | |
| Preempt resources from a waiting process | |
| Number resources and request only in increasing order | |
| Make a resource sharable when possible | |
| Require a process to release held resources before requesting new ones | |
```

This question type is recommended because it tests conceptual understanding without being too open-ended.

---

# 8. Synchronization Question Style

Synchronization questions should test reasoning, not just memorization.

Good topics:

- Race conditions
- Critical-section requirements
- Peterson’s solution
- Hardware support for synchronization
- Test-and-set
- Compare-and-swap
- Mutex locks
- Semaphores
- Semaphore misuse
- Busy waiting
- Monitors
- Condition variables
- Readers-writers
- Bounded buffer
- Dining philosophers
- Sleeping barber

Questions should often be scenario-based.

Good example:

```md
## Question 4 — Semaphore Synchronization

**15 Points**

A bounded buffer has size `n = 5`. Producers insert items and consumers remove items.

**(a) [4 points]** Write the required semaphores, their initial values, and their purpose.

**(b) [5 points]** Write the producer pseudocode using semaphores.

**(c) [6 points]** Suppose a consumer calls `wait(mutex)` before `wait(full)`. Can the system deadlock? Explain using a concrete execution order.
```

---

# 9. Resource-Allocation Graph Question Style

Resource-allocation graph questions should include:

- Processes or threads
- Resource types
- Number of instances for each resource type
- Current assignments
- Current requests

The question should ask:

1. Draw the graph
2. Identify cycles
3. Decide whether deadlock exists
4. Explain why a cycle may or may not imply deadlock

Important distinction:

- If every resource type has one instance, a cycle means deadlock.
- If some resource types have multiple instances, a cycle means deadlock is possible but not guaranteed.

Good format:

```md
## Question 6 — Resource-Allocation Graph

**10 Points**

A system has processes `T1`, `T2`, `T3` and resource types `R1`, `R2`.

| Resource Type | Instances |
|---|---:|
| R1 | 1 |
| R2 | 2 |

Current state:

- `T1` holds `R1` and requests `R2`.
- `T2` holds one instance of `R2` and requests `R1`.
- `T3` holds one instance of `R2` and requests nothing.

**(a) [4 points]** Draw the resource-allocation graph.

**(b) [3 points]** Identify any cycles.

**(c) [3 points]** Is the system deadlocked? Justify your answer.
```

---

# 10. Banker’s Algorithm Question Style

Banker’s Algorithm questions should be calculation-heavy.

They should include:

- Allocation matrix
- Max matrix
- Available vector
- Request vector, if testing resource-request algorithm

The question should ask:

1. Calculate Need matrix
2. Run the safety algorithm
3. Give a safe sequence if one exists
4. Test whether a request can be granted

Good format:

```md
## Question 7 — Banker’s Algorithm

**20 Points**

A system has 5 processes and 3 resource types.

[Allocation Matrix]

[Max Matrix]

[Available Vector]

**(a) [5 points]** Calculate the Need matrix.

**(b) [8 points]** Apply the safety algorithm and determine whether the system is safe. If safe, give one safe sequence.

**(c) [7 points]** Suppose `P1` requests `(1, 0, 2)`. Determine whether the request can be granted immediately.
```

The solution must show intermediate steps, not just the final answer.

---

# 11. Past Exam Style to Preserve

The exam should imitate the observed past-exam style.

Past-style question types include:

| Topic Area | Style | Typical Task |
|---|---|---|
| CPU scheduling | Algorithmic | Draw Gantt chart, calculate waiting/turnaround time |
| Synchronization | Conceptual + scenario | Analyze race conditions, semaphores, monitors |
| Deadlocks | Definition + scenario | Conditions, prevention, resource-allocation graph |
| Banker’s Algorithm | Calculation | Need matrix, safe sequence, request decision |
| Memory management | Calculation | Page replacement, address bits, page table entries |
| File systems | Short answer + calculation | i-nodes, allocation methods, corrupted blocks |
| I/O | Calculation + definition | Programmed I/O, interrupt-driven I/O, DMA |

---

# 12. Recommended 100-Point Mock Midterm Template

Use this as the default template unless the user asks for a different topic emphasis.

| Question | Topic | Points |
|---|---|---:|
| Q1 | Classical definitions: CPU scheduling or synchronization | 10 |
| Q2 | CPU scheduling algorithms | 15 |
| Q3 | Critical-section / race condition / synchronization concepts | 10 |
| Q4 | Semaphores and bounded buffer or readers-writers | 15 |
| Q5 | Deadlock conditions and prevention matching | 10 |
| Q6 | Resource-allocation graph | 10 |
| Q7 | Banker’s Algorithm | 20 |
| Q8 | Code-output / short OS reasoning / monitor or dining philosophers | 10 |
| **Total** |  | **100** |

---

# 13. Quality Checklist Before Finalizing a Mock Exam

Before giving the final mock exam, verify:

- [ ] Total points add up to exactly 100.
- [ ] The exam is visually readable.
- [ ] Sub-questions do not each have separate headings.
- [ ] The question does not reveal recall-based answers too directly.
- [ ] Code questions ask for output, behavior, or result.
- [ ] CPU scheduling includes a process table and calculation tasks.
- [ ] Deadlock prevention matching appears if deadlocks are included.
- [ ] Banker’s Algorithm includes Need, safety check, and possibly a request.
- [ ] Tables are used where they improve clarity.
- [ ] The exam resembles the teacher’s expected style.
- [ ] The wording is clear and unambiguous.
- [ ] No unnecessary answer hints are included.

---

# 14. Common Mistakes to Avoid

Avoid generating mock exams that:

- Add up to more or less than 100 points
- Use too many headings
- Include the answer terms inside recall questions
- Ask “explain this code” without requiring output or behavior
- Include huge code blocks
- Overload one question with too many unrelated topics
- Give too many hints inside the question
- Use poor visual spacing
- Mix answer key content into the exam unless explicitly requested
- End with an unscaled raw point total

---

# 15. Final Instruction for Future Mock Midterms

When generating future CMPE382 mock midterms, follow this priority order:

1. Match the teacher’s style.
2. Keep the exam visually clean.
3. Make the student recall important concepts.
4. Include calculation-based questions.
5. Include scenario-based reasoning.
6. Ensure the point total is exactly 100.
7. Avoid over-guiding the student.
