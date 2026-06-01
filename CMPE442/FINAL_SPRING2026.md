# CMPE442 Mock Final Exam Generation Guide

## Purpose

Generate CMPE442 mock final exams that closely match the expected style of the real final exam, using the provided CMPE442 lecture notes as the source of coverage.

The mock final exam should test:

- Conceptual understanding of machine learning terminology and model behavior
- Ability to distinguish learning settings, model types, and evaluation setups
- Ability to use only essential, low-computation equations on small machine learning datasets
- Algorithm tracing ability for supervised and unsupervised algorithms
- Interpretation of model behavior from tables, plots, confusion matrices, and simple diagrams
- Recall of important definitions without the question giving away the answer
- Practical reasoning about overfitting, underfitting, regularization, validation, preprocessing, and model selection

The final mock exam must always be visually readable, well-structured, and add up to exactly **100 points**.

---

# 1. Required Overall Exam Structure

## Required Total Point Value

Every generated CMPE442 mock final must add up to exactly:

```text
100 points
```

Do not generate raw totals such as 110, 120, or 150 points unless explicitly requested.

## Default Final Exam Structure

Use this structure as the default because it matches the information given about the real final:

| Section | Question Type | Suggested Points |
|---|---|---:|
| Section A | True / False | 30 |
| Section B | Multiple Choice | 5 |
| Section C | Fill in the Blank | 5 |
| Section D | Short Answer / Classical Questions | 20 |
| Section E | Problem Solving / Algorithm Tracing | 40 |
| **Total** |  | **100** |

This keeps the True / False section important but reduces it to **30 statements**, while increasing the weight of classical short-answer questions. The exam should feel less like a test bank and more like a realistic final with conceptual reasoning and manageable problem solving.

## Required Topic Split

The final mock exam must use this topic weighting unless the user explicitly gives a different distribution:

| Coverage Period | Topics | Required Weight |
|---|---|---:|
| Before midterm | Earlier / pre-midterm lecture topics | 35% |
| After midterm | Later / post-midterm lecture topics | 65% |

The split applies to the whole 100-point exam, not only to the problem-solving section. T/F, MCQ, fill-in-the-blank, short-answer, and problem-solving questions should collectively respect the **35% before-midterm / 65% after-midterm** balance. Later topics should have stronger representation, but earlier foundations must still appear.

---

# 2. True / False Section Rule

The mock final should normally include:

```text
30 True / False questions
1 point each
Total: 30 points
```

Use the same penalty logic expected from the midterm:

```text
3 wrong answers eliminate 1 correct answer.
Blank answers do not affect the score.
```

Recommended scoring formula:

```text
T/F Score = max(0, Correct - Wrong / 3)
```

Do not make the T/F section easier by giving clustered hints. Statements should be mixed across topics instead of ordered as a mini-summary of the lecture notes.

A good T/F section should include:

| Topic Area | Approximate Number of Statements |
|---|---:|
| Pre-midterm foundations, data, regression, validation, regularization, logistic regression, k-NN, decision trees | 10–11 |
| Post-midterm neural networks, CNNs, RNNs, autoencoders, NLP basics | 4–5 |
| Post-midterm SVMs, kernels, ensembles, random forests, boosting | 5–6 |
| Post-midterm clustering, GMM/EM, PCA, dimensionality reduction | 6–7 |
| Post-midterm Bayesian decision theory, association rules, reinforcement learning | 2–3 |

The exact distribution can vary slightly, but the T/F section must still roughly respect the 35% before-midterm / 65% after-midterm split.

## T/F Quality Rules

T/F statements must be:

- Standalone and unambiguous
- Short enough to read quickly
- Focused on one idea only
- Balanced between true and false statements
- Mixed in difficulty
- Based on lecture-note terminology and examples, but not copied directly from slides

Avoid:

- Double-negative statements
- Two independent claims inside one statement
- Statements where one word makes the answer trivial
- Excessive use of absolute wording such as “always” and “never”
- Statements that merely ask whether a memorized sentence from the notes is exactly repeated
- Statements that reveal the answer by including an explanation inside the statement

---

# 3. Less Test-Type, More Problem-Type Rule

The lecturer stated that the final will be similar to the midterm, but with fewer test-type questions and more problem-type questions.

Therefore:

