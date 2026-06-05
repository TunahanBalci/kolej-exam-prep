# CMPE326 Mock Final Exam Generation Guide

## Purpose

Generate CMPE326 mock final exams that closely match the expected style of the real exam.

The exam should test:

- Conceptual understanding
- Scenario analysis
- Scope and referencing-environment reasoning
- Functional programming reasoning
- Scheme code-writing ability
- Haskell code-output reasoning
- Subprogram and parameter-passing concepts
- Implementation-of-subprograms reasoning
- Ability to recall important definitions without being over-guided

The final mock exam must always be visually readable, well-structured, and add up to exactly **100 points**.

---

# 1. Overall Exam Structure

## Required Total Point Value

Every generated mock final exam must add up to exactly:

```text
100 points
```

Do not produce exams with raw totals such as 120, 150, or 160 points unless explicitly asked.

A good default structure is:

| Section | Internal Topic Focus | Suggested Points |
|---|---|---:|
| Question 1 | Classical definitions and short recall | 8 |
| Question 2 | Scope / visibility / lifetime concepts | 8 |
| Question 3 | Static scope, dynamic scope, or referencing environment | 12 |
| Question 4 | Functional programming concepts | 8 |
| Question 5 | Scheme fundamentals and list-processing concepts | 8 |
| Question 6 | HW3 Scheme code-writing question with subquestions | 18 |
| Question 7 | Haskell code-output question | 8 |
| Question 8 | Subprograms and parameter passing | 10 |
| Question 9 | Implementing subprograms / activation records / chains | 10 |
| Question 10 | Short classical comparison / tracing / scenario question | 10 |
| **Total** |  | **100** |

The exact topic distribution can change, but the total must always be 100. At least 2 questions should be very similar in style and structure to lecture-slide questions or exercises, but not exact copies.

The exam should contain more classical-style questions than pure code-output questions. Code-output should appear only where it is strongly justified, especially for the required Haskell question and small HW3-related subquestions.

---

# 2. Question Title Rule

Question titles in the generated exam must **not reveal the topic**.

Use only:

```md
## Question 1
## Question 2
## Question 3
```

Do **not** use topic-revealing titles such as:

```md
## Question 2 — Static and Dynamic Scoping
## Question 4 — Scheme Matrix Operations from HW3
## Question 7 — Haskell Code Output
```

The topic may be clear from the question statement itself, but the heading must not tell the student which lecture topic is being tested.

This rule applies to every mock exam and every answer sheet.

---

# 3. Visual Formatting Rules

The exam must be easy to read.

Use:

- Clear numbered question titles only
- Short paragraphs
- Tables for scope traces, variable tables, activation records, and parameter-passing data
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
- Topic-revealing question headings

---

# 4. Sub-Question Formatting Rule

Do **not** create a separate Markdown heading for every sub-question.

Good format:

```md
## Question 3

**12 Points**

Consider the following program fragment.

**(a) [4 points]** Determine which declaration of `x` is used at the marked statement under static scoping.

**(b) [4 points]** Determine which declaration of `x` is used at the marked statement under dynamic scoping.

**(c) [4 points]** Give the referencing environment at the marked statement.
```

Bad format:

```md
## 3(a) Static Scope

...

## 3(b) Dynamic Scope

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

# 5. Recall-Based Question Rule

Do not over-reveal the answer inside the question.

For definition questions, avoid listing the exact terms that the student is supposed to remember.

## Example: Variable Visibility

Good:

```md
**(b) [4 points]** A variable can be visible in a program unit without being declared inside that unit. Name and explain the relevant variable category.
```

Bad:

```md
**(b) [4 points]** Explain nonlocal variables.
```

The student should recall:

- The names of the concepts
- Their meanings
- Their consequences
- How the concepts apply to code

This rule applies especially to topics such as:

- Scope and visibility
- Static scope and dynamic scope
- Local, nonlocal, and global variables
- Scope and lifetime
- Referencing environments
- Functional programming fundamentals
- Lambda expressions and higher-order functions
- Scheme `define`, `lambda`, `let`, recursion, and list operations
- Haskell lists, pattern matching, list comprehensions, and lazy evaluation
- Subprograms, parameter-passing methods, and closures
- Activation records, static chains, and dynamic chains

---

# 6. Code Question Rule

For questions that include code, prefer asking for the **output**, **result**, **binding**, or **behavior**, not just explanation.

However, CMPE326 mock finals should not become mostly code-output exams. The style should remain close to the original CMPE382-style classical exam structure: short conceptual questions, tables, scenario analysis, and tracing.

Good:

````md
**(c) [4 points]** What is the output of the following Haskell code? Explain briefly why that output occurs.

```haskell
productList [] = 1
productList (a:x) = a * productList x

