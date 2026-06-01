# CVE Decaf: Brewing Better and More Actionable Data Quality
## Executive Summary
Jerry Gamblin (Cisco, US) and Jay Jacobs (Empirical Security, US) explore the critical shift within the CVE program from focusing on the quantity of records to the quality and "fitness for use" of the data. By identifying gaps in identification, characterization, and remediation, they propose a framework to transform CVE records into actionable products that directly support consumer tasks. Their session details how re-engineering the 27-year-old CVE record format can meet the needs of modern, high-speed, automated vulnerability management.

## Key Points
- Data quality is redefined as "fitness for use," shifting the focus from the technical requirements of the CNA to the actual needs of the data consumer.
- The "Lord's Automation Test" is introduced: if a CVE record requires human interpretation or custom logic to be understood by a tool, it fails the quality standard for modern automation.
- There are four primary consumer tasks that CVE data must support: Identification (is it in my environment?), Characterization (what is it?), Remediation (how do I fix it?), and Prioritization (how fast do I act?).
- A significant "population gap" exists in current data; only about 28% of CVEs in a recent 6-month period contained machine-readable product identifiers like CPE or PURL.
- Identification is further hindered by a "design gap" in versioning, where versions are designed for developers rather than for automated security matching.
- Characterization quality is low because current records lack structured fields for exploitation conditions and detection signature guidance (e.g., Snort-like logic).
- Remediation data is often missing or incomplete; for instance, the "workaround" field is used in less than 1% of records, often by a single CNA.
- The presenters argue that the CVE record, designed 27 years ago for simple tracking, must be re-engineered to support the modern era of high-speed, automated vulnerability management.

## Notable Quotes
- "Rather than blaming individuals, it's blaming the process. Let's figure out what's wrong with the process, not wrong with the CNA."
- "If a data requires human intervention, it doesn't pass the automation test."
- "A CVE without a fix is really just a data point at this point."
- "The CVE record was designed 27 years ago for a different purpose than it's used now... the design is wrong."

## Takeaways
- Treat CVE records as a product that must meet consumer requirements, not just a compliance check for CNAs.
- Prioritize the use of PURL and CPE identifiers in records to enable automated vulnerability matching in consumer environments.
- Move towards a "Quality Era" where completeness and machine-readability of records are as important as the assignment of the ID.
- Participate in the CVE Consumer Working Group to help define the metadata requirements that actually assist in remediation and triage.
