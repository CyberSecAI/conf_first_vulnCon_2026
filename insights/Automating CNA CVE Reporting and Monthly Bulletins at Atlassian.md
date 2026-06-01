# Automating CNA CVE Reporting and Monthly Bulletins at Atlassian

## Executive Summary
Deepak Chintala (Atlassian, US) and Zachary Echouafni (Atlassian, US) detail Atlassian's transition from a manual, labor-intensive CVE reporting process to a fully automated pipeline built on their cloud stack using Jira, Forge, and Confluence. They describe overcoming critical bottlenecks in their CNA program, which previously disclosed only 11% of patched vulnerabilities due to manual overhead. By implementing an event-driven service that integrates internal ticketing with the Mitre CVE Services API, Atlassian achieved 100% disclosure coverage and a significant reduction in customer patch time.

## Key Points
- The CNA program was primarily driven by the needs of "Data Center" (on-prem) customers who require formal, action-oriented CVE records to justify maintenance windows and meet compliance mandates.
- The previous manual workflow was a "telephone game" involving spreadsheets, CLI tools, and manual JSON PRs to GitHub, which was unsustainable for a company managing 20+ products.
- Automation was achieved using "Forge," Atlassian’s serverless Node.js platform, to build apps that subscribe to Jira events and interact directly with the Mitre CVE Services API for real-time reservation and publishing.
- A "sanitization process" was implemented to auto-draft public CVE descriptions from internal reports (bug bounty, pen tests) while stripping sensitive exploit details, maintaining a "high-signal, low-toil" output.
- The system leverages structured metadata—specifically CWEs and CVSS vectors—to automatically generate readable descriptions and accurate CPE (Common Platform Enumeration) ranges for security scanners.
- A "Monthly Security Bulletin" cockpit was created in Jira to allow globally distributed teams to review and approve their specific CVE entries in an asynchronous, one-week review cycle.
- Atlassian moved away from "linear reporting" (e.g., "vulnerable after version 7") to "range-based reporting" to accurately reflect back-ported fixes in long-term support (LTS) version lines.
- The results include a 60 work-week annual reduction in engineering toil and a shift in customer behavior, where the average upgrade time dropped from 90 days to 28 days due to the predictable disclosure cadence.

## Notable Quotes
- "We had all the fixes, but we were lacking a microphone to talk about it to our customers."
- "Missing a CVE isn't just a technical oversight. It could lead to be a massive compliance failure for [customers]."
- "We went from 11% coverage to 100%... and we gained the operational efficiency of one full-time employee."
- "Coordinated disclosure is also responsible disclosure. You don't want to just be dumping junk on the internet."
- "Investing in coordinated disclosure has increased our customer trust by a long shot."

## Takeaways
- Integrate internal vulnerability tracking systems (like Jira) directly with the Mitre CVE Services API to eliminate the manual overhead of CVE ID reservation.
- Transition to "range-based" vulnerability reporting in CVE records to avoid false positives in security scanners for customers on long-term support (LTS) version lines.
- Establish a "Monthly Security Bulletin" as a predictable event-driven service to align internal engineering reviews and external customer expectations.
- Utilize a "Self-Service CVE Portal" or API for customers to reduce the volume of manual support inquiries regarding product impact and patch availability.
