# CMPE382 Mock Final Exam Generation Guide

## Purpose

Generate CMPE382 mock final exams that closely match the expected style of the real exam while reflecting the final-exam scope and weighting.

The exam should test:

- Conceptual understanding
- Scenario analysis
- Algorithm application
- Calculation ability
- Synchronization reasoning
- Deadlock analysis
- Memory-management reasoning
- Virtual-memory calculations
- Storage, I/O, and file-system understanding
- Ability to recall important definitions without being over-guided

The final mock exam must always be visually readable, well-structured, and add up to exactly **100 points**.

---

# 1. Final Exam Scope and Weighting

## Required Coverage

The final exam covers:

```text
Chapters 1-15
```

The question distribution must follow this weighting:

| Scope | Chapters | Weight | Points in a 100-point mock final |
|---|---|---:|---:|
| Post-Midterm 2 topics | Chapters 10-15 | 60% | 60 points |
| Cumulative review | Chapters 1-9 | 40% | 40 points |
| **Total** | **Chapters 1-15** | **100%** | **100 points** |

When generating a 100-point mock final, the exam must contain exactly:

```text
60 points from Chapters 10-15
40 points from Chapters 1-9
```

Do not accidentally make the mock final look like a Midterm 2 exam. CPU scheduling, synchronization, deadlocks, and Banker’s Algorithm can still appear, but they should not dominate the exam. The final must give clear priority to virtual memory, storage, I/O, and file systems.

---

# 2. Required Total Point Value

Every generated mock final must add up to exactly:

```text
100 points
```

Do not produce exams with raw totals such as 120, 150, or 160 points unless explicitly asked.

If the user asks for a shorter or longer mock final, still preserve the same ratio:

| Total Points | Chapters 10-15 | Chapters 1-9 |
|---:|---:|---:|
| 50 | 30 | 20 |
| 80 | 48 | 32 |
| 100 | 60 | 40 |
| 120 | 72 | 48 |

---

# 3. Recommended 100-Point Final Exam Template

Use this as the default template unless the user asks for a different emphasis.

| Question | Topic Area | Chapters | Points |
|---|---|---:|---:|
| Q1 | Foundations, processes, threads, OS services, system calls | 1-4 | 10 |
| Q2 | CPU scheduling or main-memory review | 5 or 9 | 10 |
| Q3 | Synchronization, semaphores, monitors, or classical synchronization problems | 6-7 | 10 |
| Q4 | Deadlocks, resource-allocation graph, or Banker’s Algorithm | 8 | 10 |
| Q5 | Virtual memory: demand paging, page faults, EAT, or page replacement | 10 | 20 |
| Q6 | Frame allocation, thrashing, working set, COW, or memory-mapped files | 10 | 10 |
| Q7 | Mass-storage systems: HDD/NVM scheduling, I/O time, swap space, or RAID | 11 | 10 |
| Q8 | I/O systems: polling, interrupts, DMA, kernel I/O, buffering/caching/spooling | 12 | 10 |
| Q9 | File systems: interface, allocation, free space, recovery, VFS, NFS | 13-15 | 10 |
| **Total** |  |  | **100** |

This template gives exactly:

```text
Chapters 1-9:   40 points
Chapters 10-15: 60 points
Total:          100 points
```

---

# 4. Alternative Balanced Final Exam Template

Use this template when the exam should have fewer but larger questions.

| Question | Topic Area | Chapters | Points |
|---|---|---:|---:|
| Q1 | Short cumulative definitions and OS concepts | 1-4 | 10 |
| Q2 | CPU scheduling and/or main memory calculation | 5, 9 | 10 |
| Q3 | Synchronization and deadlock analysis | 6-8 | 20 |
| Q4 | Virtual memory calculation: page faults, EAT, page replacement | 10 | 20 |
| Q5 | Thrashing, frame allocation, working set, COW, or memory-mapped files | 10 | 10 |
| Q6 | Mass-storage and I/O systems | 11-12 | 15 |
| Q7 | File-system interface, implementation, and internals | 13-15 | 15 |
| **Total** |  |  | **100** |

This version is useful when the mock exam should feel more like a compact final with major multi-part questions.

---

# 5. Chapter Coverage Map

## Chapters 1-9: Cumulative Review, 40%

Use these topics for cumulative questions. They should review earlier material without overwhelming the post-Midterm 2 topics.

