---
layout: post
title: "Some Notes on Languages (CS)"
date: 2018-11-05
excerpt: "A Quick Review of Automata, Regular Language, Regex and CFG"
tags: [thought, NLP]
comments: true
---
### Finite Automata ###
**Alphabet** is a set of **characters**. **Strings** are made from sequences of **characters**.
**Language** is a set of **strings**. The **closure** is all possible **strings**. A **language** is a subset of the **closure**. To determine if a **string** is valid in your **language**, we test it in a mathematical machine, called the **finite automaton**.

**Rules**
There are
* starting states
* accepting states
* non-accepting states
* state transitions

You start from the starting state and "consume" one character from your string, reading left to right. When the string has been consumed and you end on an accepting string, the string is a member of your language.

**DFA** or deterministic finite automatons are the simplest kind.
* 1 starting state
* 1 possible transition per character

A language is **regular** if it can be expressed as an **DFA**.
A cool feature is that the complement of the **language** can also be expressed as an **DFA**.

**NFA** or non-deterministic finite automatons have the property that
* more than 1 possible transition per character
* epsilon-transitions (no character consumed)

To evaluate if a string is accepted, among the possible state transitions,
at least one must end on an accepting state. Some questions are
1. can any problem solvable by **NFA** be solved by **DFA**?
2. can any problem solved by **NFA** be solved efficiently by **DFA**?
All **NFA** can be expressed as **DFA**. Efficiency varies between automatons.

A way of stating this is - is there a universe where this sequence of actions leads to the desired outcome?

**NFA -> DFA**
1. Subset Construction
Each state in **DFA** corresponds to set of states in **NFA**.
Start state in **NFA** is start state in **DFA** plus all epsilon transitions.
The transition from some initial state from some character is set of all reachable states, including epsilon transitions.

**Regular Languages**
L1 L2 are languages. Then **regular languages** have the property that
1. Complement L1 is also regular
>Invert all accepting and non-accepting states and direction of transitions
2. L1 union L2 is also regular
>Starting with a new starting state and add epsilon transitions to all starting states in L1 and L2
3. L1 intersection L2 is also regular
>This is equivalent to the complement of the union of the complements of L1 and L2
4. Concatenation L1 L2 is also regular
>Add epsilon transition from all L1 accepting states to all L2 starting states
5. Closure L1 is also regular
>**Language exponentiation** is just concatenation of language with itself
>Just add an epsilon transition from all accepting states to starting states 

e.g. Noun = {} Verb = {} Article = {}, ArticleNounVerbNoun is a sentence made from concatenation of other languages.

**Regular Expressions**
1. Atomic Regular Expression
>null, { a }, { epsilon }
2. Compound Regular Expression
>.
>R*
>R+
>R?
>AB
>A|B
>A{4}

**Thompson's Algorithm**
Regex matchers convert regular expressions into NFA, then DFAs.

The theorem is that if a language is regular, there is a regular expression for it.
Imagine a transition that is a regular expression, rather than a character.
If we can convert NFA to regular expression, we can read that off it.
1. Add epsilon transitions to start and accepting states
2. Eliminate intermediate states between start and accepting states using properties of regular languages

**Transformation**
DFA - (direct conversion) -> NFA - (state elimination) -> Regex
Regex - (Thompson's Algorithm) -> NFA - (subset construction) -> DFA

### Nonregular Language ###

### Context Free Grammar ###
So regex matches strings and automata accepts strings in the language. CFGs is a different way to define class of languages.
It has these 4 objects.
* nonterminal symbols
* terminal symbols
* production rules - how to convert nonterminal to string of terminal and nonterminal
* start symbol (LHS)

E -> int
E -> E Op E
E -> ( E )
Op -> + - * /

CFG is the set of strings derivable from the starting symbol.
Derivation involve replacing nonterminals with the RHS of the rules of production.
It is a **context free language** iff there is a CFG for it.
Every **regular language** is **context free** since the latter is a superset of the former.

**Parse Trees**
This is a tree encoding steps of derivation. Each internal node is nonterminal and each leaf node is terminal.
**Parsing** involves finding a **parse tree** for that string, often done in compilation.
A problem that can arise is **ambiguity** when there is a string with at least 2 **parse trees**.
One way to resolve this is to use operator precedence.

