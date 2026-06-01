# The Quality Era of CVE: A Blueprint for Global Software Safety
## Executive Summary
Bob Lord (US) presents a vision for the future of the CVE program, advocating for a transition from process-oriented activities to outcome-driven safety missions. Lord argues that the program's "North Star" must be the reduction of software danger through root-cause analysis and secure-by-design practices. He introduces the "CAT" framework—Complete, Accurate, and Timely—as the essential standard for vulnerability records and demonstrates how shifting responsibility for data quality "left" to CNAs can significantly reduce the burden on downstream defenders.

## Key Points
- **The "Activity" vs. "Outcome" Trap:** Martin criticizes the current CVE mission statement ("identify, define, and catalog") as an activity rather than a safety outcome. He proposes a new focus: "To reduce the dangers of using software through the analysis of root causes."
- **Lessons from Other Sectors:** The CVE program should emulate outcome-driven agencies like the NHTSA ("Save lives") and the EPA ("Protect human health"), which focus on the final impact of their work.
- **The "CAT" Framework:** High-quality CVE records must be Complete (all defender needs met), Accurate (correct data in correct fields), and Timely (issued quickly). CAT is easy to remember because "the internet loves cats."
- **Data Entry Problem:** Current CVE schemas allow for too much free-form text, leading to inconsistent and poor-quality data that data scientists cannot easily analyze.
- **Product-Linked Identifiers:** In the proposed prototype, a CVE cannot be created "willy-nilly." It must be linked to a pre-defined parent product or package, ensuring product identification is accurate from the start.
- **Strongly Typed Fields:** Moving away from free-form text to "strongly typed" fields makes records machine-usable at the moment of issuance, reducing the burden on downstream enrichers like the NVD.
- **AI-Assisted Root Cause (CWE):** The prototype demonstrates an AI interface that helps CNAs identify the correct Common Weakness Enumeration (CWE) through clarifying questions, ensuring better root cause analysis for secure-by-design improvements.
- **Community Feedback Loops:** Martin proposes "Community Notes" where external researchers can suggest changes (e.g., a more accurate CWE) directly to the CNA, who can then accept or decline the update.
- **Upstream Quality Responsibility:** The model shifts the responsibility for data quality to the CNAs (the source) where expertise is highest, rather than relying on downstream correction which is error-prone.
- **Product Management Mindset:** CVE should be treated as a "product" where success is measured by the satisfaction and effectiveness of its "customers"—the downstream defenders.

## Notable Quotes
- "Where we are today in 2026, [identifying and cataloging] is an activity. This is not an outcome."
- "Good news: Complete, Accurate, and Timely spells CAT... and everybody on the internet loves a cat."
- "If we improve quality at the source, we have less of a burden of trying to fix things downstream."
- "The idea of a North Star is really key. I think a lot of times we make local decisions with local data... and we have local outcomes."

## Takeaways
- **Adopt the CAT Framework:** Organizations and CNAs should audit their internal CVE processes to ensure every record meets the Complete, Accurate, and Timely standard.
- **Shift Left on Data Quality:** Invest in tools that require product identification and CWE selection at the point of record creation to prevent "junk" data from entering the ecosystem.
- **Engage with Consumers:** Participate in the CVE Consumer Working Group to provide feedback on how vulnerability data is actually used in the field.
- **Focus on Root Causes:** Use CWE data not just as a label, but as a roadmap for eliminating entire classes of coding errors through secure-by-design development.