| Chapter | Main Topics to Test |
|---:|---|
| 1 | OS definition, kernel, system programs, interrupts, traps, DMA, dual-mode operation, timers, resource management |
| 2 | OS services, user interfaces, system calls, linkers/loaders, system programs, OS design and structure, booting, debugging |
| 3 | Processes, process states, PCB, process scheduling, context switch, fork/exec/wait, IPC, shared memory, message passing, pipes, sockets |
| 4 | Threads, multithreading benefits/challenges, multicore programming, user/kernel threads, multithreading models, thread libraries |
| 5 | CPU scheduling criteria, FCFS, SJF, SRTF, Round Robin, priority scheduling, Gantt charts, waiting time, turnaround time |
| 6 | Race conditions, critical-section problem, Peterson’s solution, hardware synchronization, mutex locks, semaphores, monitors, liveness |
| 7 | Bounded buffer, readers-writers, dining philosophers, synchronization examples in POSIX/Java/Linux/Windows |
| 8 | Deadlock conditions, prevention, avoidance, detection, recovery, resource-allocation graphs, Banker’s Algorithm |
| 9 | Logical/physical addresses, MMU, contiguous allocation, paging, page tables, TLB, segmentation, swapping, address translation |

## Chapters 10-15: Post-Midterm 2 Topics, 60%

These topics must form the majority of the mock final.

| Chapter | Main Topics to Test |
|---:|---|
| 10 | Virtual memory, demand paging, valid-invalid bit, page faults, effective access time, copy-on-write, page replacement, FIFO, OPT, LRU, second chance, frame allocation, global/local replacement, thrashing, working set, page-fault frequency, memory-mapped files, kernel memory |
| 11 | HDD and NVM structure, access latency, average I/O time, disk scheduling, FCFS, SSTF, SCAN, C-SCAN, NVM scheduling, error detection/correction, storage management, swap-space management, RAID |
| 12 | I/O hardware, ports, buses, controllers, polling, interrupts, DMA, application I/O interface, blocking/nonblocking/asynchronous I/O, kernel I/O subsystem, buffering, caching, spooling, error handling, protection, performance |
| 13 | File concept, file attributes, file operations, open-file tables, access methods, sequential/direct access, directory structures, protection, memory-mapped files |
| 14 | File-system structure, file-system operations, FCB/inodes, directory implementation, allocation methods, contiguous allocation, linked allocation, FAT, indexed allocation, free-space management, performance, consistency checking, journaling, recovery, WAFL |
| 15 | Partitions and mounting, file sharing, VFS, vnodes/inodes, VFS implementation objects, remote file systems, client-server file systems, NFS, NFS mounting, NFS architecture, consistency semantics |

---

# 6. Visual Formatting Rules

The exam must be easy to read.

Use:

- Clear main question titles
- Short paragraphs
- Tables for process, page, disk, resource, or file-system data
- Code blocks for code or pseudocode
- Bullet points only when they improve readability
- Horizontal separators between major questions
- Simple Markdown formatting

Avoid:

- Dense walls of text
- Too many nested headings
- Long explanations inside the question statement
- Excessive bold formatting
- A separate heading for every sub-question
- Answer-key content inside the exam unless explicitly requested

---

# 7. Sub-Question Formatting Rule

Do **not** create a separate Markdown heading for every sub-question.

Good format:

```md
## Question 5 - Virtual Memory

**20 Points**

Consider the following page reference string and a system with 3 frames.

**(a) [6 points]** Using FIFO, show the frame contents after each reference and count the page faults.

**(b) [6 points]** Using LRU, show the frame contents after each reference and count the page faults.

**(c) [4 points]** Explain why the two algorithms may produce different fault counts.

**(d) [4 points]** Calculate the effective access time for the given page-fault rate.
```

Bad format:

```md
## 5(a) FIFO
...
## 5(b) LRU
...
```

Sub-questions should usually be written as:

```md
**(a) [x points]** ...
**(b) [x points]** ...
**(c) [x points]** ...
```

---

# 8. Recall-Based Question Rule

Do not over-reveal the answer inside the question.

For definition questions, avoid listing the exact terms that the student is supposed to remember.

Good:

```md
**(a) [5 points]** A correct solution to the critical-section problem must satisfy three requirements. Name and explain these requirements.
```

Bad:

```md
**(a) [5 points]** Explain mutual exclusion, progress, and bounded waiting.
```

Good:

