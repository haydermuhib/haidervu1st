#!/usr/bin/env python3
"""
MTH202 Subjective Questions Audit and Mathematical Repair Script
Senior Subject Matter Expert Auditor for MTH202 (Discrete Mathematics)
"""

import json, re

with open("mth202_subjective.json", "r", encoding="utf-8") as f:
    subj = json.load(f)

print(f"Loaded {len(subj)} subjective questions.")

# Authoritative, complete mathematical definitions, explanations, derivations, and proofs
SUBJ_CORRECTIONS = {
    1: {
        "question": "What does it mean by the preservation of edge endpoint function in the definition of isomorphism of graphs?",
        "answer": (
            "Preservation of Edge Endpoint Function in Graph Isomorphism:\n\n"
            "1. Formal Definition:\n"
            "Let G = (V, E) and G' = (V', E') be two graphs with edge endpoint functions γ: E → {{u, v} | u, v ∈ V} and γ': E' → {{u', v'} | u', v' ∈ V'}.\n"
            "An isomorphism between G and G' consists of two bijective functions:\n"
            "  - A vertex bijection f: V → V'\n"
            "  - An edge bijection g: E → E'\n"
            "such that the edge endpoint function is preserved.\n\n"
            "2. Mathematical Meaning of Preservation:\n"
            "Preservation of the edge endpoint function means that for every edge e ∈ E, if e connects vertices u and v in G (i.e., γ(e) = {u, v}), then the corresponding edge g(e) in G' must connect f(u) and f(v) in G' (i.e., γ'(g(e)) = {f(u), f(v)}).\n\n"
            "3. Significance:\n"
            "This condition guarantees that the structural adjacency and edge connectivity are strictly preserved: two vertices are connected by an edge in G if and only if their images under f are connected by the corresponding edge in G'."
        ),
        "topic": "Graphs & Trees"
    },
    2: {
        "question": "Is there any method of identifying whether given graphs are isomorphic or not without explicitly finding the two bijection functions?",
        "answer": (
            "Determining Graph Isomorphism Without Explicit Bijections (Using Isomorphic Invariants):\n\n"
            "1. The Isomorphism Invariant Approach:\n"
            "While proving that two graphs ARE isomorphic ultimately requires demonstrating an isomorphism (or bijective mapping), we can definitively prove that two graphs are NOT isomorphic by checking 'isomorphic invariants'—properties that must be identical in any pair of isomorphic graphs.\n\n"
            "2. Necessary Conditions (Isomorphic Invariants):\n"
            "If G and G' are isomorphic, they must have:\n"
            "  a. The same number of vertices: |V(G)| = |V(G')|.\n"
            "  b. The same number of edges: |E(G)| = |E(G')|.\n"
            "  c. The same degree sequence: The sorted list of vertex degrees must be identical.\n"
            "  d. The same number of connected components.\n"
            "  e. The same number of cycles of each specific length k (e.g., triangles, 4-cycles).\n"
            "  f. The same adjacency matrix spectrum (eigenvalues).\n\n"
            "3. Decision Criterion:\n"
            "  - If ANY of these invariants differ between G and G', then G and G' are NOT isomorphic.\n"
            "  - However, if all these invariants match, the graphs might still not be isomorphic. To prove isomorphism positively, one must exhibit the bijection f: V(G) → V(G') that preserves adjacency."
        ),
        "topic": "Graphs & Trees"
    },
    3: {
        "question": "What are Complementary Graphs?",
        "answer": (
            "Complementary Graphs (Graph Complement):\n\n"
            "1. Formal Definition:\n"
            "Let G = (V, E) be a simple undirected graph. The complement of G, denoted by G' or Ḡ (G-bar), is a simple graph whose vertex set is identical to V, but whose edge set E(Ḡ) consists of all edges that are NOT present in G.\n\n"
            "2. Set Formulation:\n"
            "E(Ḡ) = { {u, v} | u, v ∈ V, u ≠ v and {u, v} ∉ E(G) } = E(K_n) \\ E(G),\n"
            "where K_n is the complete graph on n = |V| vertices.\n\n"
            "3. Key Properties:\n"
            "  - |E(G)| + |E(Ḡ)| = n(n - 1) / 2 = |E(K_n)|.\n"
            "  - Two vertices u and v are adjacent in Ḡ if and only if they are not adjacent in G.\n"
            "  - The complement of the complement is the original graph: (Ḡ)̄ = G.\n"
            "  - A self-complementary graph is isomorphic to its own complement (e.g., C_5, the 5-cycle)."
        ),
        "topic": "Graphs & Trees"
    },
    4: {
        "question": "What is the application of graph isomorphism in the real world?",
        "answer": (
            "Real-World Applications of Graph Isomorphism:\n\n"
            "1. Chemistry and Cheminformatics (Chemical Compound Identification):\n"
            "Chemical molecules are naturally represented as chemical graphs (atoms as vertices, covalent bonds as edges). Graph isomorphism algorithms are used to query chemical databases (e.g., PubChem) to determine if a newly synthesized molecule is structurally identical to an existing known chemical compound.\n\n"
            "2. Electronic Circuit Design and VLSI Testing:\n"
            "Integrated circuits and PCB layouts are represented as graphs of components and wire traces. Verification tools check whether an implemented physical layout correctly matches the original schematic graph specification using graph isomorphism.\n\n"
            "3. Computer Vision and Pattern Recognition:\n"
            "In object recognition, 2D/3D shapes are segmented into skeletal feature graphs. Matching a detected object against a database of known models involves finding subgraph or graph isomorphisms.\n\n"
            "4. Social Network Analysis:\n"
            "Identifying structurally identical network topologies or anonymous social structures across different communication platforms."
        ),
        "topic": "Graphs & Trees"
    },
    5: {
        "question": "Are isomorphic graphs reflexive, symmetric, and transitive (Is graph isomorphism an equivalence relation)?",
        "answer": (
            "Graph Isomorphism as an Equivalence Relation:\n\n"
            "Yes, graph isomorphism is an equivalence relation on the set of all graphs because it satisfies reflexivity, symmetry, and transitivity:\n\n"
            "1. Reflexive:\n"
            "Every graph G is isomorphic to itself (G ≅ G). The identity mapping id_V: V → V defined by id_V(v) = v and id_E(e) = e is a trivial isomorphism that preserves adjacency.\n\n"
            "2. Symmetric:\n"
            "If G_1 ≅ G_2, then G_2 ≅ G_1. If f: V(G_1) → V(G_2) is an isomorphism, its inverse function f^(-1): V(G_2) → V(G_1) is also a bijection that preserves edge endpoints and non-adjacency.\n\n"
            "3. Transitive:\n"
            "If G_1 ≅ G_2 and G_2 ≅ G_3, then G_1 ≅ G_3. If f: V(G_1) → V(G_2) and g: V(G_2) → V(G_3) are isomorphisms, their composition (g ∘ f): V(G_1) → V(G_3) is a bijection that preserves all adjacencies.\n\n"
            "Conclusion: Since isomorphism satisfies reflexivity, symmetry, and transitivity, it is a valid Equivalence Relation, partitioning the set of graphs into disjoint isomorphism classes."
        ),
        "topic": "Graphs & Trees"
    },
    29: {
        "question": "What is the difference between a Proper Subset, an Improper Subset, and a Power Set?",
        "answer": (
            "Proper Subset, Improper Subset, and Power Set:\n\n"
            "1. Subset (A ⊆ B):\n"
            "A set A is a subset of B if every element of A is also an element of B:\n"
            "∀x (x ∈ A → x ∈ B).\n\n"
            "2. Proper Subset (A ⊂ B):\n"
            "A is a proper subset of B if A is a subset of B and A is not equal to B (there exists at least one element in B that is not in A):\n"
            "A ⊆ B and A ≠ B.\n"
            "Example: If B = {1, 2, 3}, then A = {1, 2} is a proper subset of B.\n\n"
            "3. Improper Subset:\n"
            "A subset A of B that is equal to B itself is called an improper subset of B. Every non-empty set has exactly one improper subset: the set itself.\n\n"
            "4. Power Set (P(A)):\n"
            "The power set of a set A, denoted P(A), is the set of all subsets of A:\n"
            "P(A) = { S | S ⊆ A }.\n"
            "If |A| = n, then the cardinality of the power set is |P(A)| = 2^n.\n"
            "Example: If A = {a, b}, P(A) = { ∅, {a}, {b}, {a, b} }, and |P(A)| = 2^2 = 4."
        ),
        "topic": "Set Theory"
    },
    90: {
        "question": "There are 25 people who work in an office together. Four of these people are selected to attend four different conferences (the first to New York, the second to Chicago, the third to San Francisco, and the fourth to Miami). How many such selections are possible? Compare this to selecting an unassigned committee of four.",
        "answer": (
            "Combinatorics Problem: Distinct Conference Assignment vs. Committee Selection\n\n"
            "1. Four Different Conferences (Ordered Selection / Permutation):\n"
            "Because each selected individual is assigned to a specific, distinct city/conference (New York, Chicago, San Francisco, Miami), order matters.\n"
            "Number of ways = P(25, 4) = 25 × 24 × 23 × 22 = 303,600 ways.\n\n"
            "2. Unassigned Committee (Unordered Selection / Combination):\n"
            "If four people are selected simply to form a committee where all members have identical status and order does not matter:\n"
            "Number of ways = C(25, 4) = 25! / (4! × 21!) = (25 × 24 × 23 × 22) / (4 × 3 × 2 × 1) = 12,650 ways.\n\n"
            "3. Examination Conclusion:\n"
            "For distinct conferences, the mathematically rigorous answer is 303,600. When past paper keys note 12,650, they assumed an unordered committee of 4."
        ),
        "topic": "Discrete Mathematics"
    },
    91: {
        "question": "Prove that every integer is a rational number.",
        "answer": (
            "Theorem: Every integer is a rational number.\n\n"
            "1. Formal Definition of a Rational Number:\n"
            "A real number r is rational if and only if it can be expressed in the form r = a / b, where a and b are integers and b ≠ 0.\n\n"
            "2. Mathematical Proof:\n"
            "Let n be any arbitrary integer (n ∈ Z).\n"
            "We can express n as:\n"
            "  n = n / 1.\n"
            "Here:\n"
            "  - The numerator a = n is an integer because n ∈ Z.\n"
            "  - The denominator b = 1 is an integer and b ≠ 0.\n"
            "Thus, n satisfies the definition of a rational number.\n\n"
            "3. Conclusion:\n"
            "Since n was an arbitrary integer, every integer is a rational number: Z ⊆ Q."
        ),
        "topic": "Discrete Mathematics"
    },
    92: {
        "question": "Draw or describe a graph with six vertices and five edges that is NOT a tree.",
        "answer": (
            "Constructing a Graph with 6 Vertices and 5 Edges that is NOT a Tree:\n\n"
            "1. Theoretical Foundation:\n"
            "A graph with n vertices is a tree if and only if it is CONNECTED and has exactly n - 1 edges (or equivalently, connected and acyclic).\n"
            "For n = 6 vertices, a connected acyclic graph must have 6 - 1 = 5 edges.\n"
            "Therefore, for a graph with 6 vertices and 5 edges to NOT be a tree, it must fail one of the tree axioms: it must be DISCONNECTED (which forces it to contain a cycle).\n\n"
            "2. Explicit Construction:\n"
            "Let V = {v1, v2, v3, v4, v5, v6} (6 vertices).\n"
            "Define the 5 edges as:\n"
            "  - A 3-cycle (triangle): {v1, v2}, {v2, v3}, {v3, v1} (3 edges).\n"
            "  - A path extending from v3: {v3, v4}, {v4, v5} (2 edges).\n"
            "  - Vertex v6 has no incident edges (isolated vertex, degree 0).\n"
            "Total vertices |V| = 6.\n"
            "Total edges |E| = 3 + 2 = 5 edges.\n\n"
            "3. Verification:\n"
            "This graph is disconnected (v6 cannot be reached from v1) and contains a cycle (v1-v2-v3-v1). Hence, it is NOT a tree."
        ),
        "topic": "Graphs & Trees"
    },
    95: {
        "question": "Identify and define a digital logic circuit with two input signals and one output signal.",
        "answer": (
            "Digital Logic Gates with Two Inputs and One Output:\n\n"
            "1. Primary Types:\n"
            "A digital logic circuit that accepts two binary input signals (A, B ∈ {0, 1}) and produces a single binary output (Y ∈ {0, 1}) is a binary logic gate. The fundamental types are:\n"
            "  a. AND Gate: Y = A · B (Output is 1 if and only if both inputs are 1).\n"
            "  b. OR Gate: Y = A + B (Output is 1 if at least one input is 1).\n"
            "  c. NAND Gate: Y = ~(A · B) (Universal gate; inverted AND).\n"
            "  d. NOR Gate: Y = ~(A + B) (Universal gate; inverted OR).\n"
            "  e. XOR Gate: Y = A ⊕ B (Output is 1 when inputs are different).\n\n"
            "2. Contrast with Inverter (NOT Gate):\n"
            "A NOT gate is a unary operation accepting only 1 input signal and yielding 1 output signal. Therefore, a circuit with two inputs cannot be a NOT gate."
        ),
        "topic": "Boolean Algebra & Circuits"
    },
    96: {
        "question": "If f(x) = x + 1 and g(x) = 2x^2 - 1, find the expression for (2f - g)(x).",
        "answer": (
            "Step-by-Step Function Arithmetic:\n\n"
            "1. Given Functions:\n"
            "  f(x) = x + 1\n"
            "  g(x) = 2x^2 - 1\n\n"
            "2. Definition of Linear Combination of Functions:\n"
            "  (2f - g)(x) = 2f(x) - g(x)\n\n"
            "3. Substitution and Expansion:\n"
            "  2f(x) = 2(x + 1) = 2x + 2\n"
            "  -g(x) = -(2x^2 - 1) = -2x^2 + 1\n\n"
            "4. Combining Terms:\n"
            "  (2f - g)(x) = (2x + 2) - (2x^2 - 1)\n"
            "              = 2x + 2 - 2x^2 + 1\n"
            "              = -2x^2 + 2x + 3\n\n"
            "Final Answer: (2f - g)(x) = -2x^2 + 2x + 3."
        ),
        "topic": "Functions & Mappings"
    },
    97: {
        "question": "Show whether the statement 'It is not raining if and only if roads are dry' is logically equivalent to 'Roads are dry if and only if it is not raining'.",
        "answer": (
            "Logical Equivalence of Biconditional Statements:\n\n"
            "1. Propositional Variables:\n"
            "Let p = 'It is not raining'.\n"
            "Let q = 'Roads are dry'.\n\n"
            "2. Symbolic Forms:\n"
            "Original Statement: p ↔ q ('It is not raining if and only if roads are dry').\n"
            "Proposed Equivalent: q ↔ p ('Roads are dry if and only if it is not raining').\n\n"
            "3. Proof of Commutativity of the Biconditional:\n"
            "By definition:\n"
            "  p ↔ q ≡ (p → q) ∧ (q → p)\n"
            "  q ↔ p ≡ (q → p) ∧ (p → q)\n"
            "Since the logical connective conjunction (∧) is commutative (A ∧ B ≡ B ∧ A):\n"
            "  (p → q) ∧ (q → p) ≡ (q → p) ∧ (p → q)\n"
            "Therefore, p ↔ q ≡ q ↔ p.\n\n"
            "Truth Table Proof:\n"
            "  p | q | p ↔ q | q ↔ p\n"
            "  T | T |   T   |   T  \n"
            "  T | F |   F   |   F  \n"
            "  F | T |   F   |   F  \n"
            "  F | F |   T   |   T  \n"
            "Both truth table columns are identical in every row. Thus, the two statements are logically equivalent."
        ),
        "topic": "Logic & Propositions"
    },
    98: {
        "question": "If f(x) = x and g(x) = -2x, find (f + g)(x).",
        "answer": (
            "Function Addition:\n\n"
            "1. Given Functions:\n"
            "  f(x) = x\n"
            "  g(x) = -2x\n\n"
            "2. Definition of Sum of Functions:\n"
            "  (f + g)(x) = f(x) + g(x)\n\n"
            "3. Calculation:\n"
            "  (f + g)(x) = x + (-2x) = x - 2x = -x.\n\n"
            "Final Answer: (f + g)(x) = -x."
        ),
        "topic": "Functions & Mappings"
    },
    99: {
        "question": "Let the real-valued functions f and g be defined by f(x) = 2x + 1 and g(x) = x^2 - 1. Obtain the expressions for (f ∘ g)(x) and (g ∘ f)(x).",
        "answer": (
            "Composition of Functions:\n\n"
            "1. Given Functions:\n"
            "  f(x) = 2x + 1\n"
            "  g(x) = x^2 - 1\n\n"
            "2. Finding (f ∘ g)(x):\n"
            "  (f ∘ g)(x) = f(g(x))\n"
            "             = f(x^2 - 1)\n"
            "             = 2(x^2 - 1) + 1\n"
            "             = 2x^2 - 2 + 1\n"
            "             = 2x^2 - 1.\n\n"
            "3. Finding (g ∘ f)(x):\n"
            "  (g ∘ f)(x) = g(f(x))\n"
            "             = g(2x + 1)\n"
            "             = (2x + 1)^2 - 1\n"
            "             = (4x^2 + 4x + 1) - 1\n"
            "             = 4x^2 + 4x.\n\n"
            "Notice that (f ∘ g)(x) ≠ (g ∘ f)(x), illustrating that function composition is non-commutative."
        ),
        "topic": "Functions & Mappings"
    },
    100: {
        "question": "Let A = {1, 5, 9} and B = {6, 7}. Find the Cartesian products A × B and B × A. Are they equal? Justify your answer.",
        "answer": (
            "Cartesian Products and Non-Commutativity:\n\n"
            "1. Given Sets:\n"
            "  A = {1, 5, 9} with |A| = 3\n"
            "  B = {6, 7} with |B| = 2\n\n"
            "2. Computation of A × B:\n"
            "  A × B = { (a, b) | a ∈ A, b ∈ B }\n"
            "        = { (1, 6), (1, 7), (5, 6), (5, 7), (9, 6), (9, 7) }.\n"
            "  Cardinality: |A × B| = 3 × 2 = 6.\n\n"
            "3. Computation of B × A:\n"
            "  B × A = { (b, a) | b ∈ B, a ∈ A }\n"
            "        = { (6, 1), (6, 5), (6, 9), (7, 1), (7, 5), (7, 9) }.\n"
            "  Cardinality: |B × A| = 2 × 3 = 6.\n\n"
            "4. Equality and Justification:\n"
            "  Are they equal? NO, A × B ≠ B × A.\n"
            "  Justification: By definition of ordered pairs, (a, b) = (c, d) if and only if a = c and b = d.\n"
            "  Here, (1, 6) ∈ A × B, but (1, 6) ∉ B × A (since (6, 1) ≠ (1, 6)).\n"
            "  Hence, Cartesian product is not commutative unless A = B or at least one set is empty (∅)."
        ),
        "topic": "Set Theory"
    },
    101: {
        "question": "State the necessary and sufficient criteria to verify whether a given binary relation from set A to set B is a function.",
        "answer": (
            "Function Verification Criteria:\n\n"
            "A binary relation f ⊆ A × B is a function from A to B (denoted f: A → B) if and only if it satisfies two strict conditions:\n\n"
            "1. Domain Condition (Total Definition):\n"
            "Every element of the domain set A must be the first coordinate of at least one ordered pair in f:\n"
            "∀x ∈ A, ∃y ∈ B such that (x, y) ∈ f (i.e., Dom(f) = A).\n\n"
            "2. Well-Defined / Single-Valued Condition (Uniqueness):\n"
            "No element of A may be associated with more than one distinct element of B:\n"
            "If (x, y1) ∈ f and (x, y2) ∈ f, then y1 = y2.\n\n"
            "Visual / Graphical Tests:\n"
            "- Arrow Diagram: Exactly one arrow must emanate from every element in set A.\n"
            "- Cartesian Graph: The relation satisfies the Vertical Line Test (every vertical line x = c for c ∈ A intersects the graph at exactly one point)."
        ),
        "topic": "Functions & Mappings"
    },
    102: {
        "question": "Test the following argument for validity:\nPremise 1: Logic is difficult or not many students like logic.\nPremise 2: If Mathematics is easy, then logic is not difficult.\nConclusion: Therefore, Mathematics is not easy or logic is difficult.",
        "answer": (
            "Validity Test of Propositional Argument:\n\n"
            "1. Symbolic Formulation:\n"
            "Let:\n"
            "  d = 'Logic is difficult'\n"
            "  s = 'Many students like logic' (so ~s = 'Not many students like logic')\n"
            "  m = 'Mathematics is easy'\n\n"
            "Argument Form:\n"
            "  Premise 1: d ∨ ~s\n"
            "  Premise 2: m → ~d\n"
            "  Conclusion: ~m ∨ d\n\n"
            "2. Critical Row Analysis (Testing for Invalidity):\n"
            "An argument is valid if and only if in every row where ALL premises are True (critical row), the conclusion is also True.\n"
            "If there exists even one row where premises are True and conclusion is False, the argument is INVALID.\n\n"
            "Let us test whether the conclusion ~m ∨ d can be False:\n"
            "  ~m ∨ d = False requires both ~m = False (so m = True) and d = False.\n"
            "Now substitute m = True and d = False into the premises:\n"
            "  - Premise 2: m → ~d becomes True → ~(False) = True → True = True.\n"
            "  - Premise 1: d ∨ ~s becomes False ∨ ~s. If we assign s = False, then ~s = True, making Premise 1 = False ∨ True = True.\n\n"
            "3. Counterexample Found:\n"
            "At truth assignment m = True, d = False, s = False:\n"
            "  - Premise 1 (d ∨ ~s): True\n"
            "  - Premise 2 (m → ~d): True\n"
            "  - Conclusion (~m ∨ d): False\n\n"
            "Conclusion: Because there is a critical row where all premises are True but the conclusion is False, the argument is INVALID (Fallacious)."
        ),
        "topic": "Logic & Propositions"
    },
    103: {
        "question": "Let A = {a, b, c, d}. Define the null relation ∅ and the universal relation A × A on A. Test both relations for reflexive, symmetric, and transitive properties.",
        "answer": (
            "Analysis of Null Relation and Universal Relation on Set A = {a, b, c, d}:\n\n"
            "1. Null Relation R1 = ∅ on A:\n"
            "  a. Reflexive: False (Irreflexive). For R1 to be reflexive, (x, x) ∈ R1 for all x ∈ A. Since A is non-empty, (a, a) ∉ ∅, so ∅ is NOT reflexive.\n"
            "  b. Symmetric: True. The condition 'if (x, y) ∈ ∅ then (y, x) ∈ ∅' is vacuously true because the antecedent (x, y) ∈ ∅ is always False.\n"
            "  c. Transitive: True. The condition 'if (x, y) ∈ ∅ and (y, z) ∈ ∅ then (x, z) ∈ ∅' is vacuously true because the hypothesis is always False.\n"
            "  Note: ∅ is also antisymmetric (vacuously true), but is not an equivalence relation because it lacks reflexivity.\n\n"
            "2. Universal Relation R2 = A × A on A:\n"
            "  a. Reflexive: True. For every x ∈ A, (x, x) ∈ A × A by definition of the Cartesian product.\n"
            "  b. Symmetric: True. For any (x, y) ∈ A × A, (y, x) ∈ A × A since x, y ∈ A.\n"
            "  c. Transitive: True. For any (x, y) ∈ A × A and (y, z) ∈ A × A, (x, z) ∈ A × A.\n"
            "  Note: Universal relation R2 satisfies all three properties and is therefore an Equivalence Relation on A (with a single equivalence class containing all elements of A)."
        ),
        "topic": "Relations & Partitions"
    },
    104: {
        "question": "Let f and g be functions from the set of integers to the set of integers defined by f(x) = 2x + 3 and g(x) = 3x + 2. What is the composition of f and g (f ∘ g)? What is the composition of g and f (g ∘ f)?",
        "answer": (
            "Composition of Linear Functions on Integers:\n\n"
            "1. Given:\n"
            "  f: Z → Z, f(x) = 2x + 3\n"
            "  g: Z → Z, g(x) = 3x + 2\n\n"
            "2. Composition (f ∘ g)(x):\n"
            "  (f ∘ g)(x) = f(g(x))\n"
            "             = f(3x + 2)\n"
            "             = 2(3x + 2) + 3\n"
            "             = 6x + 4 + 3\n"
            "             = 6x + 7.\n\n"
            "3. Composition (g ∘ f)(x):\n"
            "  (g ∘ f)(x) = g(f(x))\n"
            "             = g(2x + 3)\n"
            "             = 3(2x + 3) + 2\n"
            "             = 6x + 9 + 2\n"
            "             = 6x + 11.\n\n"
            "Conclusion: (f ∘ g)(x) = 6x + 7 and (g ∘ f)(x) = 6x + 11. Since 6x + 7 ≠ 6x + 11 for any integer x, f ∘ g ≠ g ∘ f."
        ),
        "topic": "Functions & Mappings"
    },
    105: {
        "question": "If the 5th element of an arithmetic sequence is -16 and the 20th term is -46, find the 10th term using the proper formula of arithmetic sequence.",
        "answer": (
            "Step-by-Step Solution Using Arithmetic Progression Formula:\n\n"
            "1. Arithmetic Sequence General Term Formula:\n"
            "  a_n = a_1 + (n - 1)d,\n"
            "  where a_1 is the first term and d is the common difference.\n\n"
            "2. Setting Up Simultaneous Equations:\n"
            "  From the 5th term (n = 5):\n"
            "    a_5 = a_1 + 4d = -16      --- (Equation 1)\n"
            "  From the 20th term (n = 20):\n"
            "    a_20 = a_1 + 19d = -46    --- (Equation 2)\n\n"
            "3. Solving for Common Difference (d):\n"
            "  Subtract Equation 1 from Equation 2:\n"
            "    (a_1 + 19d) - (a_1 + 4d) = -46 - (-16)\n"
            "    15d = -30\n"
            "    d = -30 / 15 = -2.\n\n"
            "4. Solving for First Term (a_1):\n"
            "  Substitute d = -2 into Equation 1:\n"
            "    a_1 + 4(-2) = -16\n"
            "    a_1 - 8 = -16\n"
            "    a_1 = -16 + 8 = -8.\n\n"
            "5. Calculating the 10th Term (a_10):\n"
            "  a_10 = a_1 + (10 - 1)d\n"
            "       = a_1 + 9d\n"
            "       = -8 + 9(-2)\n"
            "       = -8 - 18\n"
            "       = -26.\n\n"
            "Final Answer: The 10th term of the arithmetic sequence is -26."
        ),
        "topic": "Sequences & Recurrence"
    },
    106: {
        "question": "Show that the sequence c_n = 2^n - 1, for n ≥ 0 (terms 0, 1, 3, 7, ...), satisfies the recurrence relation c_k = 2c_{k-1} + 1 for all integers k ≥ 1.",
        "answer": (
            "Verification of Recurrence Relation Solution:\n\n"
            "1. Given Explicit Formula:\n"
            "  c_n = 2^n - 1, for integers n ≥ 0.\n\n"
            "2. Recurrence Relation to Verify:\n"
            "  c_k = 2c_{k-1} + 1, for all integers k ≥ 1.\n\n"
            "3. Algebraic Proof (Substituting Formula into Recurrence):\n"
            "  From the explicit formula:\n"
            "    c_k = 2^k - 1\n"
            "    c_{k-1} = 2^{k-1} - 1\n"
            "  Evaluate the Right Hand Side (RHS):\n"
            "    RHS = 2 · c_{k-1} + 1\n"
            "        = 2 · (2^{k-1} - 1) + 1\n"
            "        = (2 · 2^{k-1}) - 2 + 1\n"
            "        = 2^{(k-1)+1} - 1\n"
            "        = 2^k - 1\n"
            "        = c_k = LHS.\n\n"
            "4. Base Condition Check:\n"
            "  For k = 1: c_0 = 2^0 - 1 = 1 - 1 = 0.\n"
            "  From recurrence: c_1 = 2(c_0) + 1 = 2(0) + 1 = 1.\n"
            "  From explicit formula: c_1 = 2^1 - 1 = 1. (Consistent).\n\n"
            "Conclusion: Since LHS = RHS for all integers k ≥ 1, the sequence c_n = 2^n - 1 satisfies the recurrence relation c_k = 2c_{k-1} + 1."
        ),
        "topic": "Sequences & Recurrence"
    }
}

# Apply fixes to specific indices
for idx, item in enumerate(subj):
    qid = item.get("id")
    if qid in SUBJ_CORRECTIONS:
        fix = SUBJ_CORRECTIONS[qid]
        item["question"] = fix["question"]
        item["answer"] = fix["answer"]
        item["solution"] = fix["answer"]
        item["model_answer"] = fix["answer"]
        item["topic"] = fix["topic"]

# Clean all other questions: strip website links, fix formatting
for idx, item in enumerate(subj):
    ans = item.get("answer", "")
    # Remove vulgar url artifacts like http://vustudents.ning.com
    ans = re.sub(r'https?://[^\s]+', '', ans)
    ans = re.sub(r'\n\s*\d+\s*\nMTH202[^\n]*', '', ans)
    ans = re.sub(r'www\.vustudy\.com', '', ans)
    ans = re.sub(r'\[pic\]', '', ans)
    ans = ans.strip()
    item["answer"] = ans
    item["solution"] = ans
    item["model_answer"] = ans

with open("mth202_subjective.json", "w", encoding="utf-8") as f:
    json.dump(subj, f, indent=2, ensure_ascii=False)

print("Saved updated mth202_subjective.json successfully!")
