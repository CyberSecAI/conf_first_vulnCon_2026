# Production Is the New Attack Surface: Why Post-Deployment Endpoint Detection Is Now Critical
## Executive Summary
Tracy Ragan (DeployHub.com, US) highlights a critical imbalance in modern security where mature "Shift Left" tools contrast with a post-deployment defense that remains a massive blind spot. Ragan argues that while most security resources are pre-deployment, 100% of attacks target production environments. She proposes a "Digital Twin" model—leveraging SBOMs, deployment metadata, and Git repository links to create a synchronized map of production. This approach enables near-instant vulnerability detection and auto-remediation, particularly for constrained "edge" environments like satellites and IoT where traditional security agents cannot run.

## Key Points
- **The Security Imbalance:** Organizations are strong on "offensive" pre-deployment scanning (SCA, SAST, DAST) but weak on "defensive" post-deployment protection.
- **Production Vulnerability Reality:** While pre-deployment scans catch about 80% of issues, 100% of actual attacks happen in production, often targeting vulnerabilities that emerge *after* software has been released.
- **The "Heavy" Tooling Problem:** Traditional post-deployment tools are agent-based, expensive, and require weeks of planning, making them inaccessible for smaller teams or constrained environments.
- **Constrained Edge Challenges:** Assets like satellites (often the size of a toaster) or autonomous equipment cannot support heavy security agents, leading to remediation windows as long as 180 days.
- **The Digital Twin Concept:** A Digital Twin uses an SBOM, the Git repo link, and deployment metadata (Helm charts/audit logs) to track production status without touching the live endpoint.
- **Operationalizing SBOMs:** SBOMs should not be static checkboxes; they should be the primary data source for Continuous Threat Exposure Management (CTEM).
- **Near-Instant Detection:** By syncing a Digital Twin against vulnerability feeds (like OSV.dev) every few minutes, organizations can achieve sub-day detection and response for production threats.
- **Auto-Remediation Path:** Because a Digital Twin links production state back to the Git repo, it can automatically identify the necessary patch and generate a PR or issue for developers.
- **Precision Over Noise:** Focusing only on what is actually deployed and reachable allows teams to ignore the "toil" of thousands of theoretical vulnerabilities in dormant code.
- **Adoption at the Developer Level:** Unlike enterprise agent-based tools, a Digital Twin approach can be implemented by a single DevOps engineer in less than 10 minutes.

## Notable Quotes
- "Production is the new attack surface... the right is under attack."
- "A satellite is the size of a toaster... you're not going to put an agent on it."
- "SBOMs are not a checkbox. They're not just a new doc you check into your git repo... they should be operationalized."
- "Organization buying is not required. A developer can do this on their own."
- "The goal for us as a community is to be able to address runtime software supply chain attacks in less than one day."

## Takeaways
- **Defend the "Right":** Recognize that software becomes weak *after* release as new CVEs emerge. Implement a system for continuous production monitoring.
- **Link Deployment to Sourcing:** Ensure every deployment is mapped to its specific SBOM and Git repository to enable rapid root-cause analysis and remediation.
- **Use Agentless Models for Edge:** For IoT, satellites, or short-lived containers, adopt "Digital Twin" metadata tracking instead of resource-heavy security agents.
- **Prioritize Reachability:** Use Digital Twin data to perform "de-bloating," removing unused and vulnerable packages from production images to reduce the attack surface.
- **Embrace CTEM:** Adopt the "Continuous Threat Exposure Management" mindset, syncing your production state against vulnerability databases on a sub-hourly basis.