main = print (productList [2, 3, 4])
```
````

Bad:

```md
Explain this code.
```

Code questions should usually ask one of the following:

- What is the output?
- What value is returned?
- Which variable binding is used?
- Which variable is hidden?
- What is the referencing environment at a marked point?
- What is the final value of a variable?
- What happens under static scoping?
- What happens under dynamic scoping?
- Which activation record is accessed?
- Which static or dynamic link is followed?
- Which Scheme helper function is missing?
- What list is produced by a Scheme or Haskell expression?

For CMPE326 exams, code snippets should be short and focused.

---

# 7. Scope and Referencing-Environment Question Style

Scope questions are important and should appear in the final.

A strong question should include:

- A short code fragment
- Nested functions, nested blocks, or repeated variable names
- A clear call sequence when dynamic scoping is tested
- One or more marked statements
- A static-scope task
- A dynamic-scope task
- A referencing-environment or final-value task when appropriate

Recommended topics:

- Scope of a variable
- Visibility of a variable
- Local variables
- Nonlocal variables
- Global variables
- Static scope
- Dynamic scope
- Hidden variables
- Static parent and static ancestors
- Blocks and declaration order
- `let` constructs
- Scope vs. lifetime
- Referencing environments

A good scope question may ask students to compare static and dynamic scoping on the same code.

Example structure:

````md
## Question 3

**12 Points**

Consider the following code fragment. Assume the language allows nested subprograms.

```text
procedure big
    x = 3

    procedure sub1
        x = 7
        sub2()

    procedure sub2
        y = x      // point A

    sub1()
```

**(a) [4 points]** Under static scoping, which `x` is referenced at point A? Explain briefly.

**(b) [4 points]** Under dynamic scoping, which `x` is referenced at point A? Explain briefly.

**(c) [4 points]** If `big` calls `sub2` directly instead of calling `sub1`, how does the answer in part (b) change?
````

The solution must show the lookup path, not just the final variable name.

---

# 8. Classical Concept Question Style

Classical questions should appear more often than code-output questions.

Good classical question types include:

- Define a concept and give one short example
- Compare two concepts in a table
- Match a concept to its consequence
- State whether a claim is true or false and justify briefly
- Fill in a table about scope, lifetime, parameter passing, or activation records
- Given a short scenario, identify which concept is being demonstrated

Good format:

```md
## Question 1

**8 Points**

Answer the following briefly.

**(a) [3 points]** Explain what it means for a name to be visible at a statement.

**(b) [3 points]** A variable is declared inside a program unit, while another variable is visible there but declared elsewhere. Name and distinguish these two categories.

**(c) [2 points]** Why can two variables with the same name cause hiding?
```

Another good format:

```md
## Question 2

**8 Points**

Complete the table.

| Situation | Concept Being Tested | Brief Explanation |
|---|---|---|
| A function-local `static` variable keeps its value between calls. | | |
| A variable declared in an inner block has the same name as an outer variable. | | |
| A name is searched by following the calling sequence at run time. | | |
| A name is searched by following the textual nesting of the program. | | |
```

Avoid turning every question into a code-output task.

---

# 9. Functional Programming and Scheme Concept Question Style

Functional programming questions should test reasoning, not only memorization.

Good topics:

- Imperative vs functional programming
- Mathematical functions
- Lambda expressions
- Functional forms
- Higher-order functions
- Function composition
- Apply-to-all / mapping
- Referential transparency
- Lisp lists and prefix notation
- Scheme interpreter behavior
- Scheme primitive functions
- `define`
- `lambda`
- `let`
- `cond` / conditional expressions
- Recursion
- List processing with `car`, `cdr`, `cons`, `null?`, `list`, `append`, `map`, and `apply`

Prefer short classical questions, short comparisons, and small expression evaluation. Do not overuse code-output style.

Good example:

````md
## Question 4

**8 Points**

Answer the following briefly.

**(a) [3 points]** A language design may be based on mathematical functions rather than assignments and changing variables. Explain the main difference between these two styles.

**(b) [3 points]** Explain what it means for a function to always produce the same result for the same parameters.

**(c) [2 points]** Why are functions considered first-class entities in Scheme?
````

Another good example:

````md
## Question 5

**8 Points**

Answer the following.

**(a) [3 points]** What is the purpose of `define` in Scheme?

**(b) [3 points]** What is the purpose of `lambda` in Scheme?

**(c) [2 points]** A list and a function call can both be written using parentheses in Lisp-like languages. How does interpretation determine whether the form is data or a function application?
````

---

# 10. HW3 Scheme Code-Writing Question Style

There must be one code-writing question based on **only the solution of HW3**.

This question should focus on the Scheme matrix-processing solution for:

- `row-max`
- `row-avg`
- `norm-inf`
- Helper functions used by the solution, such as row sum, absolute row sum, average, maximum, or matrix traversal helpers

Do **not** ask a Scheme code-writing question from an unrelated topic.

A strong HW3 question should include:

- A matrix represented as a list of lists
- A partially completed Scheme solution or a requested missing function
- One code-writing sub-question
- One or two short sub-questions about output, recursion, helper functions, or how the code works
- Different matrix sizes, because HW3 states that the solution may be tested on different matrices

The code-writing part should usually ask the student to write **one missing function**, not the entire homework solution.

Good format:

````md
## Question 6

**18 Points**

A matrix is represented as a list of lists in Scheme.

```scheme
(define M
  '((1 2 3)
    (3 3 4)
    (3 2 1)))
