# From JSON to Clarity: Practical Tools for SBOM Interpretation
## Executive Summary
John Bergland (IBM, US) and Zadia Alden (Supply Chain Manager, GB) discuss the "operational gap" in the use of SBOMs (Software Bill of Materials), noting that while technically sound, these documents remain under-leveraged for risk-based decision-making. They showcase a series of lightweight, AI-built web applications designed to transform dense JSON data into clear signals for stakeholders in legal, procurement, and management. The session highlights how these tools surface five key metrics—data quality, dependency mapping, CVE age, license risk, and version drift—to bridge the gap between technical data and business intelligence.

## Key Points
- SBOMs currently suffer from a "Wild West" of varying quality and structure, with many missing critical NTIA minimum elements like supplier data and dependency relationships.
- Using AI to "vibe-code" targeted web apps allows security teams to rapidly build tools that surface specific business risks without a massive development overhead.
- "SBOM Quality Insights" acts as a gatekeeper, determining if a vendor-provided SBOM is credible enough to be used for downstream risk analysis.
- The "Dependency Analyzer" makes hidden transitive relationships visible, answering the common developer question: "How did this vulnerable library get into my build?"
- The "CVE Age Tracker" provides a process health signal; if vulnerabilities survive multiple release cycles (e.g., >6 months), it indicates a breakdown in remediation.
- License Analysis categorizes software into risk tiers (High Risk/Copyleft vs. Permissive), enabling legal teams to identify compliance issues without opening a single JSON file.
- "Version Drift Analysis" identifies "dormant" or EOL projects by calculating the gap between the version in use and the latest available release.
- Smaller, modular tools are prioritized over monolithic platforms because they are easier to validate and fix, which is crucial when using AI-generated code.

## Notable Quotes
- "SBOMs are currently technically correct, but operationally we'd say under leveraged."
- "If the SBOM itself is weak, every downstream decision that we make is going to be weaker as a result."
- "AI lowers the bar to building the tooling, but it really doesn't solve the interpretation."
- "The value isn't in generating more intelligence, but it's at least exposing what's already in the SBOMs you've received."

## Takeaways
- Use simple visualization tools to bridge the gap between technical security data and non-technical decision-makers in procurement and legal.
- Prioritize "Version Drift" monitoring to identify aging or unsupported components that represent a long-term compliance and security liability.
- Before acting on SBOM data, run it through a quality check to ensure it contains the identifiers (PURL/CPE) necessary for accurate vulnerability matching.
- Adopt a "modular tools" approach to security automation; build targeted apps for specific questions rather than waiting for a single, complex platform.
