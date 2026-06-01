# Vulnrichment Playground

## Executive Summary
Art Manion (Tharros Labs, US) and Lindsey Cerkovnik (CISA, US) present CISA's "Vulnrichment" program, a public initiative designed to enhance CVE records with high-quality analysis and metadata. Serving as an experimental "playground," the program backfills missing data—such as SSVC, CVSS scores, and CWE mappings—through the CVE Authorized Data Provider (ADP) container. Manion and Cerkovnik highlight the program's philosophy of maximizing impact by focusing on actionable intelligence, including the strategic decision to prioritize SSVC over traditional CPE generation to better serve the global security community.

## Key Points
*   **Scale of Operations:** CISA handles 250–300 coordinated vulnerability disclosure (CVD) cases at any given time, disclosing over 2,000 CVEs annually. This volume provides unique insights into the "state of the art" of vulnerability disclosure.
*   **Democratizing Data:** Analysis originally mandated for Federal Civilian Executive Branch (FCEB) agencies is now provided to the public. Vulnrichment ensures that analysis paid for by taxpayers is consumable for all defenders.
*   **The ADP Container:** Vulnrichment's primary delivery mechanism is the CVE ADP container. This allows CISA to add information to a CVE record without overwriting the original CNA’s (CVE Numbering Authority) data.
*   **The CPE Experiment:** CISA discovered that creating CPEs (Common Platform Enumeration) consumed 2/3 of analysts' time. Based on public feedback that CPEs were less useful than other data, CISA stopped providing them for all records to focus on broader coverage of SSVC and other enrichments.
*   **SSVC for Prioritization:** Every new CVE in the Vulnrichment program receives Stakeholder-Specific Vulnerability Categorization (SSVC) scoring, focusing on the first three decision points: exploitation, automatability, and technical impact.
*   **Test in Production:** The program is used to perform "experiments" that would be too risky for the KEV catalog, such as testing how to represent CVE relationships or broken reference markers.
*   **Record Evolution (Case Study):** A study of a Pandoc vulnerability (SSRF) showed how Vulnrichment tracked and improved a record over several months—correcting typos, updating CVSS scores, and refining descriptions as new analysis became available.
*   **Filling the Gaps:** Vulnrichment is a "backfill" service. If a CNA provides a CVSS score or CWE, Vulnrichment does not overwrite it. It only acts when the original record is incomplete.
*   **Transparency through GitHub:** All Vulnrichment activities are public. Users can file issues on the GitHub repository to dispute scores or request corrections, fostering a transparent community debate.
*   **Future Scope:** CISA is exploring how to represent relationships between CVEs (e.g., when one vulnerability enables another) in a machine-readable way within the CVE record.

## Notable Quotes
*   "We want to spend public funds efficiently... put it out into the world, especially cyber data."
*   "The automated solutions [of today] diminish your free will." (Referencing the need for better prioritization data).
*   "If you only govern the risk that comes with a public identifier, you're only governing the street light, not the street."
*   "Reducing [what you do] is a good move also at times." (Regarding the decision to stop producing CPEs).
*   "Vulnrichment acts as a discovery tool... someone else didn't [provide the data] who maybe should have."

## Takeaways
*   **Leverage the ADP Container:** Security teams should pull data from the CVE ADP container (not just the CNA container) to get CISA’s enriched analysis, including SSVC and verified CWEs.
*   **Participate in the Playground:** Use the Vulnrichment GitHub repository to provide feedback on data quality. CISA actively uses this feedback to shape future standards for the CVE program.
*   **Adopt SSVC over Raw CVSS:** Move toward the SSVC model for internal prioritization, as it provides a more nuanced view of exploitation and impact than raw CVSS scores alone.
*   **Demand Supplier Quality:** Encourage software vendors (CNAs) to provide complete records (CVSS, CWE, affected ranges) so that backfill services like Vulnrichment aren't necessary.
*   **Monitor Record Evolution:** Realize that a CVE record is a "living document." Use tools that can track updates to ADP containers as new analysis (like weaponization confirmation) is added.
