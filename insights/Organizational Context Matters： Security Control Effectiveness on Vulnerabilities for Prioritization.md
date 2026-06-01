# Organizational Context Matters: Security Control Effectiveness on Vulnerabilities for Prioritization
## Executive Summary
Ertugrul Yaprak and Mehmet Kiliç (Picus Security, TR) present a methodology for refining vulnerability prioritization by incorporating "Security Control Effectiveness" (SCE) into the scoring process. They argue that standard CVSS base scores are insufficient because they fail to account for an organization's specific defensive posture. By mapping CVEs to an "action library" of attack simulations and measuring how existing security controls (like WAFs, EDRs, and firewalls) perform, Yaprak and Kiliç demonstrate how to calculate a "Contextual CVSS" and a final "Exposure Score." This evidence-based approach enables security teams to focus on vulnerabilities that are truly exploitable within their unique environments.

## Key Points
- **The Prioritization Crisis:** With over 50,000 vulnerabilities expected in 2026 and 28% of them being exploited within 24 hours, organizations can no longer rely on manual triage.
- **Security Control Effectiveness (SCE):** This metric measures how well an organization’s million-dollar security investments actually prevent the exploitation of specific vulnerabilities.
- **Evidence-Based Validation:** Prioritization should be based on evidence from real attack simulations (Breach and Attack Simulation) rather than theoretical risk.
- **Action Library Mapping:** Vulnerabilities are mapped to specific "actions" (TTPs) in a simulation library. AI agents now perform this mapping in minutes, a process that previously took researchers hours.
- **Contextual CVSS Calculation:** Using CVSS Environmental Metrics, scores are adjusted based on defensive performance. If a network control blocks a remote exploit, the "Attack Complexity" increases and the "Contextual CVSS" decreases.
- **Beyond Decreasing Scores:** Contextualization is not just about reducing risk; a "Medium" CVE may be elevated to "Critical" if internal security controls are proven ineffective against it.
- **The Exposure Score Formula:** A holistic operational score that combines Base CVSS, Contextual CVSS, Business Criticality (Crown Jewels), and Exploitability.
- **Instance-Level Management:** Organizations must manage millions of "vulnerability instances" (CVE x Asset). Contextual scoring helps shrink this list to a manageable set of "true" criticals.
- **AI Contextualization:** AI agents go beyond keyword matching to understand the context of a CVE (e.g., identifying Active Directory privilege escalation even if specific technical terms are omitted in the description).
- **Operational View:** In a real customer case, contextual scoring reduced the number of "Critical" and "High" vulnerabilities from 68% of the backlog to 54%, allowing for more focused remediation.

## Notable Quotes
- "CVSS alone is not enough to manage your vulnerability list."
- "You invest million dollars in security controls to prevent your organization assets... how can we use them for prioritization?"
- "We are in the post-AI era... mapping one CV actually takes a minute or less."
- "This shows you the risk of this vulnerability... it is not the same thing for other organizations because every organization has different security solutions."
- "You need to focus, and you can manage these vulnerability list via this way."

## Takeaways
- **Integrate Defensive Data:** Stop treating vulnerability management and security control management as separate silos. Use the results of your security control testing to deprioritize "blocked" vulnerabilities.
- **Adopt Contextual CVSS:** Use the Environmental Metrics section of the CVSS standard to create an automated, organization-specific risk score.
- **Automate Mapping with AI:** Use LLM-based agents to map incoming CVEs to your existing attack simulation library to maintain a real-time view of exploitability.
- **Prioritize by Exposure:** Use an "Exposure Score" that factors in business criticality so that even a highly exploitable vulnerability is deprioritized if it only affects non-critical assets.
- **Validate, Don't Assume:** Do not assume a vendor's "High" score applies to you. Validate the exploit path against your specific EDR and WAF configurations before committing remediation resources.