- Use exactly 30 T/F questions.
- Keep Multiple Choice short: usually **5 points only**.
- Do not create a large MCQ section unless explicitly asked.
- Use the remaining points mainly for short-answer/classical questions and algorithm tracing.
- At least **40 points** should be problem solving or algorithm tracing.
- At least **65 points** should require reasoning beyond choosing an option.

A mock final that has 30 T/F + 30 MCQ + 40 other points is not appropriate for this final.

---

# 4. Lecture Coverage Map

Use the full CMPE442 lecture notes as the source. The exam should be cumulative unless a narrower coverage range is explicitly given.

| Lecture Note Range | Topic Block | Mock Exam Usage |
|---|---|---|
| Pages 1–81 | ML definition, task/experience/performance, why ML, supervised/unsupervised learning, instance/model-based learning, data types, training/inference | T/F, fill-in-the-blank, short conceptual questions |
| Pages 82–162 | Supervised learning, notation, linear regression, gradient descent, stochastic/batch gradient descent, polynomial regression, feature normalization | T/F, short answer, calculation/problem solving |
| Pages 163–194 | Learning curves, underfitting/overfitting, bias/variance, regularization, model selection, cross-validation, feature selection | T/F, short answer, scenario analysis |
| Pages 195–255 | Logistic regression, decision boundaries, cost function, gradient descent, multiclass/softmax, confusion matrix, precision, recall, F1 | T/F, MCQ, metric calculation, algorithm tracing |
| Pages 256–276 | Nearest neighbor and k-NN, similarity/distance, scaling issues, weighted neighbors, dangerous examples | T/F, short calculation, small classification problem |
| Pages 277–340 | Decision trees, Hunt’s algorithm, split conditions, Gini, entropy, information gain, gain ratio, classification error | T/F, impurity/split calculation, tracing |
| Pages 341–380 | Feature types, central tendency, dispersion, histograms, correlation, data cleaning, missing/noisy data, transformations | T/F, fill-in-the-blank, preprocessing scenario |
| Pages 381–593 | Neural networks, perceptron, MLP, cost/loss, learning, backpropagation concepts, RNNs, LSTM/GRU, autoencoders, NLP feedforward/RNN models, CNNs | T/F, short answer, forward-pass/parameter-count/output-shape problems |
| Pages 594–688 | SVMs, margins, support vectors, hard/soft margin, C, slack variables, kernels, RBF, polynomial kernels, SVM regression, VC/generalization ideas | T/F, short answer, margin/kernel/scenario questions |
| Pages 690–790 | Ensemble learning, voting, bagging, random forests, bootstrapping, out-of-bag data, boosting, AdaBoost | T/F, short answer, algorithm tracing |
| Pages 792–962 | Clustering, quality of clustering, k-means, k-medoids, hierarchical clustering, cluster validity, k-means implementation, elbow method, GMM, MLE, EM | T/F, k-means tracing, GMM/EM reasoning, clustering-quality questions |
| Pages 963–1078 | PCA, curse of dimensionality, covariance matrix, eigenvectors/eigenvalues, projection, reconstruction, number of PCs, feature selection vs extraction, FA, MDS, LDA, CCA, Isomap, LLE | T/F, short answer, PCA calculation/projection problem |
| Pages 1079–1103 | Bayesian decision theory, Bayes rule, losses, risks, reject option, discriminant functions, utility theory | Mostly T/F, short answer, small decision-risk problem |
| Pages 1104–1108 | Association rules, association measures, Apriori | Mostly T/F or fill-in-the-blank |
| Pages 1109–1137 | Reinforcement learning, K-armed bandit, MDP elements, policy, cumulative reward, partial observability, Tiger problem | Mostly T/F, short answer, simple scenario question |

Do not let early introductory topics dominate the final. Later topics should have strong representation, especially in problem-solving questions.

---

# 5. Recommended Topic Weighting

Unless the user gives a specific final coverage distribution, use this approximate weighting:

| Topic Group | Coverage Period | Suggested Points |
|---|---|---:|
| Foundations, data, preprocessing, feature types | Before midterm | 6–8 |
| Regression, logistic regression, validation, regularization, metrics | Before midterm | 17–20 |
| k-NN and decision trees | Before midterm | 8–10 |
| Neural networks, CNNs, RNNs, autoencoders, NLP basics | After midterm | 12–15 |
| SVMs and ensemble methods | After midterm | 14–17 |
| Clustering, GMM/EM, PCA, dimensionality reduction | After midterm | 25–28 |
| Bayesian decision theory, association rules, reinforcement learning | After midterm | 6–8 |

