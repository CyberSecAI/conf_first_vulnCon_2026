# Flipping the Criticality Funnel, A Practical Path to Real Prioritization
## Executive Summary
Sophia Sanles-Luksetich (GitHub, US) and Zachary Goldman (GitHub, US) discuss the pervasive issue of "severity inflation," where the majority of security findings are labeled "High" or "Critical," rendering traditional prioritization systems ineffective. They introduce the GitHub Risk Score (GIHRS), a unified framework that normalizes data from 25 disparate sources into a single, transparent, and actionable score. By integrating asset criticality with real-world threat intelligence—such as EPSS and CISA KEV—GitHub has successfully "flipped the funnel," ensuring that only the most urgent risks reach the top of the engineering queue while reducing developer burnout and triage fatigue.

## Key Points
- "When everything is critical, nothing is"—GitHub found that 50% of their findings were initially labeled as High risk, leading to engineer burnout and "argumentative" triage.
- The GIHRS framework provides a "single score to rule them all," normalizing data from 25 internal and external sources into a consistent, actionable metric.
- Transparency is a core requirement; the score is composed of four auditable parts: an abstract base class, a versioned calculator, a risk map, and detailed score justifications for engineers.
- Metric groups are categorized into Base (CVSS metrics), Threat (EPSS, CISA KEV, weaponization), and Asset (crown jewels, PII, availability requirements).
- The model is multiplicative (Base * Threat * Asset), which ensures that vulnerabilities on low-value assets or those with near-zero exploit probability do not clutter the critical queue.
- GIHRS includes a "qualitative threat" vector, allowing security analysts to manually adjust scores based on specific organizational context or emerging public sentiment.
- The framework utilizes the "skeleton" of CVSS 3.1 but applies custom internal weights and values to reflect the specific threat landscape of a developer-centric organization.
- Tuning is an iterative process using a "risk pyramid" to visualize the distribution of findings; the goal is for Criticals to be the rarest and most prioritized category.

## Notable Quotes
- "When everything is critical, nothing is."
- "If a risk score isn't actionable, then nobody's really going to care."
- "Engineers want things to be transparent... so that they don't have room to argue."
- "Just starting to have your own internal risk score gives you the control to actually change what your team's priorities are versus relying on a third-party source."

## Takeaways
- Audit your vulnerability distribution; if it does not resemble a pyramid with few criticals at the top, your scoring criteria is likely failing to prioritize.
- Build an internal risk score that weights asset context (e.g., internal vs. external exposure) as heavily as the vulnerability's base severity.
- Provide full "score details" to developers; transparency reduces friction and helps teams understand the business rationale behind remediation deadlines.
- Incorporate EPSS as a high-impact multiplier to down-level "Critical" findings that have no evidence of exploitation in the wild.
