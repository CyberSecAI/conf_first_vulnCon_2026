# How to Answer “What’s Affected” in Open Source
## Executive Summary
Jess Lowe (Google, AU) and Rex Pan (Google, AU) address the "vulnerability-pocalypse"—the overwhelming volume of alerts that leads to developer burnout and "junk" findings. They propose the Open Source Vulnerability (OSV) schema as a solution, which utilizes machine-readable Git commit hashes to provide precise, artifact-level vulnerability mapping. By moving beyond unstructured text and brittle numeric versions, OSV enables automated tools to accurately determine if a specific project is affected, allowing developers to focus on resolving real threats rather than "chasing ghosts" in their dependency trees.

## Key Points
- The volume of vulnerabilities has grown from 321 in 1999 to a rate of one every 10 minutes today, making manual assessment impossible.
- Traditional CVE records often rely on unstructured text for version data, which is brittle and difficult for automated scanners to match correctly.
- The OSV schema provides a minimal, machine-readable format that uses "introduced," "fixed," and "last affected" events to define vulnerability ranges.
- Git commit hashes are the "gold standard" for precision, as they handle complex scenarios like LTS backports and cherry-picks that numeric versions cannot capture.
- A standardized "Graph Rule" is introduced for merge resolution: a commit is affected if there is a path to an "introduced" commit that does not pass through a "fixed" commit.
- "Introduced Zero" is a specialized tag used for vulnerabilities present since a project's inception, handled carefully to avoid marking unrelated Git subtrees as vulnerable.
- OSV aggregates data from across the ecosystem (GHSA, crates.io, PyPI, Linux kernel) and abstracts away ecosystem-specific versioning logic via a public API.
- The framework enables reachability analysis by providing affected function information directly within the vulnerability record.

## Notable Quotes
- "The average developer doesn't want to know about every vulnerability... they care about delivering features first."
- "Versions are designed for developers, not for security matching."
- "Git commits are the most relevant way to interpret vulnerability data... showing exactly what was changed and affected."
- "We want to stop chasing ghosts... having good vulnerability reports is an important part of that."

## Takeaways
- Integrate the OSV API into your security pipeline to automate the filtering of dependency alerts based on precise artifact data.
- When disclosing vulnerabilities for open-source projects, prioritize the inclusion of "introduced" and "fixed" Git commit hashes to aid downstream consumers.
- Rely on ecosystem-native databases (like GHSA or crates.io) when possible, as they provide better context for package-manager-specific logic.
- Utilize the "patch-id" concept to automatically verify if security fixes have been applied to internal forks or backported branches.