```md
**(b) [6 points]** Four conditions must hold simultaneously for deadlock to occur. Name and explain these conditions.
```

Bad:

```md
**(b) [6 points]** Explain mutual exclusion, hold and wait, no preemption, and circular wait.
```

This rule applies especially to:

- Critical-section requirements
- Deadlock conditions
- Scheduling criteria
- Deadlock handling methods
- Page-replacement algorithms
- I/O methods
- Memory allocation methods
- File allocation methods
- Free-space management methods
- File protection/access concepts

---

# 9. Code and Pseudocode Question Rule

For questions that include code or pseudocode, prefer asking for the output, behavior, or error, not just explanation.

Good tasks:

- What is the output?
- Is there a race condition?
- Can this deadlock?
- Which line causes the issue?
- What happens if the order of operations changes?
- Which process enters the critical section first?
- Which page is replaced?
- Which I/O method is being used?
- Which request can be granted?

Avoid vague prompts such as:

```md
Explain this code.
```

Code snippets should be short and focused.

---

# 10. Cumulative Question Style: Chapters 1-9

The cumulative portion should be worth exactly **40 points** in a 100-point final.

Good cumulative questions include:

| Topic | Preferred Style | Typical Task |
|---|---|---|
| OS basics | Short answer | Define OS/kernel/system call/trap/interrupt; compare user mode and kernel mode |
| Processes | Conceptual + scenario | Identify process state transitions, context switch behavior, IPC method |
| Threads | Conceptual | Compare process vs thread; user vs kernel threads; multithreading benefits/problems |
| CPU scheduling | Calculation | Draw Gantt chart, calculate waiting time and turnaround time |
| Synchronization | Scenario/code | Analyze race conditions, semaphore ordering, monitors, bounded buffer, readers-writers |
| Deadlocks | Scenario/calculation | Deadlock conditions, prevention matching, RAG, Banker’s Algorithm |
| Main memory | Calculation | Address translation, page number/offset bits, page table entries, TLB effective access time |

Cumulative questions should usually be shorter than the post-Midterm 2 questions.

---

# 11. CPU Scheduling Question Style

CPU scheduling can appear in the cumulative 40%, but should not dominate the final.

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

Example:

```md
## Question 2 - CPU Scheduling Review

**10 Points**

Consider the following processes:

| Process | Arrival Time | Burst Time |
|---|---:|---:|
| P1 | 0 | 7 |
| P2 | 2 | 4 |
| P3 | 4 | 1 |
| P4 | 5 | 4 |

**(a) [5 points]** Draw the Gantt chart for SRTF.

**(b) [3 points]** Calculate the waiting time of each process.

**(c) [2 points]** Calculate the average waiting time.
```

For the final exam, prefer one CPU scheduling algorithm or one comparison between two algorithms. Avoid spending 20+ points on CPU scheduling unless explicitly asked.

---

# 12. Synchronization Question Style

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

Good example:

```md
## Question 3 - Semaphore Synchronization Review

**10 Points**

A bounded buffer has size `n = 5`. Producers insert items and consumers remove items.

**(a) [3 points]** Write the required semaphores, their initial values, and their purpose.

**(b) [4 points]** Write the producer pseudocode using semaphores.

**(c) [3 points]** Suppose a consumer calls `wait(mutex)` before `wait(full)`. Can the system deadlock? Explain using a concrete execution order.
```

---

# 13. Deadlock Question Style

Deadlock questions should combine recall and scenario reasoning.

Good deadlock tasks:

- Name and explain the necessary conditions for deadlock
- Match deadlock prevention strategies to the condition they break
- Draw or analyze a resource-allocation graph
- Determine whether a cycle implies deadlock
- Apply Banker’s Algorithm
- Decide whether a request can be granted safely

Deadlock prevention matching is especially useful.

Example:

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

Resource-allocation graph questions should include:

- Processes or threads
- Resource types
- Number of instances for each resource type
- Current assignments
- Current requests

Important distinction:

- If every resource type has one instance, a cycle means deadlock.
- If some resource types have multiple instances, a cycle means deadlock is possible but not guaranteed.

---

# 14. Banker’s Algorithm Question Style

Banker’s Algorithm can appear in the cumulative 40%, but avoid making it the largest question unless the user asks for a deadlock-heavy final.

A Banker’s Algorithm question should include:

- Allocation matrix
- Max matrix
- Available vector
- Request vector, if testing the resource-request algorithm

