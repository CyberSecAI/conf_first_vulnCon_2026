# Three Musketeers: CVE, CSAF, and VEX

## Executive Summary
Presented by Owen, Tyler, and Jono from CISA, this session details how the agency operationalizes vulnerability disclosure at a national level. The "Three Musketeers" of the talk are CVE (Common Vulnerabilities and Exposures), CSAF (Common Security Advisory Framework), and VEX (Vulnerability Exploitability eXchange). The speakers discuss the shift from legacy, manual processes (using tools like Vulnogram and even Notepad) to a more integrated, automated approach using custom platforms. They emphasize that while machine-readable formats are essential for scalability, the ultimate goal is high-quality, actionable data that clearly communicates vulnerability status (affected vs. fixed) and risk (through CVSS and SSVC scoring). The talk also highlights the "naming problem" in software and the ongoing challenges of harmonizing overlapping standards.

## Key Points
*   **CISA’s CVD Mission:** Vulnerability disclosure is a core part of the "Secure by Design" initiative. CISA encourages all organizations to adopt a Vulnerability Disclosure Policy (VDP) to manage the reality that no software is perfect.
*   **Standardized Formats:** CISA has standardized on CVE and CSAF because they are machine-readable, evolving, and fulfill public reference requirements.
*   **The Status Requirement:** A quality record must include "Status" (Fixed, Known Affected, Known Not Affected, Under Investigation). Without status, a record lacks actionable value for downstream consumers.
*   **VEX within CSAF:** CISA utilizes the CSAF VEX profile to provide explicit product statuses and impact statements, helping users understand if they are actually affected by a vulnerability in their specific environment.
*   **Format Mapping:** The team developed custom tooling to map fields between CVE and CSAF, addressing inconsistencies such as CVE’s lack of an explicit "Fixed" field (which CISA maps to the "Unaffected" field).
*   **The Naming Problem:** Software naming is compared to candy bars (e.g., a US Milky Way is a UK Mars bar). This "intractable" problem is exacerbated by widely varying versioning conventions (semantic, date-based, versionless).
*   **Quality Descriptions:** CISA uses a "Mad Lib" template for CVE descriptions to ensure consistency: [Vendor] + [Product] + [Affected Versions] + [Attack Vector/Privileges] + [Impact] + [Fixed Version].
*   **Multi-Dimensional Scoring:** CISA scores vulnerabilities using CVSS 3.1, CVSS 4.0, and SSVC (Stakeholder-Specific Vulnerability Categorization). SSVC is used to provide a coordinator’s perspective on exploitation and technical impact.
*   **CSAF Trusted Provider:** As a "Trusted Provider," CISA must meet rigorous requirements, including valid JSON, ROLIE feeds, digital signatures (PGP), and consistent file naming conventions.
*   **Publication Workflow:** The team uses a Git-based workflow where CSAF documents and their signatures are pushed to a public GitHub repository, serving as the source of truth for their disclosures.

## Notable Quotes
*   "Providing good information about your CVEs is part of secure by design... because we have an acceptance that nothing is going to be absolutely perfect when it ships."
*   "Status is one of the most important parts of the record... it gives you an actionable thing to do."
*   "You can't engineer a solution to a philosophical problem."
*   "The formats alone do not solve the data quality problems."
*   "If two people with the same training and the same information... assign a different identifier [CWE], there's nothing we're going to do about that in the automation that's going to fix that problem."

## Takeaways
*   **Adopt VEX for Clarity:** Organizations should move toward CSAF/VEX to communicate exploitability clearly, reducing the "scanner noise" that plagues vulnerability management teams.
*   **Standardize Internal templates:** Use structured templates (like CISA's "Mad Lib" approach) for vulnerability descriptions to ensure that all necessary information (vector, impact, fix) is included every time.
*   **Prepare for Automation:** As vulnerability volume increases, organizations must move away from PDFs and toward machine-readable JSON (CVE 5.0, CSAF 2.x) to enable scalable response.
*   **Focus on Inter-Rater Agreement:** When using classification systems like CWE, organizations should test for consistency among their analysts to ensure that the data being automated is actually accurate.
*   **Understand Format Convergence:** Acknowledge that CVE and CSAF evolved in parallel and have significant overlap; use tooling to handle the mapping rather than trying to force one to replace the other.
