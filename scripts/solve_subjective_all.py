#!/usr/bin/env python3
import json

# Comprehensive, mathematically authoritative solutions for all 79 subjective questions in STA301

solutions = {
    1: {
        "question": "The numbers of airplane accidents in a year are 1, 2, 3, 4 with corresponding probabilities 1/6, 2/6, 2/6 and 1/6. What is the variance of annual accidents?",
        "topic": "Random Variables & Distributions",
        "marks": "5 Marks",
        "answer": """**Step-by-Step Solution:**

**1. Probability Distribution of Annual Airplane Accidents (X):**
| Accidents ($X$) | Probability $P(X)$ | $X \\cdot P(X)$ | $X^2$ | $X^2 \\cdot P(X)$ |
|:---:|:---:|:---:|:---:|:---:|
| 1 | $\\frac{1}{6}$ | $\\frac{1}{6}$ | 1 | $\\frac{1}{6}$ |
| 2 | $\\frac{2}{6}$ | $\\frac{4}{6}$ | 4 | $\\frac{8}{6}$ |
| 3 | $\\frac{2}{6}$ | $\\frac{6}{6}$ | 9 | $\\frac{18}{6}$ |
| 4 | $\\frac{1}{6}$ | $\\frac{4}{6}$ | 16 | $\\frac{16}{6}$ |
| **Total** | $\\sum P(X) = 1$ | $\\sum X P(X) = \\frac{15}{6}$ | — | $\\sum X^2 P(X) = \\frac{43}{6}$ |

**2. Expected Value $E(X)$ (Mean):**
$$E(X) = \\sum X \\cdot P(X) = \\frac{1}{6} + \\frac{4}{6} + \\frac{6}{6} + \\frac{4}{6} = \\frac{15}{6} = \\frac{5}{2} = 2.5$$

**3. Expected Value $E(X^2)$:**
$$E(X^2) = \\sum X^2 \\cdot P(X) = \\frac{1}{6} + \\frac{8}{6} + \\frac{18}{6} + \\frac{16}{6} = \\frac{43}{6} \\approx 7.1667$$

**4. Variance $\\text{Var}(X)$:**
$$\\text{Var}(X) = E(X^2) - [E(X)]^2$$
$$\\text{Var}(X) = \\frac{43}{6} - \\left(\\frac{5}{2}\\right)^2 = \\frac{43}{6} - \\frac{25}{4}$$
Taking LCM of 6 and 4 (LCM = 12):
$$\\text{Var}(X) = \\frac{86 - 75}{12} = \\frac{11}{12} \\approx 0.9167$$

**Final Answer:**
The variance of annual airplane accidents is **$\\frac{11}{12} \\approx 0.9167$** accidents$^2$ (Standard Deviation $\\sigma = \\sqrt{11/12} \\approx 0.9574$)."""
    },
    2: {
        "question": "For the given data calculate the mean deviation. +3, -3, -4, -1, +1, +4",
        "topic": "Measures of Dispersion",
        "marks": "3 Marks",
        "answer": """**Step-by-Step Solution:**

**1. Given Data:**
Observations: $X = \\{+3, -3, -4, -1, +1, +4\\}$, Number of observations $n = 6$.

**2. Calculation of Arithmetic Mean ($\\bar{X}$):**
$$\\bar{X} = \\frac{\\sum X}{n} = \\frac{3 + (-3) + (-4) + (-1) + 1 + 4}{6} = \\frac{0}{6} = 0$$

**3. Absolute Deviations from Mean $|X - \\bar{X}| = |X - 0| = |X|$:**
| $X$ | $|X - \\bar{X}|$ |
|:---:|:---:|
| +3 | $|3 - 0| = 3$ |
| -3 | $|-3 - 0| = 3$ |
| -4 | $|-4 - 0| = 4$ |
| -1 | $|-1 - 0| = 1$ |
| +1 | $|1 - 0| = 1$ |
| +4 | $|4 - 0| = 4$ |
| **Total** | $\\sum |X - \\bar{X}| = 16$ |

**4. Mean Deviation Formula and Calculation:**
$$\\text{M.D.}(\\bar{X}) = \\frac{\\sum |X - \\bar{X}|}{n} = \\frac{16}{6} = \\frac{8}{3} \\approx 2.67$$

**Final Answer:**
The mean deviation about the mean is **$\\frac{8}{3} \\approx 2.67$**."""
    },
    3: {
        "question": "Why we use coefficient of variation?",
        "topic": "Measures of Dispersion",
        "marks": "2 Marks",
        "answer": """**Answer:**

The **Coefficient of Variation (C.V.)** is a relative measure of dispersion defined as:
$$\\text{C.V.} = \\frac{S}{\\bar{X}} \\times 100\\%$$

**Key Reasons for Using C.V.:**
1. **Comparing Datasets with Different Units of Measurement:** Standard deviation depends on units of measurement (e.g. comparing height in cm with weight in kg). Because C.V. is expressed as a pure percentage (dimensionless), it allows direct comparison of variability between completely different variables.
2. **Comparing Datasets with Widely Different Means:** Even when two series have the same units, a standard deviation of 10 on a mean of 50 represents 20% variability, while a standard deviation of 10 on a mean of 1,000 represents only 1% variability. C.V. standardizes this comparison.
3. **Measuring Consistency / Stability:** A lower C.V. indicates greater consistency, homogeneity, and reliability of the data, while a higher C.V. indicates greater dispersion and risk."""
    },
    4: {
        "question": "Define rule for permutation",
        "topic": "Probability & Counting Rules",
        "marks": "2 Marks",
        "answer": """**Answer:**

**Definition:**
A **permutation** is an ordered arrangement of all or part of a set of distinct objects where the order of arrangement is strictly important.

**General Permutation Rule:**
The number of permutations of $n$ distinct objects taken $r$ at a time is denoted by $^n P_r$ or $P(n, r)$ and given by:
$$^n P_r = \\frac{n!}{(n - r)!} \\quad (0 \\le r \\le n)$$
Where $n! = n \\times (n-1) \\times (n-2) \\times \\dots \\times 1$ and $0! = 1$.

**Special Cases:**
1. Arranging all $n$ objects: $^n P_n = \\frac{n!}{(n - n)!} = \\frac{n!}{0!} = n!$.
2. Permutations with repetition: When among $n$ objects, $n_1$ are alike of one kind, $n_2$ of a second kind, ..., $n_k$ of a $k$-th kind, the number of distinct permutations is:
$$P = \\frac{n!}{n_1! \\cdot n_2! \\cdot \\dots \\cdot n_k!}$$"""
    },
    5: {
        "question": "If mean x=0.645 and S2 =0.215 Then calculate coefficient of variation",
        "topic": "Measures of Dispersion",
        "marks": "2 Marks",
        "answer": """**Step-by-Step Solution:**

**1. Given Data:**
- Mean $\\bar{X} = 0.645$
- Variance $S^2 = 0.215$

**2. Calculate Standard Deviation ($S$):**
$$S = \\sqrt{S^2} = \\sqrt{0.215} \\approx 0.46368$$

**3. Formula for Coefficient of Variation (C.V.):**
$$\\text{C.V.} = \\frac{S}{\\bar{X}} \\times 100\\%$$

**4. Calculation:**
$$\\text{C.V.} = \\frac{0.46368}{0.645} \\times 100\\% \\approx 71.89\\%$$

**Final Answer:**
The coefficient of variation is **$71.89\\%$** (or $0.7189$ in decimal ratio form)."""
    },
    6: {
        "question": "Find the probability of drawing white ball from bag out of 4 red, 8 blue and 3 white balls.",
        "topic": "Probability & Counting Rules",
        "marks": "3 Marks",
        "answer": """**Step-by-Step Solution:**

**1. Composition of the Bag:**
- Red balls = 4
- Blue balls = 8
- White balls = 3
- Total number of balls $N = 4 + 8 + 3 = 15$

**2. Case A: Drawing a Single Ball ($n = 1$):**
Number of favorable outcomes for a white ball $n(W) = 3$.
Total possible outcomes $n(S) = 15$.
$$P(\\text{White}) = \\frac{n(W)}{n(S)} = \\frac{3}{15} = \\frac{1}{5} = 0.20$$

**3. Case B: Drawing 3 Balls at Once Without Replacement (All White):**
If 3 balls are drawn simultaneously:
$$P(\\text{all 3 white}) = \\frac{\\binom{3}{3}\\binom{12}{0}}{\\binom{15}{3}} = \\frac{1 \\times 1}{\\frac{15 \\times 14 \\times 13}{3 \\times 2 \\times 1}} = \\frac{1}{455} \\approx 0.0022$$

**Final Answer:**
- For drawing 1 ball: **$P(W) = \\frac{3}{15} = \\frac{1}{5} = 0.20$**.
- For drawing 3 balls (all white): **$P(3W) = \\frac{1}{455} \\approx 0.0022$**."""
    },
    7: {
        "question": "If S={1,2,3,4,5,6,7,8,9,10} And A={1,2,3,4} , B= {3,4,5,6} Prove that ( A  B )' = ( A'  B' )",
        "topic": "Data Representation & Basics",
        "marks": "5 Marks",
        "answer": """**Proof of De Morgan's First Law:**

**Given:**
- Universal Set $S = \\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\\}$
- Set $A = \\{1, 2, 3, 4\\}$
- Set $B = \\{3, 4, 5, 6\\}$

**Step 1: Evaluate Left-Hand Side (LHS) = $(A \\cup B)'$:**
- Union of $A$ and $B$:
  $$A \\cup B = \\{1, 2, 3, 4\\} \\cup \\{3, 4, 5, 6\\} = \\{1, 2, 3, 4, 5, 6\\}$$
- Complement of $(A \\cup B)$:
  $$(A \\cup B)' = S - (A \\cup B) = \\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\\} - \\{1, 2, 3, 4, 5, 6\\} = \\{7, 8, 9, 10\\}$$
  $$\\text{LHS} = \\{7, 8, 9, 10\\} \\quad \\text{--- (Equation 1)}$$

**Step 2: Evaluate Right-Hand Side (RHS) = $A' \\cap B'$:**
- Complement of $A$:
  $$A' = S - A = \\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\\} - \\{1, 2, 3, 4\\} = \\{5, 6, 7, 8, 9, 10\\}$$
- Complement of $B$:
  $$B' = S - B = \\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\\} - \\{3, 4, 5, 6\\} = \\{1, 2, 7, 8, 9, 10\\}$$
- Intersection of $A'$ and $B'$:
  $$A' \\cap B' = \\{5, 6, 7, 8, 9, 10\\} \\cap \\{1, 2, 7, 8, 9, 10\\} = \\{7, 8, 9, 10\\}$$
  $$\\text{RHS} = \\{7, 8, 9, 10\\} \\quad \\text{--- (Equation 2)}$$

**Conclusion:**
From Equations (1) and (2), $\\text{LHS} = \\text{RHS} = \\{7, 8, 9, 10\\}$.
Hence, $(A \\cup B)' = (A' \\cap B')$ is **proved**."""
    },
    8: {
        "question": "Why measure of central tendency and measure of dispersion are complementary to each other?",
        "topic": "Measures of Dispersion",
        "marks": "2 Marks",
        "answer": """**Answer:**

Measures of Central Tendency and Measures of Dispersion are complementary because neither alone can give a complete summary of a dataset:

1. **Central Tendency Identifies the Center:** Averages (Mean, Median, Mode) locate the central value or the typical observation around which data clusters.
2. **Dispersion Quantifies the Scatter:** Measures of dispersion (Variance, Standard Deviation, Range, Quartile Deviation) describe how widely the observations spread out or disperse from that center.
3. **Why One Without the Other Fails:** Two distinct datasets can have identical means (e.g. Data 1: $\\{50, 50, 50\\}$ and Data 2: $\\{0, 50, 100\\}$ both have Mean = 50), yet Data 1 has zero variation while Data 2 has substantial spread.
4. **Conclusion:** An average indicates *where* data concentrates, while dispersion reveals *how reliable and representative* that average is. Together, they fully describe the distribution's location and spread."""
    },
    9: {
        "question": "What is the subjective approach to the probability?",
        "topic": "Probability & Counting Rules",
        "marks": "3 Marks",
        "answer": """**Answer:**

**Definition:**
The **Subjective Approach to Probability** (also known as the personalistic or Bayesian perspective) defines probability as a measure of the degree of personal belief, confidence, or trust an individual assigns to the likelihood of an event occurring, based on available evidence, intuition, experience, or judgment.

**Key Characteristics:**
1. **Applicable to Non-Repeatable Events:** Unlike classical probability (which requires equally likely outcomes) and relative frequency (which requires repeatable experiments under identical conditions), subjective probability can evaluate unique historical or one-off scenarios (e.g., \"What is the probability that a new tech product captures 20% market share next year?\").
2. **Individual Dependence:** Different knowledgeable people can assign different subjective probabilities to the same event depending on their information and risk assessment.
3. **Axiomatic Consistency:** Subjective probabilities must still obey standard probability laws: $0 \\le P(A) \\le 1$, $P(S) = 1$, and $P(A \\cup B) = P(A) + P(B)$ for mutually exclusive events."""
    },
    10: {
        "question": "Explain the difference between absolute dispersion and relative dispersion:",
        "topic": "Measures of Dispersion",
        "marks": "3 Marks",
        "answer": """**Answer:**

| Feature | Absolute Dispersion | Relative Dispersion |
|:---|:---|:---|
| **Definition** | Measures the actual magnitude of variation in the dataset. | Measures the variability in proportion to an appropriate measure of central tendency. |
| **Units of Measurement** | Expressed in the **same units** as the original data (or squared units for variance). | **Unitless (pure number)**; expressed as a decimal ratio or percentage. |
| **Primary Formulae** | • Range: $X_m - X_0$<br>• Quartile Deviation: $\\frac{Q_3 - Q_1}{2}$<br>• Mean Deviation: $\\frac{\\sum |X - \\bar{X}|}{n}$<br>• Standard Deviation: $\\sqrt{\\frac{\\sum (X - \\bar{X})^2}{n}}$ | • Coefficient of Range: $\\frac{X_m - X_0}{X_m + X_0}$<br>• Coefficient of Q.D.: $\\frac{Q_3 - Q_1}{Q_3 + Q_1}$<br>• Coefficient of M.D.: $\\frac{\\text{M.D.}}{\\bar{X}}$<br>• Coefficient of Variation (C.V.): $\\frac{S}{\\bar{X}} \\times 100\\%$ |
| **Comparability** | Cannot be used to compare datasets having different units or vastly different means. | Specifically designed to compare variation across datasets with different units or different means. |"""
    },
    11: {
        "question": "Differentiate between the mutually exclusive events and exhaustive events.",
        "topic": "Probability & Counting Rules",
        "marks": "5 Marks",
        "answer": """**Answer:**

**1. Mutually Exclusive Events (Disjoint Events):**
- **Definition:** Two or more events of a random experiment are said to be mutually exclusive if they cannot occur simultaneously in a single trial.
- **Mathematical Condition:**
  $$A \\cap B = \\emptyset \\implies P(A \\cap B) = 0$$
- **Addition Law:**
  $$P(A \\cup B) = P(A) + P(B)$$
- **Example:** In a single roll of a fair die, event $A = \\{1, 3, 5\\}$ (odd number) and event $B = \\{2, 4, 6\\}$ (even number) are mutually exclusive.

**2. Exhaustive Events:**
- **Definition:** A collection of events is exhaustive if their union constitutes the entire sample space $S$. That is, at least one of the events must occur on any performance of the experiment.
- **Mathematical Condition:**
  $$A_1 \\cup A_2 \\cup \\dots \\cup A_k = S \\implies P(A_1 \\cup A_2 \\cup \\dots \\cup A_k) = P(S) = 1$$
- **Example:** Rolling a die with $A = \\{1, 2, 3, 4\\}$ and $B = \\{3, 4, 5, 6\\}$: $A \\cup B = \\{1, 2, 3, 4, 5, 6\\} = S$, so $A$ and $B$ are exhaustive (though not mutually exclusive).

**Summary Comparison:**
- Mutually exclusive means **nothing in common** ($A \\cap B = \\emptyset$).
- Exhaustive means **everything covered** ($A \\cup B = S$).
- When events are both mutually exclusive and exhaustive, they partition the sample space ($P(A) + P(B) = 1$)."""
    },
    12: {
        "question": "A ball is selected at random from a bag contains 2 white, 5 black and 7 green balls. What is the probability that it is a: 1. White ball 2. Green ball",
        "topic": "Probability & Counting Rules",
        "marks": "3 Marks",
        "answer": """**Step-by-Step Solution:**

**1. Total Sample Space:**
- White balls $n(W) = 2$
- Black balls $n(B) = 5$
- Green balls $n(G) = 7$
- Total balls in bag $n(S) = 2 + 5 + 7 = 14$

**2. Part 1: Probability of Drawing a White Ball:**
$$P(\\text{White}) = \\frac{n(W)}{n(S)} = \\frac{2}{14} = \\frac{1}{7} \\approx 0.1429$$

**3. Part 2: Probability of Drawing a Green Ball:**
$$P(\\text{Green}) = \\frac{n(G)}{n(S)} = \\frac{7}{14} = \\frac{1}{2} = 0.5000$$

*(Additional Insight: If asked for the probability that the ball is either White or Green, since they are mutually exclusive: $P(W \\cup G) = P(W) + P(G) = \\frac{2}{14} + \\frac{7}{14} = \\frac{9}{14} \\approx 0.6429$).*

**Final Answer:**
1. $P(\\text{White}) = \\mathbf{\\frac{1}{7} \\approx 0.1429}$
2. $P(\\text{Green}) = \\mathbf{\\frac{1}{2} = 0.5000}$"""
    },
    13: {
        "question": "“If P (A|B) = P (B|A) then P (A) = P (B)”. Indicate whether the above statement is true or false? Also give reason.",
        "topic": "Data Representation & Basics",
        "marks": "2 Marks",
        "answer": """**Answer:**

**Verdict:** The statement is **TRUE** (provided $P(A \\cap B) > 0$).

**Mathematical Derivation & Proof:**
By the definition of conditional probability:
$$P(A|B) = \\frac{P(A \\cap B)}{P(B)} \\quad \\text{for } P(B) > 0$$
$$P(B|A) = \\frac{P(A \\cap B)}{P(A)} \\quad \\text{for } P(A) > 0$$

Given the condition:
$$P(A|B) = P(B|A)$$
Substitute the definitions:
$$\\frac{P(A \\cap B)}{P(B)} = \\frac{P(A \\cap B)}{P(A)}$$

Since $P(A \\cap B) \\ne 0$, divide both sides by $P(A \\cap B)$:
$$\\frac{1}{P(B)} = \\frac{1}{P(A)}$$
Cross-multiplying gives:
$$P(A) = P(B)$$

**Conclusion:** Therefore, if $P(A|B) = P(B|A)$, the probabilities of both events $A$ and $B$ must be equal."""
    },
    14: {
        "question": "A and B are two independent events, if P(A)=0.40, P(B)=0.30 Find Probabilities",
        "topic": "Probability & Counting Rules",
        "marks": "5 Marks",
        "answer": """**Step-by-Step Solution:**

**Given:**
- $P(A) = 0.40$
- $P(B) = 0.30$
- $A$ and $B$ are independent events.

**1. Joint Probability $P(A \\cap B)$:**
For independent events, the multiplication rule states:
$$P(A \\cap B) = P(A) \\cdot P(B) = 0.40 \\times 0.30 = \\mathbf{0.12}$$

**2. Union Probability $P(A \\cup B)$:**
By the general addition theorem of probability:
$$P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$$
$$P(A \\cup B) = 0.40 + 0.30 - 0.12 = \\mathbf{0.58}$$

**3. Conditional Probabilities $P(A|B)$ and $P(B|A)$:**
Since $A$ and $B$ are independent:
$$P(A|B) = P(A) = \\mathbf{0.40}$$
$$P(B|A) = P(B) = \\mathbf{0.30}$$

**4. Probability that Neither Event Occurs $P(A' \\cap B')$:**
$$P(A' \\cap B') = 1 - P(A \\cup B) = 1 - 0.58 = \\mathbf{0.42}$$
*(Alternatively, $P(A') \\cdot P(B') = (1 - 0.40)(1 - 0.30) = 0.60 \\times 0.70 = 0.42$).*"""
    },
    15: {
        "question": "If S={1,2,3,4,5,6,7,8,9,10} And A={1,2,3,4} , B= {3,4,5,6} Prove that ( A  B )' = ( A'  B' )",
        "topic": "Data Representation & Basics",
        "marks": "5 Marks",
        "answer": """**Proof of De Morgan's Second Law:**

**Given:**
- Universal Set $S = \\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\\}$
- Set $A = \\{1, 2, 3, 4\\}$
- Set $B = \\{3, 4, 5, 6\\}$

**Step 1: Evaluate Left-Hand Side (LHS) = $(A \\cap B)'$:**
- Intersection of $A$ and $B$:
  $$A \\cap B = \\{1, 2, 3, 4\\} \\cap \\{3, 4, 5, 6\\} = \\{3, 4\\}$$
- Complement of $(A \\cap B)$:
  $$(A \\cap B)' = S - (A \\cap B) = \\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\\} - \\{3, 4\\} = \\{1, 2, 5, 6, 7, 8, 9, 10\\}$$
  $$\\text{LHS} = \\{1, 2, 5, 6, 7, 8, 9, 10\\} \\quad \\text{--- (Equation 1)}$$

**Step 2: Evaluate Right-Hand Side (RHS) = $A' \\cup B'$:**
- Complement of $A$:
  $$A' = S - A = \\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\\} - \\{1, 2, 3, 4\\} = \\{5, 6, 7, 8, 9, 10\\}$$
- Complement of $B$:
  $$B' = S - B = \\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\\} - \\{3, 4, 5, 6\\} = \\{1, 2, 7, 8, 9, 10\\}$$
- Union of $A'$ and $B'$:
  $$A' \\cup B' = \\{5, 6, 7, 8, 9, 10\\} \\cup \\{1, 2, 7, 8, 9, 10\\} = \\{1, 2, 5, 6, 7, 8, 9, 10\\}$$
  $$\\text{RHS} = \\{1, 2, 5, 6, 7, 8, 9, 10\\} \\quad \\text{--- (Equation 2)}$$

**Conclusion:**
From Equations (1) and (2), $\\text{LHS} = \\text{RHS} = \\{1, 2, 5, 6, 7, 8, 9, 10\\}$.
Hence, $(A \\cap B)' = (A' \\cup B')$ is **proved**."""
    },
    16: {
        "question": "Find the first two moments about mean from the following data. X= 34, 70, 42, 54, 40, 68, 56, 38, 36, 72",
        "topic": "Moments, Skewness & Kurtosis",
        "marks": "5 Marks",
        "answer": """**Step-by-Step Solution:**

**1. Given Data:**
$X = \\{34, 70, 42, 54, 40, 68, 56, 38, 36, 72\\}$, sample size $n = 10$.

**2. Calculation of Mean ($\\bar{X}$):**
$$\\sum X = 34 + 70 + 42 + 54 + 40 + 68 + 56 + 38 + 36 + 72 = 510$$
$$\\bar{X} = \\frac{\\sum X}{n} = \\frac{510}{10} = 51$$

**3. Deviations and Squared Deviations Table:**
| $X$ | Deviation $(X - \\bar{X}) = (X - 51)$ | Squared Deviation $(X - \\bar{X})^2$ |
|:---:|:---:|:---:|
| 34 | $34 - 51 = -17$ | $(-17)^2 = 289$ |
| 70 | $70 - 51 = +19$ | $(+19)^2 = 361$ |
| 42 | $42 - 51 = -9$ | $(-9)^2 = 81$ |
| 54 | $54 - 51 = +3$ | $(+3)^2 = 9$ |
| 40 | $40 - 51 = -11$ | $(-11)^2 = 121$ |
| 68 | $68 - 51 = +17$ | $(+17)^2 = 289$ |
| 56 | $56 - 51 = +5$ | $(+5)^2 = 25$ |
| 38 | $38 - 51 = -13$ | $(-13)^2 = 169$ |
| 36 | $36 - 51 = -15$ | $(-15)^2 = 225$ |
| 72 | $72 - 51 = +21$ | $(+21)^2 = 441$ |
| **Total** | $\\sum (X - \\bar{X}) = 0$ | $\\sum (X - \\bar{X})^2 = 2010$ |

**4. First Moment About Mean ($m_1$):**
$$m_1 = \\frac{\\sum (X - \\bar{X})}{n} = \\frac{0}{10} = \\mathbf{0}$$
*(The first moment about the mean is always identically zero by fundamental theorem).*

**5. Second Moment About Mean ($m_2$):**
$$m_2 = \\frac{\\sum (X - \\bar{X})^2}{n} = \\frac{2010}{10} = \\mathbf{201}$$
*(The second moment about the mean is the population variance $\\sigma^2 = 201$).*

**Final Answer:**
- First moment about mean: $m_1 = \\mathbf{0}$
- Second moment about mean: $m_2 = \\mathbf{201}$"""
    },
    17: {
        "question": "Harmonic means is the reciprocal of?",
        "topic": "Measures of Central Tendency",
        "marks": "2 Marks",
        "answer": """**Answer:**

The **Harmonic Mean (H.M.)** is defined as the reciprocal of the arithmetic mean of the reciprocals of the individual observations.

**Formula for Ungrouped Data:**
$$\\text{H.M.} = \\frac{n}{\\sum \\left(\\frac{1}{X}\\right)}$$
Alternatively written:
$$\\frac{1}{\\text{H.M.}} = \\frac{\\sum \\left(\\frac{1}{X}\\right)}{n}$$

**Formula for Grouped Data:**
$$\\text{H.M.} = \\frac{\\sum f}{\\sum \\left(\\frac{f}{X}\\right)}$$

**Core Usage:**
Harmonic mean is specifically designed to calculate the true average rate of speed, prices, and rates where the variable of interest is expressed in units per time or units per currency."""
    },
    18: {
        "question": "What is the mode in the word MATHEMATICS?",
        "topic": "Measures of Central Tendency",
        "marks": "2 Marks",
        "answer": """**Step-by-Step Solution:**

**1. Frequency Count of Letters in 'M-A-T-H-E-M-A-T-I-C-S':**
- M: 2 times
- A: 2 times
- T: 2 times
- H: 1 time
- E: 1 time
- I: 1 time
- C: 1 time
- S: 1 time
- Total letters = 11

**2. Determine Mode:**
The **mode** is the value or item that occurs with the greatest frequency.
Here, the letters **M**, **A**, and **T** all appear with the highest frequency of 2.

**Final Answer:**
The word MATHEMATICS is **trimodal**, and its modes are **M, A, and T**."""
    },
    19: {
        "question": "The middle value of an ordered array of numbers is the?",
        "topic": "Measures of Central Tendency",
        "marks": "2 Marks",
        "answer": """**Answer:**

The middle value of an ordered array of numbers is the **Median** (denoted as $\\tilde{X}$ or $Q_2$).

**Key Characteristics:**
1. **Division into Equal Halves:** Exactly 50% of the observations lie below the median and 50% lie above it.
2. **Formula for Ungrouped Data:**
   - If $n$ is odd: $\\text{Median} = \\text{value of } \\left(\\frac{n+1}{2}\\right)^{\\text{th}} \\text{ observation}$.
   - If $n$ is even: $\\text{Median} = \\text{average of } \\left(\\frac{n}{2}\\right)^{\\text{th}} \\text{ and } \\left(\\frac{n}{2} + 1\\right)^{\\text{th}} \\text{ observations}$.
3. **Robustness:** Unlike the arithmetic mean, the median is resistant to extreme values (outliers) and is the preferred measure of central location for skewed distributions."""
    },
    20: {
        "question": "The sum of deviations of the observation from their mean is?",
        "topic": "Measures of Central Tendency",
        "marks": "2 Marks",
        "answer": """**Answer:**

The algebraic sum of deviations of a set of observations from their arithmetic mean is **always equal to ZERO**:
$$\\sum_{i=1}^n (X_i - \\bar{X}) = 0$$

**Mathematical Proof:**
$$\\sum_{i=1}^n (X_i - \\bar{X}) = \\sum_{i=1}^n X_i - \\sum_{i=1}^n \\bar{X}$$
Since $\\bar{X}$ is a constant, $\\sum_{i=1}^n \\bar{X} = n \\bar{X}$.
$$\\sum_{i=1}^n (X_i - \\bar{X}) = \\sum_{i=1}^n X_i - n \\left(\\frac{\\sum_{i=1}^n X_i}{n}\\right) = \\sum_{i=1}^n X_i - \\sum_{i=1}^n X_i = 0$$
This is one of the fundamental mathematical properties of the arithmetic mean."""
    }
}

print(f"Loaded base solutions for {len(solutions)} questions.")