The question should ask students to:

1. Calculate the Need matrix
2. Run the safety algorithm
3. Give a safe sequence if one exists
4. Test whether a request can be granted

Example:

```md
## Question 4 - Banker’s Algorithm Review

**10 Points**

A system has 5 processes and 3 resource types.

[Allocation Matrix]

[Max Matrix]

[Available Vector]

**(a) [3 points]** Calculate the Need matrix.

**(b) [4 points]** Apply the safety algorithm and determine whether the system is safe. If safe, give one safe sequence.

**(c) [3 points]** Suppose `P1` requests `(1, 0, 2)`. Determine whether the request can be granted immediately.
```

The solution must show intermediate steps, not just the final answer.

---

# 15. Virtual Memory Question Style

Virtual memory is the most important post-Midterm 2 topic and should usually receive the largest single point allocation.

Good virtual-memory topics:

- Logical vs physical memory
- Demand paging
- Valid-invalid bit
- Page faults
- Page-fault service steps
- Effective access time
- Copy-on-write
- Page replacement
- FIFO
- Optimal replacement
- LRU
- Second-chance / clock-style algorithms
- Belady’s anomaly
- Frame allocation
- Global vs local replacement
- Thrashing
- Locality
- Working-set model
- Page-fault frequency
- Memory-mapped files
- Kernel memory allocation

A strong virtual-memory question should include at least one calculation.

Recommended calculation types:

- Page fault count for FIFO/LRU/OPT
- Frame table after each reference
- Effective access time from memory access time, page-fault rate, and page-fault service time
- Working-set size from a reference string and window size
- Page number and offset calculation
- Page table lookup / valid-invalid bit reasoning

Example:

```md
## Question 5 - Virtual Memory and Page Replacement

**20 Points**

A system has 3 page frames and uses demand paging. Consider the page reference string:

```text
7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2
```

**(a) [6 points]** Using FIFO, show the frame contents after each reference and count the number of page faults.

**(b) [6 points]** Using LRU, show the frame contents after each reference and count the number of page faults.

**(c) [4 points]** Using OPT, count the number of page faults.

**(d) [4 points]** Explain whether Belady’s anomaly can occur for the algorithms used above.
```

---

# 16. Effective Access Time Question Style

Effective access time questions are strong final-exam questions because they combine concept and calculation.

Good format:

```md
## Question 6 - Demand Paging and Effective Access Time

**10 Points**

A memory access takes 100 ns. A page fault takes 8 ms to service. The page-fault rate is `p = 0.0002`.

**(a) [4 points]** Write the effective access time formula for demand paging.

**(b) [4 points]** Calculate the effective access time.

**(c) [2 points]** Explain why a small page-fault rate can still heavily affect performance.
```

When asking EAT questions, make unit conversions explicit enough that the problem is fair, but do not solve the conversion inside the question.

---

# 17. Thrashing and Working-Set Question Style

Thrashing questions should test reasoning about locality and frame allocation.

Good prompts:

```md
**(a) [4 points]** Explain what happens when the total demand for frames exceeds the available physical memory.

**(b) [4 points]** Given the following reference string and window size `Delta = 4`, calculate the working set at the marked time.

**(c) [2 points]** Explain how page-fault frequency can be used to control thrashing.
```

Avoid asking only for a definition. Prefer a small scenario, table, or reference string.

---

# 18. Mass-Storage Question Style

Mass-storage questions should test both calculations and algorithmic reasoning.

Good topics:

- HDD structure
- Seek time
- Rotational latency
- Transfer time
- Average I/O time
- HDD scheduling
- FCFS disk scheduling
- SSTF disk scheduling
- SCAN and C-SCAN
- NVM characteristics
- Flash translation layer
- Garbage collection
- Wear leveling
- Error detection/correction
- Swap-space management
- RAID levels and tradeoffs

A strong disk scheduling question should include:

- Initial head position
- Queue of cylinder requests
- Disk range
- Direction of movement for SCAN/C-SCAN
- Request to compute total head movement

Example:

```md
## Question 7 - Mass Storage and Disk Scheduling

**10 Points**

A disk has cylinders numbered `0` to `199`. The current head position is `53`. The pending queue is:

```text
98, 183, 37, 122, 14, 124, 65, 67
```

Assume the head is initially moving toward larger cylinder numbers.

**(a) [4 points]** Calculate the total head movement using FCFS.

**(b) [4 points]** Calculate the total head movement using SCAN.

**(c) [2 points]** Explain why disk scheduling matters less for SSD/NVM devices than for HDDs.
```

