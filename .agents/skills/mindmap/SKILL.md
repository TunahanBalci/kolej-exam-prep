# MIND MAP CREATOR SKILL

## Goal

Create a mindmap for the user, based on the provided lecture notes, to help them prepare for an exam. The mind map should be clear, concise and cover all necessary topics, sub-topics, and information from the specified chapters. The mindmap should be structured in a way that facilitates easy understanding and retention of the material.

## Mindmap Creation

The mind map is a **single Markdown file**. `template.html` is a viewer: the user opens your `.md` file in it with the **Open** button. Rules:

- **Output only the Markdown file.** Make it downloadable, named after the topic, e.g. `os-ch3-processes.md`.
- **Do not edit, rewrite or output `template.html`.**
- **Do not write HTML, JSON, node IDs, colours or layout data.** The viewer derives all of these from the Markdown.

### Expected format (schema)

Headings are nodes. Everything under a heading, down to the next heading, is that node's content.

| Element | Syntax | Notes |
|---|---|---|
| Root node (centre) | `# Title` | Exactly **one** `#` heading, and it must be the **first line** of the file. |
| Main branch | `## Title` | Each `##` gets its own colour; everything under it inherits that colour. |
| Sub-topic, detail, … | `###`, `####`, `#####`, … | The number of `#` sets the depth. There is no depth limit. Never skip a level (`##` → `####`). |
| Node title | text after the `#`s | Keep it short (2–6 words). Inline `**bold**`, `` `code` `` and `$math$` are allowed. |
| Paragraph | plain text | Short explanation, terms and definitions. |
| Unordered list | `- item` | Use whenever there are several items (see Rules). Nest with 2 spaces. |
| Ordered list | `1. step` | Use whenever order or sequence matters. |
| Emphasis | `**bold**`, `*italic*`, `` `inline code` `` | Use `` `code` `` for identifiers like `fork()` or `SCHED_FIFO`. |
| Inline math | `$...$` | LaTeX, e.g. `$O(n \log n)$`. Write a literal dollar sign as `\$`. |
| Display math | `$$...$$` | LaTeX on its own line(s). |
| Code block | ```` ```lang ```` … ```` ``` ```` | Always give the language. Highlighted: `c`, `cpp`, `java`, `python`, `scheme`, `haskell`, `javascript`, `bash`, `sql` (others show as plain text). |
| Code result | `**Result:** ...` | A line right after a code block, when the output matters. |

Not supported: raw HTML (it is shown as plain text, not rendered), images, and text before the first heading (it is ignored).

### Example

````markdown
# Operating Systems: CPU Scheduling
Decides which ready process gets the CPU next.

## Scheduling Criteria
- **CPU utilisation:** keep the CPU busy
- **Throughput:** processes completed per time unit
- **Turnaround time:** $T_{finish} - T_{arrival}$

## Algorithms
### First-Come, First-Served (FCFS)
Runs processes in arrival order.
- **Problem:** convoy effect, where short jobs wait behind a long one

### Round Robin (RR)
Each process runs for at most one time quantum $q$, then goes to the back of the queue.
1. Take the process at the head of the ready queue
2. Run it for up to $q$
3. If it hasn't finished, put it back at the tail

#### Example
```c
while (!queue_empty(ready)) {
    proc *p = dequeue(ready);
    run(p, QUANTUM);
    if (!p->done) enqueue(ready, p);
}
```
**Result:** every process gets the CPU at least once every $(n-1)q$ time units.
````

## Rules:

- The reader should be able to understand >80% of the information in the given sources solely by reading the mindmap.
- Explain each topic and sub-topic clearly. 
- Cover all information bases. 
- Always include the properties or shortcomings of a topic: What distinguishes it?
- If something (a topic, a model, an algorithm, an approach, etc.) solves an existing problem, include this information.
- Do not go into extreme or redundant details unless necessary. Example: no need to include Matemathical background (e.g. proofs, derivations, etc.) unless it is necessary to understand the topic.
- Explain how something works.
- Do not treat the lecture notes as the single source of truth. Use the knowledge to make the mindmap more understandable and easier to remember.
- If a topic contains any elements or concepts listed, use unordered lists instead of expressing it in sentences. If order or sequence matters, use ordered lists. Always cover all concepts of a topic.
- If you need to state or list multiple elements in a sentence, use a list instead, to increase readability.

>   Bad list example:
>   "System programs usage area: File manipulation, status information, 
>   file modification, programming-language support"
> 
>   Good list example:
>   "System programs usage area:
>   - File manipulation
>   - Status information
>   - File modification
>   - Programming-language support"
>
>   Bad sequence example: 
>   "Each system call usually has a number. The system-call interface indexes a table, 
>   invokes the intended kernel routine, and returns status and results to the caller", 
>
>   Good sequence example:
>   "Each system call usually has a number.
>   1- System-call indexes a table
>   2- Invokes the intended kernel routine
>   3- Returns status and results to the caller"

## Topic / Sub-topic Boundaries

### Topic
A topic is the next depth level after a chapter, meaning, a chapter consists of multiple topics.
Assume depth level of a chapter = 1, then depth level of a topic = 2.

### Sub-topc
A sub-topic is the next depth level after a topic or sub-topic.
Assume depth level of a chapter = 1, then depth level of a topic = 2, and depth level of a sub-topic is 3 or more

### Concept
A concept is the last depth level. It explains a single idea, concept or definition, and has no multiple elements listed. It is not big enough to be a sub-topic, and generally, only a small piece of text is enough to describe it.

## Information to include
For all covered chapters, you should read all information from the start of that chapter. Include ALL topics within that chapter. These may include, but not limited to: problems, theorems, models, methods, algorithms, properties, etc. If the user provides a page range, include information in that page range instead.

Include any terms/definitions you come across inside the Node of that specific topic.
