# CVE Record Format - Purl and CPE Workshop
## Executive Summary
Chris Coffin (MITRE) and MZ MegaZone (F5, Inc., US) lead a technical workshop on integrating Package URL (PURL) and Common Platform Enumeration (CPE) identifiers into the CVE JSON record format (versions 5.1 and 5.2). The session focuses on how these identifiers eliminate ambiguity in software identification across diverse ecosystems and outlines the specific logic required for correct implementation. While these fields remain optional to maintain a low barrier to entry for CNAs, the presenters emphasize that their adoption is essential for enabling the automation required in modern vulnerability management.

## Key Points
- PURL (Package URL) is a universal, URL-based syntax for identifying software packages independent of the distribution channel (e.g., NPM, RPM, Maven).
- In CVE JSON 5.2, PURL identifiers must be included without the version component; the version must be defined in the existing "versions" array to avoid data conflicts.
- CPE (Common Platform Enumeration) remains the primary standard for identifying commercial platforms, products, and operating systems.
- The "CPE Applicability Language" is integrated into the CVE format, allowing CNAs to describe complex vulnerable configurations using AND/OR logical operators.
- This logic enables "running on" statements, such as specifying that a piece of software is only vulnerable when installed on a specific version of an operating system.
- CNAs are strongly encouraged to use CPEs that already exist in the official NVD dictionary to ensure downstream tools can resolve the data.
- PURL and CPE are both located within the "affected" array of the JSON record, sitting alongside traditional fields like product name and vendor.
- The workshop highlights that the CVE program is open to adopting additional identifiers (like OmniBOR) in the future if they gain significant community traction.

## Notable Quotes
- "Identifying software packages reliably has been hard... PURL attempts to eliminate that by creating a universal identifier with a predictable structure."
- "The nice thing about standards is there's so many to choose from."
- "We're not officially recognizing just CPE and just Pearl... we'll extend it and include other software identifiers in the future if need be."
- "It was better to have a CVE ID assigned to something so everyone could talk about the same thing... and to keep the barrier to entry for that as low as possible."

## Takeaways
- Adopt PURL for open-source software records to facilitate automated matching in developer-centric package management environments.
- Utilize the CPE Applicability Language to provide context-aware security data, specifically for "running on" hardware or OS dependencies.
- Before adding a CPE to a record, verify its existence in the NVD CPE Dictionary or request its addition from NIST to ensure interoperability.
- Avoid embedding version data within PURL strings; instead, map the package name to the CVE record's structured version ranges.