---

# 19. I/O Systems Question Style

I/O questions should test the student’s ability to distinguish I/O methods and OS responsibilities.

Good topics:

- I/O hardware concepts: ports, buses, controllers
- Device drivers
- Polling
- Interrupts
- DMA
- Blocking I/O
- Nonblocking I/O
- Asynchronous I/O
- Kernel I/O subsystem
- I/O scheduling
- Buffering
- Caching
- Spooling
- Error handling
- I/O protection
- Performance bottlenecks

Good example:

```md
## Question 8 - I/O Systems

**10 Points**

A network card transfers large blocks of data directly into main memory while the CPU continues executing another process.

**(a) [3 points]** Identify the I/O mechanism being used and explain why it is suitable.

**(b) [3 points]** Compare this mechanism with programmed I/O or polling.

**(c) [2 points]** Explain the role of interrupts in this transfer.

**(d) [2 points]** Give one performance advantage and one possible cost of this mechanism.
```

---

# 20. File-System Interface Question Style

File-system interface questions should test file abstraction, access, directories, and protection.

Good topics:

- File concept
- File attributes
- File operations
- Open-file tables
- File pointers
- Sequential access
- Direct access
- Directory structures
- Single-level directory
- Two-level directory
- Tree-structured directory
- Acyclic graph directory
- General graph directory
- File protection
- Access lists and permission bits
- Memory-mapped files

Good example:

```md
## Question 9 - File-System Interface

**10 Points**

Answer the following:

**(a) [3 points]** Explain why an operating system maintains an open-file table.

**(b) [3 points]** Compare sequential access and direct access with one suitable use case for each.

**(c) [4 points]** A directory structure allows shared files through links. Explain one benefit and one problem that can occur when deleting files.
```

---

# 21. File-System Implementation Question Style

File-system implementation questions should be concrete and often calculation-based.

Good topics:

- File-system layers
- Boot control block
- Volume control block / superblock
- File control block / inode
- Directory implementation
- Linear list directories
- Hash table directories
- Contiguous allocation
- Linked allocation
- FAT
- Indexed allocation
- Multi-level indexed allocation
- Free-space bit vector
- Free-space linked list
- Grouping
- Counting
- Consistency checking
- Journaling / log-structured file systems
- Recovery

Good example:

```md
## Question 9 - File-System Implementation

**10 Points**

A file system uses indexed allocation. The block size is 4 KB and each disk block pointer is 4 bytes.

**(a) [3 points]** How many block pointers can fit in one index block?

**(b) [3 points]** What is the largest file size that can be addressed using a single index block?

**(c) [4 points]** Compare indexed allocation with linked allocation for random access.
```

---

# 22. File-System Internals Question Style

File-system internals questions should focus on mounting, sharing, VFS, and remote file systems.

Good topics:

- Partitions and volumes
- Mount points
- Root partition
- File-system consistency checks during mounting
- File sharing
- Owner/group permissions
- VFS abstraction
- Vnodes/inodes
- Linux VFS objects: inode, file, superblock, dentry
- Remote file systems
- Client-server file systems
- NFS
- NFS mount protocol
- File handles
- NFS architecture layers
- Consistency semantics

Good example:

```md
## Question 9 - File-System Internals

**10 Points**

A Unix-like operating system mounts a remote directory from an NFS server into the local directory tree.

**(a) [3 points]** Explain what changes from the user’s point of view after mounting.

**(b) [3 points]** Explain why VFS is useful in this scenario.

**(c) [2 points]** What is the purpose of a file handle in NFS?

**(d) [2 points]** Give one reason why consistency semantics matter in remote file systems.
```

---

# 23. Past Exam Style to Preserve

The exam should imitate the observed past-exam style.

Past-style question types include:

| Topic Area | Style | Typical Task |
|---|---|---|
| CPU scheduling | Algorithmic | Draw Gantt chart, calculate waiting/turnaround time |
| Synchronization | Conceptual + scenario | Analyze race conditions, semaphores, monitors |
| Deadlocks | Definition + scenario | Conditions, prevention, resource-allocation graph |
| Banker’s Algorithm | Calculation | Need matrix, safe sequence, request decision |
| Main memory | Calculation | Address bits, page table entries, TLB reasoning |
| Virtual memory | Calculation + scenario | Page faults, EAT, page replacement, thrashing |
| Mass storage | Calculation + algorithm | Disk scheduling, I/O time, RAID comparison |
| I/O | Calculation + definition | Programmed I/O, interrupt-driven I/O, DMA, buffering/caching/spooling |
| File systems | Short answer + calculation | Open-file tables, access methods, inodes, allocation methods, corrupted blocks |
| File-system internals | Conceptual + scenario | Mounting, VFS, NFS, remote file-system behavior |

