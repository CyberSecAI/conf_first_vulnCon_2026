# The Hidden Cost of CVEs: Can CSAF and VEX Change the Equation?
## Executive Summary
Lisa Olson (Microsoft, US) examines the immense global resource burden imposed by CVEs and the urgent need for automation and standardization as vulnerability volumes skyrocket. Using Microsoft's experience with "Patch Tuesday" as a backdrop, Olson explores the "hidden costs"—potentially hundreds of millions of human hours—spent globally on assessing and testing vulnerabilities. She argues that as AI-driven research accelerates, current manual processes are becoming unsustainable, making the adoption of machine-readable standards like CSAF and VEX a critical survival strategy for the entire security ecosystem.

## Key Points
- **The "Great Wall" of Effort:** Microsoft Copilot estimates that a single Windows CVE can consume up to 200 million global human hours across 10 million organizations. Cumulatively, this effort is equivalent to building the Great Wall of China 25 times.
- **Vulnerability Volume Explosion:** The volume of CVEs is increasing rapidly; for instance, Google published more Chrome CVEs in the first three months of 2024 (186) than in the entirety of 2023 (174).
- **Automation is Mandatory:** As red teams and researchers begin using LLMs to find vulnerabilities in bulk, the entire CVE lifecycle—from assessment to publication—must be fully automated to keep pace.
- **The CNA Inconsistency Gap:** Approximately 80% of CVE records are produced by a small number of top CNAs. While top CNAs struggle to maintain 100% "enrichment" (CVSS, CWE, CPE), smaller CNAs with less practice face even greater challenges in data quality.
- **VEX Adoption Signal:** Microsoft began publishing VEX statements for Azure Linux and saw over 100 million requests in a single month (March 2024), indicating a massive, hungry audience for machine-readable exploitability data.
- **The Quality Age of CVE:** Standards like CVSS, CWE, and CPE are necessary for a "quality" CVE, but consistent application remains a hurdle that requires better industry-wide tooling.
- **Shared Tooling vs. Regulation:** Olson advocates for the industry to band together to build shared CVE/CSAF/VEX generation tools rather than waiting for regulators (like CISA) or MITRE to provide them.
- **Researcher Relations:** The industry must better respect and protect researchers, making the CVE process easier for them to navigate as they contribute to the global vulnerability pool.
- **Risk of Splintering:** There is a growing danger of regional or sectoral vulnerability numbering systems (e.g., EUVD) emerging, which would force vendors to produce multiple records for the same issue and complicate global protection efforts.
- **CVE as the Core:** Despite its flaws, Olson argues for keeping the 25-year-old CVE program as the "core" to avoid the fragmentation of global vulnerability intelligence.

## Notable Quotes
- "You could build the Great Wall of China 25 times based on this number of hours that have been spent [on Windows CVEs]."
- "If you're going to automate [the researcher's] job, you have to automate mine."
- "The industry needs to help itself to build the tools that we need. I don't think we can depend on the regulators or MITRE, God love them, to build us the tools that we need."
- "Imagine a world where you'd have the CVE machine and it spits out in proper CSAF and proper VEX... and we all spoke the same language."

## Takeaways
- **Prioritize Machine-Readability:** Transitioning to CSAF and VEX is not just a compliance task but a survival strategy for managing the coming wave of bulk-reported vulnerabilities.
- **Invest in Automation:** Organizations must automate the enrichment of CVE records (CWE/CVSS) to maintain high data quality and relevance in an AI-driven environment.
- **Collaborate on Infrastructure:** Join industry coalitions to build vendor-neutral tools for CVE management, rather than relying on disparate, proprietary systems.
- **Monitor Data Quality:** Use tools like the "CNA Scoreboard" to benchmark CVE completeness and ensure that vulnerability data is actionable for downstream consumers.