The final exam should feel broad, but not shallow. Prefer conceptual/classical reasoning and a few meaningful tracing problems over many computationally heavy questions. The total should approximately satisfy **35 points before midterm** and **65 points after midterm**.

---

# 6. Visual Formatting Rules

The generated mock exam must be easy to read.

Use:

- Clear main section titles
- Clean tables for datasets, confusion matrices, vectors, centroids, and model outputs
- Short paragraphs
- Simple Markdown formatting
- Horizontal separators between major sections
- Code blocks only when pseudocode or formulas must be visually separated

Avoid:

- Dense walls of text
- Too many nested headings
- Over-explaining concepts inside the question
- Excessive bold formatting
- Long lecture-like introductions before questions
- Answer-key content inside the exam body

---

# 7. Sub-Question Formatting Rule

Do **not** create a separate Markdown heading for every sub-question.

Good structure:

```md
## Question 5 — Problem Solving

**10 Points**

A small dataset is given below.

**(a) [3 points]** Perform the required first calculation.

**(b) [4 points]** Continue the algorithm for the specified step.

**(c) [3 points]** State the final result and justify it briefly.
```

Bad structure:

```md
## 5(a)
...

## 5(b)
...

## 5(c)
...
```

Sub-questions should usually be written as:

```md
**(a) [x points]** ...
**(b) [x points]** ...
**(c) [x points]** ...
```

---

# 8. No Answer-Leakage Rule

The questions themselves must not reveal the answer or give unnecessary hints.

For recall-based questions, do **not** list the exact terms that the student is expected to remember.

Good style:

```md
**(a) [3 points]** A model performs very well on the training set but poorly on unseen data. Name the issue and state one appropriate remedy.
```

Bad style:

```md
**(a) [3 points]** The model is overfitting. Explain overfitting and regularization.
```

Good style:

```md
**(b) [4 points]** A learning algorithm must choose between several candidate models. Explain how the data should be used to make this choice reliably.
```

Bad style:

```md
**(b) [4 points]** Explain hold-out cross-validation and k-fold cross-validation for model selection.
```

Good style:

```md
**(c) [4 points]** A classifier returns the following prediction counts. Compute the requested evaluation values.
```

Bad style:

```md
**(c) [4 points]** Use precision, recall, and F1 score, where F1 is the harmonic mean of precision and recall.
```

This rule applies especially to:

- Learning types
- Generalization approaches
- Model evaluation metrics
- Overfitting and underfitting
- Bias/variance behavior
- Regularization methods
- Validation methods
- Distance-based classification
- Decision-tree impurity measures
- Neural network components
- SVM margin and kernel concepts
- Ensemble methods
- Clustering methods
- Dimensionality reduction methods
- Bayesian decision terminology
- Reinforcement learning components

---

# 9. Multiple Choice Rule

Multiple choice questions should be limited and purposeful.

Recommended MCQ size:

```text
5 questions × 1 point = 5 points
```

MCQs should test distinctions that are easy to confuse, such as:

- Learning setting vs task type
- Model behavior under scaling or regularization
- Evaluation metric interpretation
- Algorithm assumption or limitation
- Which method is appropriate for a given scenario

MCQs should not be trivial vocabulary questions unless the vocabulary is frequently confused.

Avoid:

- Options where only one answer is obviously technical
- “All of the above” as a frequent option
- “None of the above” as a frequent option
- Options that differ only by wording instead of concept
- Questions that reveal the correct answer by over-describing one option

---

# 10. Fill-in-the-Blank Rule

Fill-in-the-blank questions should be short and exact.

Recommended size:

```text
5 blanks × 1 point = 5 points
```

Use fill-in-the-blank for:

- Important terms
- Small formula components
- Missing algorithm step names
- Short model-selection or evaluation vocabulary
- Core definitions where the answer is one phrase

Avoid blanks that are too open-ended.

Bad:

```md
Machine learning is ________.
```

Good:

```md
In a supervised dataset, the desired output values are called ________.
```

Do not include another word in the sentence that directly gives away the blank.

---

# 11. Short Answer Rule

Short-answer / classical questions should usually be worth:

```text
3–5 points each
Total: about 20 points
```

They should require concise reasoning, not long essays. This section should be larger than before because the revised target is to include more classical questions and fewer pure test-type questions.

Good short-answer topics:

- Why training error alone is not enough for model selection
- Why scaling matters for distance-based models or gradient descent
- What changes when model complexity increases
- What type of issue is shown by a learning curve
- Why an ensemble can improve predictions
- Why high-dimensional data can harm generalization
- Why unsupervised learning cannot be evaluated exactly like supervised classification

Avoid asking the student to “write everything you know about” a topic.

---

# 12. Problem-Solving and Algorithm-Tracing Section

The final should contain at least:

```text
40 points of problem solving / algorithm tracing, with low arithmetic burden
```

Recommended structure:

| Problem | Topic | Suggested Points |
|---|---|---:|
| Problem 1 | Model evaluation, validation, metrics, or simple regression/logistic reasoning | 8–10 |
| Problem 2 | k-NN or decision-tree easy calculation/tracing | 8–10 |
| Problem 3 | Neural network/CNN/SVM/ensemble conceptual tracing | 8–12 |
| Problem 4 | Clustering/GMM/PCA/dimensionality-reduction tracing or interpretation | 10–14 |
| Optional Small Problem | Bayesian decision theory, association rules, or reinforcement learning | 4–6 |

A strong final usually contains 4 medium-sized problems rather than 10 tiny problems, but the computations inside those problems should remain short and exam-realistic.

Problem statements should provide only the data needed to solve the task. Do not include hidden hints or unnecessary reminders of the method.

---

# 13. Recommended Problem Styles by Topic

## Regression / Logistic Regression / Evaluation

Possible problem styles:

- Compute predictions from a given hypothesis
- Perform one small gradient-descent update
- Interpret a decision boundary from given parameters
- Compute entries of a confusion matrix
- Compute evaluation metrics from a confusion matrix
- Compare training, validation, and test behavior
- Choose a model using validation results

Rules:

- Keep arithmetic manageable.
- Use small datasets.
- Do not provide the final formula unless the point is not formula recall.
- Do not tell the student which failure mode is present if that is what they must identify.

## k-NN

Possible problem styles:

- Classify one query point using a given distance table or small coordinate dataset
- Compare results for different k values
- Show how scaling changes neighbor selection
- Apply weighted voting with given weights

Rules:

- Use at most 2D or 3D points.
- Keep distances simple or provide a distance table.
- Do not make the answer depend on ambiguous tie-breaking unless the tie rule is stated.

## Decision Trees

Possible problem styles:

- Compute impurity of a node
- Compute impurity after a candidate split
- Compare candidate splits
- Trace one level of tree construction
- Classify a test instance using a given tree

Rules:

- Use small tables.
- Use binary or low-cardinality categorical attributes.
- If entropy is used, provide required approximate log values only when arithmetic would otherwise dominate the question.
- Do not name the best split inside the question.

## Neural Networks / CNNs / RNNs

Possible problem styles:

- Perceptron output for given weights and input
- One small forward pass through a simple network
- Parameter count in a dense or convolutional layer
- CNN output-size calculation from input size, filter size, stride, and padding
- Identify what kind of sequence behavior a recurrent model is designed for
- Explain the role of gates in a recurrent architecture without revealing the exact gate names unless asked

Rules:

- Avoid large networks.
- Avoid long backpropagation derivations unless explicitly requested.
- Keep numeric forward passes short.
- For CNNs, state assumptions about padding and stride clearly.

## SVM

Possible problem styles:

- Identify support vectors from a small plotted/table dataset
- Interpret margin width qualitatively or with simple numeric values
- Explain the effect of changing a regularization parameter in a given scenario
- Decide whether a nonlinear feature mapping or kernel is needed for a described dataset
- Compare hard-margin and soft-margin behavior using a scenario

Rules:

- Do not make the question require advanced optimization derivations unless the formula is provided.
- Do not reveal the answer by saying which kernel is appropriate before asking the question.

## Ensembles / Random Forests / Boosting

Possible problem styles:

- Majority-vote prediction from several classifiers
- Bootstrap sample / out-of-bag reasoning
- Compare bagging and boosting in a scenario
- Trace one simple boosting-weight update if all required numbers are provided
- Explain why diversity among base models matters

Rules:

- Keep boosting calculations small.
- Use simple classifier outputs.
- Do not turn ensemble questions into pure definition recall only.

## Clustering / k-Means / GMM / EM

Possible problem styles:

