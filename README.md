# KOLEJ EXAM PREPARATION

---

### Purpose
This repository acts as an archive. It stores instructions to create mock exams that are statistically similar to the real ones, using AI. In this use case, the project contains markdown files for instructions.

> Content:
>
> - Mock exam instructions:
>   - Midterm(s)
>   - Final
> - Project preparation instructions
> - Mind map generation templates

<br>

### Mock Exam Generation

Explains how to properly use an instruction file to create a mock exam.

1. Download the instruction file you wish to use.
2. Download course contents (lecture notes) from LMS.
3. Convert course contents into markdown (.md) format.
> AI tools can convert lecture notes from PDF/PPTX to markdown easily.
4. Copy exam information given by the lecturer (which topics are included, question types, question distribution, etc.)
5. Attach the instruction file, converted course content markdown files, to a powerful AI model (ChatGPT 5.5+, for example), and use this prompt:

```
Exam-specific information:
<Lecturer's Mail or any other custom instructions>

---

According to the attached lecture notes, 
instruction file, and the exam-specific information,
create 3 mock exams.

The created mock exams must cover all bases of the
topics mentioned in exam-specific information part.

Mock exams must have alternating questions,
with all 3 mock exams covering all possible question
styles and exam scenarios.

Choose questions that will be the most likely come up
in the real exam.

Export created mock exams as downloadable MD files.
Export each mock exam's answer sheet as downloadable MD file.
```
> [!NOTE]
> Replace `<Lecturer's Mail>` part with the actual exam mail.

<br>

### Verified Instructions

Contains the list of verified / tried out instructions, with their "usefulness" scores of 1 through 5, with 5 being extremely useful.

> Instruction files that are not verified / tried out are not included, and they should be considered as drafts.

<br>
All verified instructions:<br><br>


| COURSE CODE | INSTRUCTION NAME     | SCORE |
|-------------|----------------------|-------|
| CMPE382     | MIDTERM-2_SPRING2026 | ⭐⭐⭐⭐⭐   |


<br>


### Mind Map Generation

Instructions on how to create a mind map of a course, using lecture notes and templates provided here.

1. Download mind map markdown instructions, you may edit it to your liking.
> Currently these instructions state not to include any formulas, but you may change this.
2. Download the mind map HTML template.
4. Attach markdown and HTML templates and your lecture notes,
5. Select chapter(s) to cover, and give this prompt to a strong AI model:
```
According to the provided HTML template, lecture notes and mind map instructions, create a mindmap.

Included chapter(s):
- <CHAPTER>
- >CHAPTER> (pg. X - Y)

```
> [!TIP] 
> You can specify page ranges. For example:
> - Semaphores (pg. 150-200)
>
> For optimal results, keep covered chaptes part with chapters that are 50-150 pages long TOTAL.


<br>

### Contribution

_"Knowledge is power. Knowledge shared is power multiplied."_ <br>-- Robert Noyce

If you have anything to add to this archive, feel free to fork the repository and create a merge request!

<br>

### Disclaimer

Instruction files **DO NOT** contain any information regarding confidential past exam documents. These instruction files do not expose any private coursework, and they are purely for educational/study purposes.


For any legal requests, you can reach me (TunahanBalci) by creating a new issue. I will be responding to created issues.