---

# 24. Recommended Topic Distribution Inside the 60% Post-Midterm Portion

For a 100-point mock final, the 60 post-Midterm points should usually be distributed approximately as follows:

| Topic | Chapters | Suggested Points |
|---|---:|---:|
| Virtual memory and page replacement | 10 | 20-30 |
| Thrashing, frame allocation, COW, memory-mapped files | 10 | 5-10 |
| Mass storage and disk/NVM scheduling | 11 | 10-15 |
| I/O systems | 12 | 8-12 |
| File-system interface | 13 | 5-10 |
| File-system implementation and internals | 14-15 | 10-15 |

A good default is:

```text
Chapter 10:       30 points
Chapters 11-12:   20 points
Chapters 13-15:   10 points
Total:            60 points
```

Another good balanced option is:

```text
Chapter 10:       25 points
Chapter 11:       10 points
Chapter 12:       10 points
Chapters 13-15:   15 points
Total:            60 points
```

---

# 25. Recommended Topic Distribution Inside the 40% Cumulative Portion

For a 100-point mock final, the 40 cumulative points should usually be distributed approximately as follows:

| Topic | Chapters | Suggested Points |
|---|---:|---:|
| OS foundations, services, processes, threads | 1-4 | 5-10 |
| CPU scheduling | 5 | 5-10 |
| Synchronization | 6-7 | 10-15 |
| Deadlocks and Banker’s Algorithm | 8 | 10-15 |
| Main memory | 9 | 5-10 |

Do not include all cumulative topics at full depth in one exam. Choose a representative mix and keep the total exactly 40 points.

---

# 26. Quality Checklist Before Finalizing a Mock Final

Before giving the final mock exam, verify:

- [ ] Total points add up to exactly 100.
- [ ] Chapters 10-15 add up to exactly 60 points.
- [ ] Chapters 1-9 add up to exactly 40 points.
- [ ] The exam is visually readable.
- [ ] Sub-questions do not each have separate headings.
- [ ] Recall-based questions do not reveal the answer terms too directly.
- [ ] Code questions ask for output, behavior, or result.
- [ ] At least one virtual-memory calculation is included.
- [ ] At least one post-Midterm 2 storage, I/O, or file-system question is included.
- [ ] Cumulative CPU scheduling, synchronization, or deadlock questions are included only within the 40-point cumulative portion.
- [ ] Tables are used where they improve clarity.
- [ ] The exam resembles the teacher’s expected style.
- [ ] The wording is clear and unambiguous.
- [ ] No unnecessary answer hints are included.
- [ ] No answer-key content is mixed into the exam unless explicitly requested.

---

# 27. Common Mistakes to Avoid

Avoid generating mock finals that:

- Add up to more or less than 100 points
- Ignore the 60/40 final-exam weighting
- Give too many points to CPU scheduling or Banker’s Algorithm
- Treat the final as only Chapters 10-15 and forget cumulative review
- Treat the final as only old midterm topics and forget Chapters 10-15
- Use too many headings
- Include answer terms inside recall questions
- Ask “explain this code” without requiring output or behavior
- Include huge code blocks
- Overload one question with too many unrelated topics
- Give too many hints inside the question
- Use poor visual spacing
- Mix answer key content into the exam unless explicitly requested
- End with an unscaled raw point total

---

# 28. Final Instruction for Future CMPE382 Mock Finals

When generating future CMPE382 mock final exams, follow this priority order:

1. Match the teacher’s style.
2. Enforce the exact final-exam weighting: 60% Chapters 10-15, 40% Chapters 1-9.
3. Keep the exam visually clean.
4. Make the student recall important concepts.
5. Include calculation-based questions.
6. Include scenario-based reasoning.
7. Include virtual-memory, storage, I/O, and file-system topics prominently.
8. Keep cumulative review present but controlled.
9. Ensure the point total is exactly 100.
10. Avoid over-guiding the student.