- Run one or two iterations of k-means
- Assign points to nearest centroids
- Update centroids
- Use SSE or another criterion to compare clusterings
- Explain why a clustering result fails on non-convex or differently sized clusters
- Distinguish hard assignment from probabilistic assignment using a small example
- Trace E-step/M-step meaning without giving away both names in the question if recall is being tested

Rules:

- Use small 1D or 2D datasets.
- State initial centroids clearly.
- Avoid too many points.
- If testing EM numerically, provide enough intermediate values to keep the question reasonable.

## PCA / Dimensionality Reduction

Possible problem styles:

- Standardize a tiny dataset
- Compute or use a given covariance matrix
- Select a principal component from eigenvalues/eigenvectors
- Project points onto a given component
- Decide how many components are needed from an explained-variance table
- Compare feature selection and feature extraction in a scenario

Rules:

- Do not require heavy matrix algebra unless the necessary intermediate values are given.
- Use small matrices.
- For projection questions, provide eigenvectors or components explicitly.

## Bayesian Decision Theory / Association Rules / Reinforcement Learning

These topics should usually be lighter unless the lecturer emphasizes them later.

Possible problem styles:

- Compute posterior probabilities from given priors and likelihoods
- Choose an action from a small loss/risk table
- Decide whether a reject option is preferred from given costs
- Compute support/confidence/lift for a small transaction table
- Identify agent, state, action, reward, and policy in a simple RL scenario
- Choose an action in a small bandit setting from given value estimates

Rules:

- Keep these questions short.
- Do not let these small final topics dominate the exam.
- Avoid advanced derivations.

---

# 14. Formula and Data-Table Rule

For calculation questions:

- Avoid complex calculations and long computations.
- Include only essential, easy equations such as Gini impurity, precision, recall, F1 score, simple accuracy/error rate, simple entropy/information gain when values are manageable, support/confidence/lift, and very small projection or distance calculations.
- Do not include long gradient-descent derivations, heavy matrix algebra, long backpropagation calculations, difficult SVM optimization, or multi-step EM arithmetic unless all intermediate values are given and the arithmetic is minimal.
- Provide all raw data needed to solve the problem.
- Use tables instead of paragraphs for datasets.
- State rounding rules when decimals are expected.
- State tie-breaking rules when ties can happen.
- Keep numbers small enough for exam conditions.
- Do not include worked examples in the question.

For formulas:

- Do not provide a formula when the purpose is to test whether the student remembers it.
- Provide a formula only when the purpose is to test application rather than memorization.
- If a formula is provided, do not also explain which concept it corresponds to unless necessary.

---

# 15. Figure / Plot / Diagram Question Rule

The lecture notes contain many visual examples: decision boundaries, neural-network diagrams, CNN illustrations, SVM margins, clustering plots, PCA projections, and decision-tree diagrams.

Mock exams may include simplified text-based versions of these visuals.

Use:

- Small coordinate tables instead of complex plots
- Simple ASCII or Markdown diagrams only when helpful
- Clearly labeled axes or feature names
- Short model-output tables
- Small trees or network diagrams

Avoid:

- Requiring the student to infer too much from a low-quality image
- Copying a slide figure exactly
- Asking a question whose answer depends on visual guessing instead of reasoning
- Including an image that already visually marks the answer

---

# 16. Difficulty Calibration

A realistic CMPE442 mock final should be challenging but not unfair.

Recommended difficulty mix:

| Difficulty | Approximate Share | Description |
|---|---:|---|
| Easy | 20–25% | Direct concepts, basic terminology, simple T/F |
| Medium | 40–50% | Concept application, short calculations, scenario reasoning |
| Hard | 25–35% | Multi-step problems, algorithm tracing, subtle model behavior |

Do not make every T/F statement tricky. Do not make every problem computationally long. The challenge should come from understanding, interpretation, and application, not arithmetic overload. Calculations should be short and based only on essential formulas.

---

# 17. Recommended 100-Point Mock Final Template

Use this as the default template unless the user requests a different distribution.

| Section | Topic Coverage | Points |
|---|---|---:|
| A | 30 mixed True / False statements across all lecture-note blocks | 30 |
| B | 5 Multiple Choice questions on easily confused distinctions | 5 |
| C | 5 Fill-in-the-Blank questions on core terminology/formula components | 5 |
| D | 4–5 Short Answer / Classical questions on validation, model behavior, preprocessing, generalization, SVMs, ensembles, clustering, PCA, or RL | 20 |
| E1 | Regression/logistic/evaluation/model-selection easy calculation or reasoning | 8–10 |
| E2 | k-NN or decision-tree easy calculation/tracing | 8–10 |
| E3 | Neural network/CNN/SVM/ensemble conceptual tracing problem | 8–12 |
| E4 | Clustering/GMM/PCA/dimensionality-reduction tracing or interpretation problem | 10–14 |
| Optional inside E | Small Bayes/association/RL scenario if needed | 4–6 |
| **Total** |  | **100** |

