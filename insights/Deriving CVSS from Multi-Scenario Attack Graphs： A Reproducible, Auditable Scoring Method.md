# Deriving CVSS from Multi-Scenario Attack Graphs： A Reproducible, Auditable Scoring Method
## Executive Summary
This presentation addresses the inherent subjectivity and inconsistency in traditional CVSS scoring by proposing a graph-based modeling approach. The speakers argue that "checklist" scoring often leads to "Frankenstein factors"—vectors that mix unrelated attack scenarios—making the data unusable for automation. By explicitly modeling atomic attack actions and conditions in a directed graph, organizations can programmatically derive reproducible and auditable CVSS scores that accurately reflect the true risk of a vulnerability.

## Key Points
- CVSS subjectivity is a major hurdle for security automation; different analysts frequently produce different scores for the same CVE due to varying interpretations of "worst-case" scenarios.
- "Frankenstein factors" occur when metrics from distinct attack paths (e.g., a remote path and a local user-interaction path) are blended into a single, nonsensical vector.
- The core principle introduced is: "Score the scenario, not the vulnerability." A single vulnerability can enable multiple attack paths, each requiring its own explicit model.
- The proposed method uses a directed graph of atomic actions (Delivery and Exploitation phases), where each node is assigned properties like proximity, privileges, and phase.
- Attack Complexity (AC) and Attack Requirements (AT) are derived from specific "conditions" placed on graph nodes rather than being globally estimated.
- Impact (CIA) is associated with specific actions and systems within the graph, allowing for precise, automated calculation of scope changes.
- This graph-based approach is version-agnostic; characteristics are modeled once and then programmatically mapped to CVSS 3.1 or 4.0 vectors.
- Beyond scoring, these attack graphs serve as a single source of truth for CAPEC mapping, reachability analysis, and automated attack chaining.

## Notable Quotes
- "Score the scenario. Do not score the vulnerability... if you make the scenario explicit, then we can probably eliminate quite some things off the list."
- "What the AI was doing... it answered based on what it felt like... produced Frankenstein factors."
- "Auditability is at the center of reproducible results."
- "The graph is just a single source of truth for so many conclusions."

## Takeaways
- Transition from "checklist-style" CVSS scoring to scenario-based modeling to ensure consistency across distributed security teams.
- Implement structured JSON-based attack graphs to enable the automated derivation of CVSS vectors, reducing human error.
- When a CVE supports multiple attack scenarios, model each separately and derive scores for each to identify the true "worst-case" impact.
- Leverage attack graphs as a foundation for broader security intelligence, such as mapping vulnerabilities to CAPEC patterns.
