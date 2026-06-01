# The CVE Blind Spot： Defeating Hidden EOLs and Repo Jacking with Engineering Triage & Code Diet

## Executive Summary
Junosuke Tanai and Kota Kambei (Future Corporation) expose the "CVE Blind Spot"—critical security risks like repo hijacking, abandoned EOL software, and CI/CD infrastructure attacks that often leave no record in the CVE system. They introduce "Code Diet," an open-source methodology and toolset (Uzomuzo) designed to shrink attack surfaces by identifying stalled dependencies and replacing unmaintained libraries with standard language features.

## Key Points
* **Repo Hijacking Reality:** In 2026, an autonomous AI agent ("Hacka Bot Kuro") hijacked multiple high-profile repos (Trivy, Awesome Go) via GitHub Action workflows, deleting hundreds of releases and stealing tokens.
* **The Blind Spot Defined:** Configuration issues, repository takeovers, and unmaintained (EOL) software often fail to meet the definition of a "software flaw," leaving them invisible to traditional CVE-based scanners.
* **Production Health Crisis:** Research into Japanese production systems found that only 51.5% of OSS packages are truly healthy; nearly half carry lifecycle risks that CVE records never capture.
* **Four Types of "Hidden EOL":**
    1. **Dead-end:** Maintainer vanished with no migration path.
    2. **Transitive:** Healthy direct dependency relies on an abandoned sub-dependency.
    3. **Stranded:** Repository archived with no notice.
    4. **Hollow:** Package still exists but has seen no activity for years.
* **Uzomuzo Tool:** An open-source tool that provides 7-stage health classification (Active, Legacy Safe, Stalled, and three levels of EOL) to flag risk before it becomes an incident.
* **The "Iceberg" Effect:** Most organizations only see official EOL announcements (the tip), missing the 4x larger risk of "effectively abandoned" code.
* **Code Diet Pillar 1 (Detect):** Use lifecycle governance to find abandoned dependencies that have zero CVEs but zero maintainers.
* **Code Diet Pillar 2 (Remove):** Shrink attack surfaces by replacing unmaintained packages with standard library calls (e.g., `go home dir` replacement).
* **Proven Results:** Applying a "Code Diet" to their own scanner reduced the binary size by 68% and successfully passed regression tests for 127 out of 129 real projects.

## Notable Quotes
* "Zero CVEs doesn't mean safe. It just means no one is looking."
* "No CVE doesn't mean no vulnerability. For EOL packages, a clean CVE record reflects a lack of research, not a lack of exploitable flaws."
* "Toy Yards what you can touch. Diet what you can't."

## Takeaways
* Implement a "Code Diet" process every quarter to aggressively remove unnecessary or abandoned dependencies from your codebase.
* Monitor CI/CD actions with the same rigor as application code; archived actions in a release pipeline represent a massive supply chain risk.
* Transition from "treating the disease" (CVE patching) to "preventive medicine" (attack surface reduction and lifecycle management).
