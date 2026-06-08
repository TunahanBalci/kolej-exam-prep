
> VERSION: Mind Map Creation Guide With "Include Code Blocks" Instruction 

# BEGIN - Mind Map Creation Guide

## Discipline
Treat all directions in this instruction set as a hard constraint.

## MindMap Generation

To create the mindmap, use the HTML file provided by the user as a template.
The template file contains all necessary visual structure. Template rules:
    - Use the template's structure as is.
    - Do not implement additional features or fixes.
    - Do not change the visual design in any way.
    - Change only the content inside the template.

Update the template with the actual mindmap content, while following template rules.

## Purpose
Prepare the user for an exam. Forming a clear mind-map, enabling the user to comprehend the covered chapter(s)
in all aspects, while keeping explanations concise.

## Covered Chapters 
Covered chapters will be specified by the user.

## Rules:

- Explaining each topic and sub-topic clearly. 
- Cover all information bases. 
- If something (a topic, a model, an algorithm, an approach, etc.) has certain shortcomings/problems, include these problems.
- If something (a topic, a model, an algorithm, an approach, etc.) solves an existing problem, include this information.
- No need to include formulas
- Explain how something (a topic, a model, an algorithm, an approach, etc.) works.
- No need to treat the provided lecture notes as the single source of truth.
- For each topic, understand what it is and what information it gives, and explain it in your own terms; like when a user asks "what is this topic in the slides? explain".
- When explaining a topic, dont add unnecessary information, as this will be a focused, exam-pr
- If a topic contains sub-topics or elements listed, use unordered lists instead of expressing it in sentences. If order or sequence matters, use ordered lists.

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

## Information to include
For all covered chapters, you should read all information from the start of that chapter, until the slides move on to a completely different chapter that is not covered. Include ALL topics within that chapter. These may include, but not limited to: problems, theorems, models, methods, algorithms, properties, etc. If the user provides a page range, include information in that page range.

If a topic includes a code block as an example or directly, add a concise code block example part as a sub-tree/child of that Node. The example does not need to be the exact code block provided in lecture notes, however it must be clear, and it must contain a concise description on how it works.

Include any terms/definitions you come across inside the Node of that specific topic.

# END - Mind Map Creation Guide