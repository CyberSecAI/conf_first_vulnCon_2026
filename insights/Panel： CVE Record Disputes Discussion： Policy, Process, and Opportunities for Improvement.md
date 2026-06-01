# Panel： CVE Record Disputes Discussion： Policy, Process, and Opportunities for Improvement
## Executive Summary
This panel, featuring experts from MITRE, CISA, Microsoft, Red Hat, Qualys, and Trend Micro, dives into the complexities of the CVE record dispute process. The discussion explores the two primary types of disputes—technical disagreements (is it truly a vulnerability?) and operational rule violations (incorrect scope or counting). The experts highlight the "catch-22" faced by vulnerability scanners and defenders when a CVE is permanently disputed, as well as the unique challenges in the open-source ecosystem where upstream maintainers and downstream vendors may disagree on risk. The panel concludes with a call for greater community involvement to help the CVE program evolve its policies to handle the "tsunami" of reports expected in the AI era.

## Key Points
- **Nature of Disputes:** CVE record disputes typically center on whether a bug constitutes a vulnerability, how vulnerabilities are counted (assignment rules), or whether a CNA has violated operational policies.
- **Formalized Policy:** The CVE program has a specific dispute policy (found on cve.org) that includes timelines for acknowledgment (3 days) and resolution/escalation (5 days to conclude after acknowledgment).
- **The "Disputed Forever" Tag:** Tags may remain indefinitely if two parties (e.g., a researcher and a vendor) satisfy program rules but have a technical disagreement that cannot be resolved through consensus.
- **KEV and Disputed CVEs:** CISA occasionally adds disputed CVEs to the Known Exploited Vulnerabilities (KEV) catalog if they are weaponized in the wild, emphasizing that real-world exploitation overrides administrative status.
- **Scanner Dilemma:** Vulnerability management vendors (like Qualys) must choose between alerting customers to a disputed bug (potential false positive) or staying silent (potential false negative liability).
- **Open Source Deadlock:** A significant pain point occurs when upstream maintainers refuse to acknowledge a vulnerability, leaving the entire downstream supply chain in a "deadlock" without a fix.
- **The "Resume" Factor:** For researchers, CVE assignments are "resumes." Denying an assignment can lead to frustration and potentially uncoordinated disclosure if the dispute process feels unfair.
- **Bug Bounty vs. Disclosure Policy:** A concerning trend is vendors using their "bug bounty scope" as their "disclosure policy," refusing to assign CVEs for classes of bugs they simply choose not to pay for.
- **Escalation Path:** Disputes begin with the assigning CNA, can escalate to a Root (e.g., Red Hat, CISA), and finally to the Top-Level Root (MITRE) for a final adjudication.
- **AI Tsunami:** Panelists anticipate a massive increase in vulnerability reports driven by AI, which will test the scalability of the current manual dispute resolution processes.

## Notable Quotes
- "The disputed tag may remain there forever... as much as we like closure, that's not realistic in a program as distributed and large as the CVE program."
- "If there is a bug that is being weaponized in the wild, it is irrelevant that it's disputed or not."
- "Red Hat respects upstream's assessment... but the entire open source supply chain is expecting a fix."
- "I'm tired of the 'if we can find it, somebody already found it' speech... if we can find it, attackers already have it."
- "Accept some nuance because that's basically what a dispute tag is. Coordinated vulnerability disclosure is difficult."

## Takeaways
- **Don't Ignore Disputed Tags:** A "Disputed" label doesn't mean a vulnerability isn't real; it means there is a conflict. Organizations should evaluate the technical description and their own exposure.
- **Use Formal Channels:** Follow the cve.org dispute policy rather than engaging in "social media debates" to resolve assignment or technical conflicts.
- **Prepare for Nuance:** Auditors and compliance officers should be educated on the meaning of the "Disputed" tag to avoid automatically failing systems for unpatched, but technically contested, CVEs.
- **Participate in Policy:** The CVE Strategic Planning Working Group is open for volunteers; your perspective as an enterprise consumer or auditor is needed to help refine dispute rules.
- **VEX for Clarity:** Support and advocate for machine-readable formats like VEX to communicate the context and status of disputes more effectively across security tools.