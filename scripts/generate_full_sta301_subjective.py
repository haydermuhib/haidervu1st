#!/usr/bin/env python3
import json

with open('/home/haider/Desktop/Chores/sta301_subjective.json') as f:
    items = json.load(f)

# Complete solutions dictionary for all 79 subjective questions
solutions = {
    1: """**Step-by-Step Solution:**

**1. Probability Distribution of Annual Airplane Accidents ($X$):**
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
Taking the common denominator (LCM = 12):
$$\\text{Var}(X) = \\frac{86 - 75}{12} = \\frac{11}{12} \\approx 0.9167$$

**Final Answer:**
The variance of annual airplane accidents is **$\\frac{11}{12} \\approx 0.9167$** (Standard Deviation $\\sigma = \\sqrt{11/12} \\approx 0.9574$).""",

    2: """**Step-by-Step Solution:**

**1. Given Data:**
Observations: $X = \\{+3, -3, -4, -1, +1, +4\\}$, Sample size $n = 6$.

**2. Calculation of Arithmetic Mean ($\\bar{X}$):**
$$\\bar{X} = \\frac{\\sum X}{n} = \\frac{3 - 3 - 4 - 1 + 1 + 4}{6} = \\frac{0}{6} = 0$$

**3. Absolute Deviations Table from Mean $|X - \\bar{X}| = |X - 0| = |X|$:**
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
The mean deviation about the mean is **$\\frac{8}{3} \\approx 2.67$**.""",

    3: """**Answer:**

The **Coefficient of Variation (C.V.)** is a relative measure of dispersion defined as:
$$\\text{C.V.} = \\frac{S}{\\bar{X}} \\times 100\\%$$

**Why We Use C.V.:**
1. **Comparing Datasets with Different Units of Measurement:** Standard deviation depends on units of measurement (e.g. comparing height in cm with weight in kg). Because C.V. is expressed as a pure percentage (dimensionless), it allows direct comparison of variability between completely different variables.
2. **Comparing Datasets with Widely Different Means:** Even when two series have the same units, a standard deviation of 10 on a mean of 50 represents 20% variability, while a standard deviation of 10 on a mean of 1,000 represents only 1% variability. C.V. standardizes this comparison.
3. **Evaluating Consistency / Stability:** A lower C.V. indicates greater consistency, homogeneity, and reliability of the data, while a higher C.V. indicates greater dispersion and risk.""",

    4: """**Answer:**

**Definition of Permutation:**
A **permutation** is an ordered arrangement of all or part of a set of distinct objects where the order of arrangement is strictly important.

**General Permutation Rule:**
The number of permutations of $n$ distinct objects taken $r$ at a time is denoted by $^n P_r$ or $P(n, r)$ and given by:
$$^n P_r = \\frac{n!}{(n - r)!} \\quad (0 \\le r \\le n)$$
Where $n! = n \\times (n-1) \\times (n-2) \\times \\dots \\times 1$ and $0! = 1$.

**Special Cases:**
1. Arranging all $n$ objects: $^n P_n = \\frac{n!}{(n - n)!} = \\frac{n!}{0!} = n!$.
2. Permutations with repetition: When among $n$ objects, $n_1$ are alike of one kind, $n_2$ of a second kind, ..., $n_k$ of a $k$-th kind, the number of distinct permutations is:
$$P = \\frac{n!}{n_1! \\cdot n_2! \\cdot \\dots \\cdot n_k!}$$""",

    5: """**Step-by-Step Solution:**

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
The coefficient of variation is **$71.89\\%$** (or $0.7189$ in decimal ratio form).""",

    6: """**Step-by-Step Solution:**

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
- For drawing 3 balls (all white): **$P(3W) = \\frac{1}{455} \\approx 0.0022$**.""",

    7: """**Proof of De Morgan's First Law:**

**Given Sets:**
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
Hence, $(A \\cup B)' = (A' \\cap B')$ is **proved**.""",

    8: """**Answer:**

Measures of Central Tendency and Measures of Dispersion are complementary because neither alone can give a complete summary of a dataset:

1. **Central Tendency Identifies the Center:** Averages (Mean, Median, Mode) locate the central value or the typical observation around which data clusters.
2. **Dispersion Quantifies the Scatter:** Measures of dispersion (Variance, Standard Deviation, Range, Quartile Deviation) describe how widely the observations spread out or disperse from that center.
3. **Why One Without the Other Fails:** Two distinct datasets can have identical means (e.g. Data 1: $\\{50, 50, 50\\}$ and Data 2: $\\{0, 50, 100\\}$ both have Mean = 50), yet Data 1 has zero variation while Data 2 has substantial spread.
4. **Conclusion:** An average indicates *where* data concentrates, while dispersion reveals *how reliable and representative* that average is. Together, they fully describe the distribution's location and spread.""",

    9: """**Answer:**

**Definition:**
The **Subjective Approach to Probability** (also known as the personalistic or Bayesian perspective) defines probability as a measure of the degree of personal belief, confidence, or trust an individual assigns to the likelihood of an event occurring, based on available evidence, intuition, experience, or judgment.

**Key Characteristics:**
1. **Applicable to Non-Repeatable Events:** Unlike classical probability (which requires equally likely outcomes) and relative frequency (which requires repeatable experiments under identical conditions), subjective probability can evaluate unique historical or one-off scenarios (e.g., \"What is the probability that a new tech product captures 20% market share next year?\").
2. **Individual Dependence:** Different knowledgeable people can assign different subjective probabilities to the same event depending on their information and risk assessment.
3. **Axiomatic Consistency:** Subjective probabilities must still obey standard probability laws: $0 \\le P(A) \\le 1$, $P(S) = 1$, and $P(A \\cup B) = P(A) + P(B)$ for mutually exclusive events.""",

    10: """**Answer:**

| Feature | Absolute Dispersion | Relative Dispersion |
|:---|:---|:---|
| **Definition** | Measures the actual magnitude of variation in the dataset. | Measures the variability in proportion to an appropriate measure of central tendency. |
| **Units of Measurement** | Expressed in the **same units** as the original data (or squared units for variance). | **Unitless (pure number)**; expressed as a decimal ratio or percentage. |
| **Primary Formulae** | • Range: $X_m - X_0$<br>• Quartile Deviation: $\\frac{Q_3 - Q_1}{2}$<br>• Mean Deviation: $\\frac{\\sum |X - \\bar{X}|}{n}$<br>• Standard Deviation: $\\sqrt{\\frac{\\sum (X - \\bar{X})^2}{n}}$ | • Coefficient of Range: $\\frac{X_m - X_0}{X_m + X_0}$<br>• Coefficient of Q.D.: $\\frac{Q_3 - Q_1}{Q_3 + Q_1}$<br>• Coefficient of M.D.: $\\frac{\\text{M.D.}}{\\bar{X}}$<br>• Coefficient of Variation (C.V.): $\\frac{S}{\\bar{X}} \\times 100\\%$ |
| **Comparability** | Cannot be used to compare datasets having different units or vastly different means. | Specifically designed to compare variation across datasets with different units or different means. |""",

    11: """**Answer:**

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
- When events are both mutually exclusive and exhaustive, they partition the sample space ($P(A) + P(B) = 1$).""",

    12: """**Step-by-Step Solution:**

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
2. $P(\\text{Green}) = \\mathbf{\\frac{1}{2} = 0.5000}$""",

    13: """**Answer:**

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

**Conclusion:** Therefore, if $P(A|B) = P(B|A)$, the probabilities of both events $A$ and $B$ must be equal.""",

    14: """**Step-by-Step Solution:**

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
*(Alternatively, $P(A') \\cdot P(B') = (1 - 0.40)(1 - 0.30) = 0.60 \\times 0.70 = 0.42$).*""",

    15: """**Proof of De Morgan's Second Law:**

**Given Sets:**
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
Hence, $(A \\cap B)' = (A' \\cup B')$ is **proved**.""",

    16: """**Step-by-Step Solution:**

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
- Second moment about mean: $m_2 = \\mathbf{201}$""",

    17: """**Answer:**

The **Harmonic Mean (H.M.)** is defined as the reciprocal of the arithmetic mean of the reciprocals of the individual observations.

**Formula for Ungrouped Data:**
$$\\text{H.M.} = \\frac{n}{\\sum \\left(\\frac{1}{X}\\right)}$$
Alternatively written:
$$\\frac{1}{\\text{H.M.}} = \\frac{\\sum \\left(\\frac{1}{X}\\right)}{n}$$

**Formula for Grouped Data:**
$$\\text{H.M.} = \\frac{\\sum f}{\\sum \\left(\\frac{f}{X}\\right)}$$

**Core Usage:**
Harmonic mean is specifically designed to calculate the true average rate of speed, prices, and rates where the variable of interest is expressed in units per time or units per currency.""",

    18: """**Step-by-Step Solution:**

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
The word MATHEMATICS is **trimodal**, and its modes are **M, A, and T**.""",

    19: """**Answer:**

The middle value of an ordered array of numbers is the **Median** (denoted as $\\tilde{X}$ or $Q_2$).

**Key Characteristics:**
1. **Division into Equal Halves:** Exactly 50% of the observations lie below the median and 50% lie above it.
2. **Formula for Ungrouped Data:**
   - If $n$ is odd: $\\text{Median} = \\text{value of } \\left(\\frac{n+1}{2}\\right)^{\\text{th}} \\text{ observation}$.
   - If $n$ is even: $\\text{Median} = \\text{average of } \\left(\\frac{n}{2}\\right)^{\\text{th}} \\text{ and } \\left(\\frac{n}{2} + 1\\right)^{\\text{th}} \\text{ observations}$.
3. **Robustness:** Unlike the arithmetic mean, the median is resistant to extreme values (outliers) and is the preferred measure of central location for skewed distributions.""",

    20: """**Answer:**

The algebraic sum of deviations of a set of observations from their arithmetic mean is **always equal to ZERO**:
$$\\sum_{i=1}^n (X_i - \\bar{X}) = 0$$

**Mathematical Proof:**
$$\\sum_{i=1}^n (X_i - \\bar{X}) = \\sum_{i=1}^n X_i - \\sum_{i=1}^n \\bar{X}$$
Since $\\bar{X}$ is a constant, $\\sum_{i=1}^n \\bar{X} = n \\bar{X}$.
$$\\sum_{i=1}^n (X_i - \\bar{X}) = \\sum_{i=1}^n X_i - n \\left(\\frac{\\sum_{i=1}^n X_i}{n}\\right) = \\sum_{i=1}^n X_i - \\sum_{i=1}^n X_i = 0$$
This is one of the fundamental mathematical properties of the arithmetic mean.""",

    21: """**Answer:**

In a **Histogram**, the **Class Boundaries** (or class intervals) are plotted along the horizontal axis (**X-axis**), and the **Class Frequencies** (or frequency densities in case of unequal intervals) are plotted along the vertical axis (**Y-axis**).

In a **Cumulative Frequency Polygon (Ogive)**, the upper class boundaries are plotted along the X-axis against cumulative frequencies on the Y-axis.""",

    22: """**Answer:**

The arrangement of raw numerical data in order of magnitude (either in ascending order from lowest to highest, or descending order from highest to lowest) is called an **Array** (or **Ordered Array** / **Ordered Data**).

**Importance:**
Constructing an array is the necessary first step for computing order statistics such as the Median, Quartiles, Deciles, Percentiles, and the Range.""",

    23: """**Answer:**

The mode value from raw ungrouped data can be conveniently obtained with the help of a **Dot Plot** (or a frequency tally / stem-and-leaf plot).

**Explanation:**
On a dot plot, each observation is represented by a dot along a number line. Repeated identical values stack vertically; the column with the tallest stack of dots immediately reveals the most frequently occurring value—the **Mode**.""",

    24: """**Answer:**

In a **Symmetrical Distribution** (such as the **Normal Distribution** or Bell-Shaped Curve), the left-hand side of the distribution is the exact **mirror image** of the right-hand side across the vertical axis drawn at the center.

**Key Mathematical Properties:**
1. $\\text{Mean} = \\text{Median} = \\text{Mode}$.
2. Moment coefficient of skewness $\\beta_1 = 0$ ($m_3 = 0$).
3. Quartiles are equidistant from the median: $Q_3 - \\text{Median} = \\text{Median} - Q_1$.""",

    25: """**Step-by-Step Solution:**

**1. Frequency Count of Letters in 'T-O-M-A-T-O':**
- T: 2 times
- O: 2 times
- M: 1 time
- A: 1 time
- Total letters = 6

**2. Determine Mode:**
The letters **T** and **O** both appear with the highest frequency of 2.

**Final Answer:**
The word TOMATO is **bimodal**, with modes **T and O**.""",

    26: """**Answer:**

**Relationship Between Class Interval and Range:**
In the construction of a grouped frequency distribution, the **class interval size (width) $h$** is determined by dividing the **Range** by the desired number of classes $k$:
$$h = \\frac{\\text{Range}}{k} = \\frac{X_{\\max} - X_{\\min}}{k}$$

The number of classes $k$ is commonly estimated using **Sturges' Rule**:
$$k = 1 + 3.322 \\log_{10}(n)$$
Where $n$ is the total sample size.""",

    27: """**Answer:**

If all $n$ observations in a dataset are identical and equal to a positive constant $c$ (i.e. $X_1 = X_2 = \\dots = X_n = c$), then the **Harmonic Mean will be equal to $c$**:
$$\\text{H.M.} = \\frac{n}{\\sum_{i=1}^n \\frac{1}{c}} = \\frac{n}{n \\cdot \\frac{1}{c}} = c$$

Under this condition:
$$\\text{Arithmetic Mean} = \\text{Geometric Mean} = \\text{Harmonic Mean} = c$$

*(Note: If any observation in the dataset is zero, the Harmonic Mean cannot be computed because division by zero is undefined).*""",

    28: """**Answer:**

**Shape of Distribution Based on Averages:**
1. If $\\mathbf{\\text{Mean} = \\text{Median} = \\text{Mode}}$ (e.g. all equal to 5), the distribution is perfectly **Symmetrical** (Bell-shaped).
2. If $\\mathbf{\\text{Mean} < \\text{Median} < \\text{Mode}}$, the distribution is **Negatively Skewed** (skewed to the left, with a long left tail).
3. If $\\mathbf{\\text{Mean} > \\text{Median} > \\text{Mode}}$, the distribution is **Positively Skewed** (skewed to the right, with a long right tail).""",

    29: """**Answer:**

In the construction of a frequency distribution from raw continuous data, the very first step is to calculate the **Range**:
$$\\text{Range} = X_{\\max} - X_{\\min}$$

**Sequential Steps in Order:**
1. Calculate the **Range** (difference between maximum and minimum values).
2. Determine the **number of classes ($k$)** (using Sturges' Rule $k = 1 + 3.322 \\log_{10} n$).
3. Calculate the **class interval width ($h$)** ($h = \\text{Range}/k$).
4. Establish class limits and class boundaries.
5. Tally the frequencies for each class.""",

    30: """**Answer:**

**Difference Between Histogram and Historigram:**
1. **Histogram:** A graphical representation of a continuous frequency distribution consisting of adjacent vertical bars whose bases represent class boundaries and whose areas/heights are proportional to class frequencies.
2. **Historigram:** A graphical display of **time-series data** where time periods (years, months, days) are plotted on the horizontal axis and values of the variable under observation are plotted on the vertical axis, connected by straight line segments.
3. **Key Distinction:** A histogram depicts frequency distributions, whereas a historigram depicts chronological changes over time.""",

    31: """**Answer:**

When the data are **severely skewed** or contain extreme outlier values, the most appropriate and reliable measure of central tendency is the **Median**.

**Reasoning:**
The **Arithmetic Mean** is pulled heavily in the direction of the skewness (sensitive to extreme values), providing a distorted view of the center. The **Median**, being a positional average based on rank, remains unaffected by extreme outliers and reliably identifies the true 50% midpoint of the data.""",

    32: """**Answer:**

According to the **Empirical Rule** for a bell-shaped (Normal) distribution with mean $\\bar{X}$ and standard deviation $s$:
1. Approximately **$68.27\\%$** (about $68\\%$) of the measurements fall within **1 standard deviation** of the mean:
   $$(\\bar{X} - s, \\bar{X} + s)$$
2. Approximately **$95.45\\%$** (about $95\\%$) of the measurements fall within **2 standard deviations** of the mean:
   $$(\\bar{X} - 2s, \\bar{X} + 2s)$$
3. Approximately **$99.73\\%$** (about $99.7\\%$) of the measurements fall within **3 standard deviations** of the mean:
   $$(\\bar{X} - 3s, \\bar{X} + 3s)$$""",

    33: """**Answer:**

The number of times a particular observation or data value appears in a dataset is called the value's **Frequency** (or absolute frequency, denoted by $f$).

The proportion of times a value appears relative to the total number of observations is its **Relative Frequency** ($f / n$).""",

    34: """**Answer:**

Dividing the range of a variable by the number of classes gives the **Class Width** (also known as the **Class Interval size** or class length, denoted by $h$ or $c$):
$$h = \\frac{\\text{Range}}{\\text{Number of Classes } (k)} = \\frac{X_{\\max} - X_{\\min}}{k}$$""",

    35: """**Answer:**

A tabular summary of data showing categories or non-overlapping classes alongside the number of items (observations) belonging to each class is called a **Frequency Distribution** (or **Frequency Table**).""",

    36: """**Answer:**

**True Statements About the Median:**
1. **Middle Positional Value:** The median is the positional value that divides an ordered array into two equal parts such that exactly 50% of the data values are less than or equal to the median, and 50% are greater than or equal to it.
2. **Resistance to Outliers:** The median is robust and insensitive to extreme values, unlike the arithmetic mean.
3. **Applicability to Open-Ended Classes:** The median can be determined even when frequency distributions have open-ended classes (e.g. \"Below 10\" or \"60 and above\").
4. **Coincidence with Quantiles:** The median corresponds exactly to the 2nd Quartile ($Q_2$), the 5th Decile ($D_5$), and the 50th Percentile ($P_{50}$).""",

    37: """**Answer:**

In the case of **open-ended classes** (such as \"Less than 20\" or \"80 and above\"), it is impossible to compute the:
1. **Arithmetic Mean**
2. **Geometric Mean**
3. **Harmonic Mean**
4. **Variance and Standard Deviation**

**Reason:** All these measures require the class mark (midpoint $X$) of every class. Since open-ended classes lack an upper or lower boundary, their midpoints cannot be determined without arbitrary assumptions.
*(Note: Positional measures such as the **Median**, **Quartiles**, and **Mode** can still be computed).*""",

    38: """**Answer:**

**Grouping error** (the error introduced when individual raw data values are replaced by class midpoints) is less serious when:
1. The **class interval width ($h$) is small / narrow**, resulting in a larger number of finely spaced classes.
2. The observations within each class are **uniformly distributed** or symmetrically clustered around the class midpoint.
3. Total sample size $n$ is large, allowing individual positive and negative errors to cancel out.""",

    39: """**Answer:**

Exactly **half of the observations ($50\\%$)** in an ordered dataset are always larger than the **Median** (as well as the **Second Quartile $Q_2$** and the **50th Percentile $P_{50}$**).""",

    40: """**Answer:**

A frequency curve that has a long tail extending toward higher values (to the right) is called a **Positively Skewed Curve** (or **Right-Skewed Distribution**).

**Characteristics:**
- $\\text{Mean} > \\text{Median} > \\text{Mode}$
- Third central moment $m_3 > 0$
- Coefficient of skewness is positive.""",

    41: """**Answer:**

In a **Histogram**, the bases of the adjacent rectangles are marked off by the **Class Boundaries** along the horizontal axis (**X-axis**).""",

    42: """**Answer:**

The statistical graphical display that splits each data observation into two parts is the **Stem-and-Leaf Display** (or Stem-and-Leaf Plot, introduced by John Tukey in 1977).

**Structure:**
- **Stem:** Contains the leading digit(s) representing the broader class.
- **Leaf:** Contains the trailing single digit representing the specific value.""",

    43: """**Answer:**

The **Arithmetic Mean** (often simply called the mean, $\\bar{X}$) is obtained by summing all the individual observations in the dataset and dividing that total sum by the number of observations:
$$\\bar{X} = \\frac{\\sum_{i=1}^n X_i}{n}$$
For grouped frequency data:
$$\\bar{X} = \\frac{\\sum f X}{\\sum f}$$""",

    44: """**Answer:**

An extremely positively skewed frequency curve (where frequency starts at a maximum and drops off sharply, or vice versa) is commonly known as a **J-shaped curve** (or **reverse J-shaped curve** / exponential distribution curve).""",

    45: """**Answer:**

**Importance of Venn Diagrams in Probability and Statistics:**
1. **Visualizing Set Relationships:** Provides an intuitive geometric representation of sets, subsets, disjoint sets, and overlapping events within a universal sample space $S$.
2. **Simplifying Complex Probabilities:** Makes it easy to visualize compound events such as unions ($A \\cup B$), intersections ($A \\cap B$), and complements ($A'$).
3. **Proving Probability Laws:** Graphically demonstrates key algebraic laws, including De Morgan's laws ($(A \\cup B)' = A' \\cap B'$) and the General Addition Theorem ($P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$).
4. **Error Prevention:** Prevents double-counting of overlapping outcomes in joint probability problems.""",

    46: """**Answer:**

The **75th Percentile ($P_{75}$)** and the **Third Quartile ($Q_3$)** are **mathematically identical**:
$$P_{75} \\equiv Q_3$$

**Explanation:**
- By definition, the third quartile $Q_3$ cuts off the lowest $75\\%$ of the data.
- The 75th percentile $P_{75}$ is the value below which $75\\%$ of the observations lie.
- Therefore, both measures represent the exact same value in any dataset.""",

    47: """**Answer:**

The **Geometric Mean** gives equal weightage to **equal proportional changes**, **relative rates of change**, and **ratios / percentages**, rather than absolute differences.

**Core Applications:**
It is the mathematically correct average for calculating average annual growth rates of populations, sales growth, compound interest, index numbers, and inflation rates.""",

    48: """**Answer:**

In a **Cumulative Frequency Curve (Ogive)**:
- **Upper Class Boundaries** are plotted along the horizontal axis (**X-axis**).
- **Cumulative Frequencies** are plotted along the vertical axis (**Y-axis**).
Points are connected with a smooth curve or line segments.""",

    49: """**Answer:**

**Rules and Guidelines for Constructing a Stem-and-Leaf Display:**
1. **Splitting the Digits:** Each raw observation is split into two parts: a **Stem** (leading digit or digits) and a **Leaf** (the final trailing single digit).
2. **Stem Column:** Stems are listed in a vertical column from smallest to largest with a vertical line drawn to their right.
3. **Leaf Listing:** Each leaf is written in the row corresponding to its stem in ascending order without commas.
4. **Single-Digit Leaves:** Each leaf must consist of only a single digit (0 through 9).
5. **Advantage:** Unlike a histogram, a stem-and-leaf display retains the original raw values of the data while displaying the shape of the distribution.""",

    50: """**Answer:**

**Relationship Among the Averages (A.M., G.M., H.M.):**
For any set of positive observations:
$$\\mathbf{\\text{Arithmetic Mean} \\ge \\text{Geometric Mean} \\ge \\text{Harmonic Mean}}$$
$$\\text{A.M.} \\ge \\text{G.M.} \\ge \\text{H.M.}$$

**Special Properties:**
1. **Equality Condition:** The three averages are strictly equal ($\\text{A.M.} = \\text{G.M.} = \\text{H.M.}$) if and only if all the observations in the dataset are identical.
2. **Two Positive Numbers:** For any two positive values $a$ and $b$:
   $$\\text{G.M.}^2 = \\text{A.M.} \\times \\text{H.M.} \\iff \\text{G.M.} = \\sqrt{\\text{A.M.} \\times \\text{H.M.}}$$""",

    51: """**Answer:**

In a **Symmetrical Distribution** (such as the **Normal Distribution**), the left side of the distribution curve is the exact **mirror image** of the right-hand side.

**Consequences:**
- Skewness is zero ($m_3 = 0, \\beta_1 = 0$).
- $\\text{Mean} = \\text{Median} = \\text{Mode}$.
- Area to the left of the mean is exactly $0.50$, and area to the right is $0.50$.""",

    52: """**Answer:**

The formula for the **Mid-Range** (a rough measure of central tendency) is:
$$\\text{Mid-Range} = \\frac{X_{\\min} + X_{\\max}}{2} = \\frac{X_0 + X_m}{2}$$
Where:
- $X_0$ or $X_{\\min}$ is the lowest (minimum) observation.
- $X_m$ or $X_{\\max}$ is the highest (maximum) observation.""",

    53: """**Answer:**

Cumulative frequency is presented graphically by an **Ogive** (also known as a **Cumulative Frequency Polygon** or Cumulative Frequency Curve).

**Types:**
1. **Less-than Ogive:** Plots upper class boundaries vs. less-than cumulative frequencies (curves upward to the right).
2. **More-than Ogive:** Plots lower class boundaries vs. more-than cumulative frequencies (curves downward to the right).
3. The intersection point of both curves corresponds to the **Median** on the X-axis.""",

    54: """**Answer:**

In the case of an **open-ended class** (e.g. \"Less than 10\" or \"50 and above\"):
- **Cannot be Computed:** The **Arithmetic Mean**, **Geometric Mean**, **Harmonic Mean**, **Variance**, and **Standard Deviation** cannot be calculated because the midpoint of open-ended intervals cannot be determined.
- **Can be Computed:** The **Median**, **Quartiles**, **Deciles**, **Percentiles**, and **Mode** can still be computed accurately, provided the median/mode does not fall within the open-ended class itself.""",

    55: """**Answer:**

**Essential Steps in the Construction of a Frequency Distribution:**
1. **Find the Range:** Compute $\\text{Range} = X_{\\max} - X_{\\min}$.
2. **Decide the Number of Classes ($k$):** Usually between 5 and 20, or via Sturges' Rule: $k = 1 + 3.322 \\log_{10} n$.
3. **Determine Class Interval Size ($h$):** Divide the range by the number of classes: $h = \\text{Range} / k$ (round up to a convenient unit).
4. **Establish Class Limits and Class Boundaries:** Start with a lower limit slightly below or equal to the minimum value $X_{\\min}$.
5. **Tally Raw Data:** Count the number of observations falling into each class interval to determine the class frequencies ($f$).
6. **Verify:** Ensure $\\sum f = n$.""",

    56: """**Answer:**

**Determining Distribution Shape from Summary Statistics:**
- If **$\\text{Mean} = \\text{Median} = \\text{Mode}$**, the distribution is **Symmetrical**.
- If **$\\text{Mean} < \\text{Median} < \\text{Mode}$**, the distribution is **Negatively Skewed** (left tail is elongated).
- If **$\\text{Mean} > \\text{Median} > \\text{Mode}$**, the distribution is **Positively Skewed** (right tail is elongated).
- In a symmetrical distribution, the coefficient of skewness equals 0.""",

    57: """**Answer:**

**Frequency Polygon:**
A **Frequency Polygon** is a line graph of a frequency distribution formed by plotting the class frequencies against the class midpoints (class marks), connecting adjacent plotted points with straight line segments, and closing the polygon by extending lines to the horizontal axis at the midpoints of hypothetical classes with zero frequency on both ends.""",

    58: """**Answer:**

In a **Symmetrical Distribution**, both the **Median** and the **Mode** are equal to the **Mean**:
$$\\mathbf{\\text{Mean} = \\text{Median} = \\text{Mode}}$$

Furthermore, the first moment about the mean $m_1 = 0$ and the third moment about the mean $m_3 = 0$.""",

    59: """**Answer:**

The formula for the **Mid-Quartile Range** (also known as the **Mid-Quartile**) is:
$$\\text{Mid-Quartile} = \\frac{Q_1 + Q_3}{2}$$

*(Distinction Note: Do not confuse with **Quartile Deviation** / Semi-Interquartile Range, which is $\\text{Q.D.} = \\frac{Q_3 - Q_1}{2}$, or **Interquartile Range**, which is $\\text{IQR} = Q_3 - Q_1$).*""",

    60: """**Answer:**

The **free-hand frequency curve** is a smooth, continuous limiting curve obtained by smoothing out the jagged steps of a frequency polygon or histogram.

**Statistical Interpretation:**
It represents the theoretical continuous probability density function of the population from which the sample was drawn, representing the limit as the sample size $n \\to \\infty$ and the class width $h \\to 0$.""",

    61: """**Answer:**

A line graph connecting the midpoints of adjacent histogram bars that touches the horizontal axis (X-axis) at both ends at zero-frequency class midpoints is a **Frequency Polygon**.""",

    62: """**Answer:**

The **Harmonic Mean** is the reciprocal of the arithmetic mean of the reciprocals of the data values:
$$\\text{H.M.} = \\frac{n}{\\sum_{i=1}^n \\left(\\frac{1}{X_i}\\right)}$$""",

    63: """**Step-by-Step Analysis:**

**Given:**
- Mean $\\bar{X} = 150.00$
- Median $\\tilde{X} = 151.00$
- Mode $= 152.80$

**Evaluation:**
Comparing the values:
$$150.00 < 151.00 < 152.80 \\implies \\mathbf{\\text{Mean} < \\text{Median} < \\text{Mode}}$$

**Conclusion:**
Whenever the Mean is smaller than the Median, and the Median is smaller than the Mode, the distribution is **Negatively Skewed** (skewed to the left, with an extended tail toward the lower values).""",

    64: """**Answer:**

**Formal Definition of Statistics:**
**Statistics** is defined as the mathematical science that deals with the collection, organization, presentation, analysis, and interpretation of numerical data to make valid decisions and inferences in the face of uncertainty.

**Two Main Branches:**
1. **Descriptive Statistics:** Techniques used to summarize, organize, and simplify data (tables, charts, averages, measures of dispersion).
2. **Inferential Statistics:** Techniques that use sample data to draw conclusions, estimate parameters, and test hypotheses about an entire population.""",

    65: """**Answer:**

**Five-Number Summary:**
A **Five-Number Summary** is a set of five descriptive summary statistics that provides a concise overview of the center, spread, and shape of a dataset:
1. **Minimum Value ($X_0$ or $X_{\\min}$):** The smallest observation in the data.
2. **First Quartile ($Q_1$):** The 25th percentile; 25% of data falls below it.
3. **Median ($Q_2$ or $\\tilde{X}$):** The 50th percentile; 50% of data falls below it.
4. **Third Quartile ($Q_3$):** The 75th percentile; 75% of data falls below it.
5. **Maximum Value ($X_m$ or $X_{\\max}$):** The largest observation in the data.

**Application:**
The five-number summary forms the foundation for drawing a **Box-and-Whisker Plot**.""",

    66: """**Answer:**

**Why Venn Diagrams are Important:**
1. **Visual Clarification:** They provide a visual, geometric depiction of sets and events as regions within a bounding rectangle representing the universal set (sample space $S$).
2. **Understanding Relationships:** They intuitively illustrate concepts of intersection ($A \\cap B$), union ($A \\cup B$), complement ($A'$), and mutually exclusive subsets ($A \\cap B = \\emptyset$).
3. **Verifying Theorems:** They serve as intuitive proofs for set algebra laws, including De Morgan's Laws and distributive properties.
4. **Solving Probability Problems:** They provide a clear visual tool to prevent double-counting when applying the addition theorem: $P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$.""",

    67: """**Answer:**

**Definition of Probability (Classical / Laplace Definition):**
Formulated by Pierre-Simon Laplace, if a random experiment can result in $n$ mutually exclusive and equally likely outcomes, and if $m$ of these outcomes are favorable to an event $A$, then the probability of event $A$ is:
$$P(A) = \\frac{m}{n} = \\frac{\\text{Number of favorable outcomes}}{\\text{Total number of possible outcomes}}$$

**Axioms of Probability:**
1. $0 \\le P(A) \\le 1$ for any event $A$.
2. $P(S) = 1$ for the certain event.
3. $P(A \\cup B) = P(A) + P(B)$ if $A$ and $B$ are mutually exclusive.""",

    68: """**Answer:**

**Definition of Geometric Mean:**
The **Geometric Mean ($G$)** of a set of $n$ positive numbers $X_1, X_2, \\dots, X_n$ is defined as the positive $n$-th root of their product:
$$G = \\sqrt[n]{X_1 \\cdot X_2 \\dots X_n} = (X_1 \\cdot X_2 \\dots X_n)^{1/n}$$

**Logarithmic Form for Computation:**
$$\\log G = \\frac{\\sum \\log X}{n} \\implies G = \\text{antilog}\\left(\\frac{\\sum \\log X}{n}\\right)$$
For grouped data:
$$G = \\text{antilog}\\left(\\frac{\\sum f \\log X}{\\sum f}\\right)$$

**Limitation:** If any observation is zero or negative, the Geometric Mean cannot be calculated.""",

    69: """**Answer:**

**Difference Between Nominal and Ordinal Scales:**

| Basis | Nominal Scale | Ordinal Scale |
|:---|:---|:---|
| **Definition** | Data categorized into mutually exclusive qualitative categories with no natural ranking. | Data categorized into distinct classes that have a natural order or rank. |
| **Mathematical Property** | Only equality ($=$ or $\\ne$) is meaningful. | Relative order ($<$, $>$, $=$) is meaningful. |
| **Permissible Operations** | Counting / Frequency, Mode. | Median, Percentiles, Rank Correlation. |
| **Examples** | Gender (Male/Female), Blood Group (A, B, AB, O), Religion, Eye Color, Nationality. | Student Letter Grades (A, B, C, D), Military Ranks, Socioeconomic Status (Low, Middle, High), Likert Survey Scales. |""",

    70: """**Answer:**

**Four Levels / Scales of Measurement with Classification Examples:**

1. **Nominal Scale (Categorical, No Order):**
   - *Examples:* Gender, Marital Status, City of Birth, Postal Zip Code, Religion, Car Make.
2. **Ordinal Scale (Ranked / Ordered Categories):**
   - *Examples:* Performance Rating (Poor, Fair, Good, Excellent), Educational Qualification (Matric, Inter, BS, MS), Pain Level Scale (1 to 10), Customer Satisfaction.
3. **Interval Scale (Ordered, Meaningful Differences, Arbitrary Zero):**
   - *Examples:* Temperature in Celsius or Fahrenheit (0°C does not mean absence of temperature), IQ Scores, Calendar Years.
4. **Ratio Scale (Ordered, Equal Intervals, True Absolute Zero):**
   - *Examples:* Height, Weight, Monthly Income, Age, Distance traveled, Reaction time.""",

    71: """**Answer:**

**Discrete vs. Continuous Variables:**

1. **Discrete Variable:** A quantitative variable that can take only distinct, separated, countable values (typically integers), with no intermediate values possible.
   - *Examples:*
     1. Number of children in a household.
     2. Number of airplane accidents in a year.
     3. Number of cars passing a toll booth per hour.
     4. Number of typographical errors on a page.
     5. Number of heads obtained when tossing 3 coins.

2. **Continuous Variable:** A quantitative variable that can take on any real value within a given continuous interval or continuum (obtained through measurement).
   - *Examples:*
     1. Weight of an adult (e.g. 68.45 kg).
     2. Height of a student (e.g. 172.5 cm).
     3. Ambient temperature (e.g. 24.8°C).
     4. Time taken to complete a test (e.g. 45.2 minutes).
     5. Volume of milk produced by a cow per day.""",

    72: """**Answer:**

**Relationship Between 75th Percentile and Third Quartile:**
The **75th Percentile ($P_{75}$)** and the **Third Quartile ($Q_3$)** represent the **exact same statistical value**:
$$P_{75} = Q_3$$

**Explanation:**
- Quartiles divide an ordered dataset into four equal parts: $Q_1$ (25%), $Q_2$ (50%), and $Q_3$ (75%).
- Percentiles divide an ordered dataset into 100 equal parts.
- Therefore, $Q_3$ leaves exactly $75\\%$ of the observations below it and $25\\%$ above it, which is the precise definition of the 75th percentile ($P_{75}$).""",

    73: """**Answer:**

**Definition of a Negatively Skewed Curve:**
A frequency curve is said to be **negatively skewed** (or **skewed to the left**) when the left tail of the distribution is longer and fatter than the right tail.

**Key Characteristics:**
1. **Order of Averages:** $\\mathbf{\\text{Mean} < \\text{Median} < \\text{Mode}}$.
2. **Moments:** The third central moment is negative ($m_3 < 0$), and Karl Pearson's coefficient of skewness is negative ($S_k < 0$).
3. **Quartile Separation:** The distance from the first quartile to the median is greater than the distance from the median to the third quartile:
   $$(Q_2 - Q_1) > (Q_3 - Q_2)$$""",

    74: """**Answer:**

**Primary Data vs. Secondary Data:**

1. **Primary Data:** Data collected for the first time by an investigator or agency directly from original sources for a specific intended purpose.
   - *Examples:*
     - A survey conducted by a university student using a questionnaire.
     - Direct observations and experimental measurements in a chemistry laboratory.
     - Data collected by the Census Bureau during a nationwide population census.

2. **Secondary Data:** Data that have already been collected, compiled, and published by someone else and are re-used by a secondary investigator.
   - *Examples:*
     - Economic figures extracted from the State Bank of Pakistan's annual report.
     - Weather records obtained from the Meteorological Department's website.
     - Historical sales data referenced from a published industry journal.""",

    75: """**Answer:**

**Disadvantages of Range as a Measure of Dispersion:**
1. **Ignores Intermediate Data:** Range is computed solely from the two extreme values ($X_{\\max} - X_{\\min}$); it completely ignores the distribution and values of all intermediate data points.
2. **Highly Sensitive to Outliers:** A single unusually large or small outlier can artificially inflate the range drastically.
3. **Cannot be Computed for Open-Ended Distributions:** If a frequency distribution has open-ended classes (e.g. \"Under 10\" or \"Over 100\"), the range cannot be calculated.
4. **Instability Across Samples:** Range fluctuates widely from sample to sample, making it a statistically inefficient and unstable estimator for population spread.""",

    76: """**Answer:**

**Empirical Rule Limits and Percentages:**
For a bell-shaped (Normal) distribution with mean $\\bar{X}$ and standard deviation $s$:

1. **Limits $(\\bar{X} \\pm 1s)$:**
   Approximately **$68.27\\%$** of the measurements fall within the interval $(\\bar{X} - s, \\bar{X} + s)$.
2. **Limits $(\\bar{X} \\pm 2s)$:**
   Approximately **$95.45\\%$** of the measurements fall within the interval $(\\bar{X} - 2s, \\bar{X} + 2s)$.
3. **Limits $(\\bar{X} \\pm 3s)$:**
   Approximately **$99.73\\%$** of the measurements fall within the interval $(\\bar{X} - 3s, \\bar{X} + 3s)$ (virtually all observations).""",

    77: """**Answer:**

**Quantitative vs. Qualitative Variables:**

| Attribute | Quantitative Variable | Qualitative Variable (Attribute) |
|:---|:---|:---|
| **Definition** | A variable that is naturally numerical and measurable in terms of numbers. | A variable that represents categories, characteristics, or attributes without numerical measurement. |
| **Subtypes** | • Discrete (countable integer values)<br>• Continuous (measurable continuous values) | • Nominal (unordered categories)<br>• Ordinal (ordered/ranked categories) |
| **Statistical Calculations** | Arithmetic Mean, Variance, Standard Deviation, Correlation. | Frequencies, Percentages, Proportions, Mode. |
| **Examples** | Salary, Height, Age, Weight, Number of children, Test scores. | Marital Status, Eye Color, Gender, Religion, Academic Grade (A, B, C). |""",

    78: """**Answer:**

**Definition of a Multiple Bar Chart:**
A **multiple bar chart** (also called a grouped or compound bar chart) is a graphical tool used to display two or more related categorical data sets simultaneously.

**Structure & Application:**
- Two or more adjacent vertical or horizontal bars are drawn side-by-side for each category.
- Different colors, shadings, or hatch patterns are used to distinguish the component series, accompanied by a legend.
- It enables direct visual comparison both between different categories and across the sub-variables within each category (e.g. comparing imports and exports across multiple consecutive years).""",

    79: """**Answer:**

**Definition and Properties of Negative Skewness:**
**Negative skewness** (or left-skewness) describes an asymmetric frequency distribution in which the tail on the left side of the distribution is longer or fatter than the tail on the right side.

**Core Properties:**
1. **Inequality of Averages:** $\\mathbf{\\text{Mean} < \\text{Median} < \\text{Mode}}$.
2. **Central Tendency Relationship:** The bulk of observations cluster toward the higher end of the scale (on the right), while a few extreme small values pull the arithmetic mean to the left.
3. **Skewness Coefficients:**
   - Karl Pearson's coefficient: $S_k = \\frac{\\text{Mean} - \\text{Mode}}{s} < 0$.
   - Bowley's coefficient: $S_b = \\frac{Q_3 - 2Q_2 + Q_1}{Q_3 - Q_1} < 0$.
   - Moment coefficient: $b_1 = \\frac{m_3^2}{m_2^3}$, where $m_3 < 0$."""
}

# Update all items
count_updated = 0
for item in items:
    qid = item["id"]
    if qid in solutions:
        item["answer"] = solutions[qid]
        count_updated += 1

with open('/home/haider/Desktop/Chores/sta301_subjective.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, indent=2, ensure_ascii=False)

print(f"Successfully updated all {count_updated} subjective questions in sta301_subjective.json!")