```

The following solution uses helper functions to implement one of the required operations.

```scheme
(define (row-sum-abs row)
  ; missing code
)

(define (norm-inf matrix)
  (apply max (map row-sum-abs matrix)))
```

**(a) [10 points]** Write the missing `row-sum-abs` function.

**(b) [4 points]** What is the result of `(norm-inf M)`?

**(c) [4 points]** Briefly explain how the helper function is applied to every row.
````

Another good format:

````md
## Question 6

**18 Points**

Consider the following matrix.

```scheme
(define A
  '((2 -5 1)
    (4 0 -3)
    (-1 -1 -1)))
```

**(a) [10 points]** Write a Scheme function `row-avg` that takes a matrix and returns a list containing the average of each row.

**(b) [4 points]** What is the result of `(row-avg A)`?

**(c) [4 points]** Which part of your function processes one row, and which part applies that operation to all rows?
````

The answer key should accept equivalent correct Scheme solutions, including recursive solutions and solutions using standard Scheme list operations, unless the question explicitly restricts the method.

---

# 11. Haskell Code-Output Question Style

There should be exactly one Haskell code-output question unless the user explicitly requests otherwise.

The Haskell question should be short and traceable by hand.

Good topics:

- List notation
- Arithmetic series with `..`
- List concatenation using `++`
- The colon operator `:`
- Pattern matching on lists
- Recursive functions over lists
- Factorial using list products
- Length using recursion
- List comprehensions
- Guards or filters in list comprehensions
- Backtick operator usage such as ``mod`` or ``div``
- Quicksort-style recursive list processing
- Lazy evaluation with simple infinite lists

Avoid very large Haskell programs.

Good example:

````md
## Question 7

**8 Points**

What is the output of the following Haskell expressions? Explain briefly.

```haskell
[2, 4..10]
[1, 3] ++ [5, 7]
1:[3, 5, 7]
[n * n | n <- [1..5], n `mod` 2 == 1]
```

**(a) [5 points]** Write the resulting list for each expression.

**(b) [3 points]** Explain the difference between `++` and `:` in Haskell lists.
````

Another good example:

````md
## Question 7

**8 Points**

Consider the following Haskell function.

```haskell
len [] = 0
len (a:x) = len x + 1
```

**(a) [3 points]** What is the result of `len [10, 20, 30]`?

**(b) [2 points]** Which equation is used for the empty list?

**(c) [3 points]** Which part of `(a:x)` represents the head and which part represents the tail?
````

The solution should show intermediate reasoning for recursion-based code-output questions.

---

# 12. Subprogram Question Style

Subprogram questions should combine definitions with small scenarios.

Good topics:

- Subprogram definitions
- Function vs procedure
- Formal parameters and actual parameters
- Local referencing environments
- Local variables: stack-dynamic vs static
- Parameter-passing modes: in, out, inout
- Pass-by-value
- Pass-by-result
- Pass-by-value-result
- Pass-by-reference
- Pass-by-name
- Type checking of parameters
- Overloaded subprograms
- Generic subprograms
- Design issues for functions
- Closures
- Coroutines

A good subprogram question may ask students to match parameter-passing behavior to a code effect.

Good format:

````md
## Question 8

**10 Points**

Answer the following.

**(a) [3 points]** A language supports several ways of transmitting data between a caller and a called subprogram. Name and explain the three general parameter-passing modes.

**(b) [4 points]** Complete the table.

| Method | Can the actual parameter change after the call? | Brief reason |
|---|---|---|
| Pass-by-value | | |
| Pass-by-result | | |
| Pass-by-value-result | | |
| Pass-by-reference | | |
| Pass-by-name | | |

**(c) [3 points]** Explain what a closure contains and why the referencing environment is part of it.
````

This question type is recommended because it tests conceptual understanding without becoming too open-ended.

---

# 13. Implementing Subprograms Question Style

Implementation questions should test how subprogram calls are represented and accessed at run time.

Good topics:

- Subprogram linkage
- Call semantics
- Return semantics
- Activation records
- Activation record instances
- Stack-dynamic local variables
- Recursion and run-time stack
- Dynamic link
- Static link
- Static chain
- Dynamic chain
- Accessing nonlocal variables
- Nested subprogram implementation
- Blocks and local variables
- Implementing dynamic scoping
- Deep access and shallow access

Questions should often use tables.

Good example:

````md
## Question 9

**10 Points**

Assume `main` calls `A`, `A` calls `B`, and `B` calls `C`. The language uses stack-dynamic local variables.

**(a) [3 points]** Draw the order of activation record instances on the run-time stack when execution is inside `C`.

**(b) [3 points]** Which link represents the caller relationship?

**(c) [4 points]** In a statically scoped language with nested subprograms, which mechanism is used to access nonlocal variables? Explain briefly.
````

Another good format:

````md
## Question 9

**10 Points**

The following call sequence occurs:

```text
main -> sub2 -> sub1
```

Each subprogram has local variables with some repeated names.

| Subprogram | Local Variables |
|---|---|
| main | c, d |
| sub2 | b, c |
| sub1 | a, b |

**(a) [4 points]** Give the visible variables while execution is inside `sub1` under dynamic scoping.

**(b) [3 points]** Which variables are hidden?

**(c) [3 points]** Explain how the dynamic chain is used to find a nonlocal variable.
````

The solution must show the search path or stack reasoning, not just the final answer.

---

# 14. Past Exam Style to Preserve

The exam should imitate the observed past-exam style.

Past-style question types should be adapted to CMPE326 topics as follows:

| Topic Area | Style | Typical Task |
|---|---|---|
| Scope | Code tracing + conceptual | Static vs dynamic binding, hidden variables, final values |
| Referencing environments | Table / trace | List visible variables at marked program points |
| Scope and lifetime | Short answer + table | Determine scope and lifetime of variables in C/C++-like code |
| Functional programming | Classical short answer | Compare paradigms, define concepts, explain referential transparency |
| Scheme | Classical + short expression reasoning | `define`, `lambda`, `let`, recursion, list operations |
| HW3 Scheme solution | Code writing + subquestions | Missing `row-max`, `row-avg`, `norm-inf`, or helper function |
| Haskell | One code-output question | Lists, `++`, `:`, pattern matching, list comprehensions, lazy evaluation |
| Subprograms | Conceptual + scenario | Parameter-passing modes, closures, local variables |
| Implementing subprograms | Trace / table | Activation records, static chains, dynamic chains, shallow/deep access |

---

# 15. Lecture-Slide Similarity Rule

At least **2 questions** in every generated CMPE326 mock final should be very similar in style and structure to questions or exercises that appear in the lecture slides.

These questions must **not** copy the lecture-slide questions exactly. They should preserve the same exam-like pattern while changing the concrete details, variable names, values, code structure, or scenario.

Good lecture-slide-inspired question types include:

- Static-scope vs dynamic-scope tracing with a modified call sequence
- Referencing-environment tables at marked program points
- Scope and lifetime tables for C/C++-like variables
- Short classical questions asking for definitions with examples
- Functional-programming concept questions similar to the lecture review questions
- Scheme expression evaluation or missing helper function questions based on lecture-style Scheme examples
- Haskell list-processing or recursive function tracing questions similar to the Haskell slide examples

Good approach:

```md
Use the same reasoning pattern as a slide exercise, but change the program fragment, variable names, call sequence, matrix values, list values, or sub-question wording.
```

Bad approach:

```md
Copy the exact question from the lecture slide without meaningful changes.
```

The two lecture-slide-inspired questions should still follow all other rules:

- Their headings must be only `Question X`.
- They must not reveal the topic in the heading.
- They must fit into the 100-point structure.
- They should be written in the same clean classical style as the original CMPE382 instruction file.
- They should not add extra code-output questions beyond the required single Haskell code-output question unless explicitly requested.

---

# 16. Recommended 100-Point Mock Final Template

Use this as the default template unless the user asks for a different topic emphasis. At least 2 of the questions in this structure should be lecture-slide-inspired modified questions.

| Question | Internal Topic Focus | Points |
|---|---|---:|
| Q1 | Classical definitions and short recall | 8 |
| Q2 | Scope / lifetime / visibility table | 8 |
| Q3 | Static scope, dynamic scope, and referencing environment | 12 |
| Q4 | Functional programming concepts | 8 |
| Q5 | Scheme / Lisp concepts, mostly classical | 8 |
| Q6 | HW3 Scheme code-writing question with subquestions | 18 |
| Q7 | Haskell code-output question | 8 |
| Q8 | Subprograms and parameter passing | 10 |
| Q9 | Implementing subprograms: activation records, static/dynamic chains | 10 |
| Q10 | Short conceptual / comparison / tracing question | 10 |
| **Total** |  | **100** |

When generating the actual exam, the headings must still be only `Question 1`, `Question 2`, etc. Do not include the internal topic focus in the exam headings.

The HW3 Scheme code-writing question and one Haskell code-output question should be included unless the user explicitly asks for a different exam composition.

---

# 17. Quality Checklist Before Finalizing a Mock Exam

Before giving the final mock exam, verify:

- [ ] Total points add up to exactly 100.
- [ ] The exam is visually readable.
- [ ] It is labeled as a final exam, not a midterm.
- [ ] Question headings do not reveal topics.
- [ ] Each main question heading is only `Question X`.
- [ ] Sub-questions do not each have separate headings.
- [ ] The question does not reveal recall-based answers too directly.
- [ ] The exam includes more classical-style questions than code-output questions.
- [ ] At least 2 questions are very similar in style and structure to lecture-slide questions or exercises, without copying them exactly.
- [ ] Code questions ask for output, behavior, binding, or result.
- [ ] Scope questions include clear call sequences when dynamic scoping is tested.
- [ ] Referencing-environment questions specify the exact program point.
- [ ] The HW3 code-writing question is only from the HW3 solution area.
- [ ] The HW3 question includes `row-max`, `row-avg`, `norm-inf`, or helper functions used by these functions.
- [ ] The HW3 question includes one code-writing part and one or two subquestions about output or how the code works.
- [ ] Exactly one Haskell code-output question is included unless otherwise requested.
- [ ] Subprogram questions include parameter passing, closures, or local variable behavior.
- [ ] Implementation questions use activation records, static chains, dynamic chains, or dynamic-scope access methods.
- [ ] Tables are used where they improve clarity.
- [ ] The exam resembles the teacher’s expected style.
- [ ] The wording is clear and unambiguous.
- [ ] No unnecessary answer hints are included.

---

# 18. Common Mistakes to Avoid

Avoid generating mock exams that:

- Add up to more or less than 100 points
- Call the exam a midterm
- Use topic-revealing question headings
- Use too many headings
- Include the answer terms inside recall questions
- Ask “explain this code” without requiring output, result, binding, or behavior
- Include huge code blocks
- Ask Scheme code-writing questions unrelated to HW3
- Ask the entire HW3 solution when a missing-function question would be better
- Add multiple code-output questions when classical questions would better match the intended style
- Omit the required HW3 Scheme code-writing question
- Omit the required Haskell code-output question
- Copy lecture-slide questions exactly instead of creating similar modified versions
- Forget to include at least 2 lecture-slide-inspired questions
- Overload one question with too many unrelated topics
- Give too many hints inside the question
- Use poor visual spacing
- Mix answer key content into the exam unless explicitly requested
- End with an unscaled raw point total

---

# 19. Final Instruction for Future Mock Finals

When generating future CMPE326 mock finals, follow this priority order:

1. Match the teacher’s style.
2. Keep the exam visually clean.
3. Label it as a final exam.
4. Use only numbered question headings without topic names.
5. Make the student recall important concepts.
6. Prefer classical-style questions, tables, and scenario reasoning over excessive code-output questions.
7. Include the HW3 Scheme code-writing question from the HW3 solution only.
8. Include exactly one Haskell code-output question unless otherwise requested.
9. Include at least 2 questions that are very similar in style and structure to lecture-slide questions, but not exact copies.
10. Include scenario-based scope and subprogram reasoning.
11. Ensure the point total is exactly 100.
12. Avoid over-guiding the student.