The exact problem split can change, but the final point total must remain exactly 100.

---

# 18. Past-Style Elements to Preserve

The exam should imitate the observed midterm style while adapting it to CMPE442 and the final-exam warning.

Preserve:

- 30 True / False questions
- 100 total points
- A mix of objective, classical, fill-in, short-answer, and problem-solving questions
- Algorithm-tracing questions
- Easy calculation questions with small tables
- Direct but non-hinting wording
- Questions that require recall rather than recognition only

Adapt:

- Reduce the number of MCQ/test-style questions outside the T/F section.
- Increase classical short-answer weight and keep problem-solving weight high.
- Include later lecture topics strongly.
- Use ML-specific calculations and traces instead of general conceptual-only questions.

---

# 19. Quality Checklist Before Finalizing a Mock Exam

Before finalizing a generated CMPE442 mock final, verify:

- [ ] Total points add up to exactly 100.
- [ ] The T/F section contains exactly 30 statements unless explicitly changed.
- [ ] The T/F penalty rule is written clearly.
- [ ] The MCQ section is small.
- [ ] At least 40 points are problem solving or algorithm tracing, without complex computation.
- [ ] The exam covers the full lecture-note range.
- [ ] Later topics are represented strongly enough to satisfy the 65% post-midterm requirement.
- [ ] No question reveals the answer or gives unnecessary hints.
- [ ] Recall questions do not list the exact terms being asked for.
- [ ] Calculation questions include all necessary data and use only essential, easy equations.
- [ ] Tie-breaking and rounding rules are stated when needed.
- [ ] Tables are used where they improve readability.
- [ ] Sub-questions are not separate Markdown headings.
- [ ] No answer-key content is mixed into the exam body.
- [ ] The wording is clear and unambiguous.
- [ ] Questions are not copied directly from lecture slides.
- [ ] The mock exam resembles a realistic final, not a lecture summary.

---

# 20. Common Mistakes to Avoid

Avoid generating mock finals that:

- Add up to more or less than 100 points
- Replace the expected 30 T/F questions with a different structure
- Include too many MCQs after the T/F section
- Turn the final into a lecture summary
- Give formula explanations inside recall questions
- Tell the student which concept is being tested before asking the question
- Use huge datasets for hand calculations
- Require long matrix algebra, long gradient updates, heavy EM arithmetic, or complex SVM optimization
- Make all problems about early supervised-learning topics
- Ignore neural networks, SVMs, ensembles, clustering, GMM/EM, PCA, and dimensionality reduction
- Overweight very small late topics such as association rules or reinforcement learning
- Copy exact examples from the slides
- Include answer key material unless the user explicitly asks for it

---

# 21. Answer Key Rule

By default, generate only the mock exam.

If the user explicitly asks for an answer key:

- Put the answer key after the full exam.
- Clearly separate it from the exam.
- For T/F, list the answer only unless explanations are requested.
- For calculation problems, show intermediate steps.
- For algorithm tracing, show each required iteration or decision point.
- Do not place answers directly after each question unless specifically requested.

---

# 22. Final Instruction for Future CMPE442 Mock Finals

When generating future CMPE442 mock final exams, follow this priority order:

1. Match the lecturer’s stated final-exam style.
2. Keep the total exactly 100 points.
3. Include exactly 30 T/F questions with the midterm penalty rule.
4. Use 35% before-midterm topics and 65% after-midterm topics.
5. Reduce extra test-style questions outside T/F and add more classical short-answer questions.
6. Keep problem-solving and algorithm-tracing weight high, but avoid complex computations.
7. Cover the full lecture notes, with strong representation of later topics.
8. Do not reveal answers or give hints inside question wording.
9. Do not include topic names on the question titles. Bad example: "Question 5 — PCA and Bayesian Decision", Good Example: "Question 5" 
10. Use clean tables and readable Markdown formatting.
11. Keep calculations realistic for exam conditions and limited to essential formulas.
12. Avoid summaries, teaching sections, and copied slide examples.