# AI Systems Are Software Systems

## Executive Summary
Jonathan Spring (CISA, US) asserts that AI systems are, fundamentally, software systems and must be managed within existing cybersecurity and risk management frameworks. By translating AI jargon into mature security concepts, he provides a strategic roadmap for PSIRT and product security teams to integrate AI models and datasets into their standard governance processes. The session emphasizes that AI software carries the same fundamental security obligations as any information system, requiring a secure-by-design approach.

## Key Points
- AI systems are not an exception to the rule that software must be secure by design; they are information systems and carry the same fundamental security obligations.
- Federal directives, such as CISA’s Known Exploited Vulnerabilities (KEV) list and VDP requirements, apply to AI systems; there is no "get out of jail free" card for AI.
- CISA Directive 26-02 (January 2026) requires the decommissioning of any system, including AI software, that is no longer receiving supported security updates.
- Much of AI security is simply established concepts with new jargon; for example, "prompt injection" is essentially a specific form of adversarial input screening.
- AI models and datasets should be treated as software libraries and configuration files, respectively, within an organization’s Asset Management and SBOM (Software Bill of Materials) framework.
- Organizations must maintain a clear distinction between software quality issues (e.g., factually incorrect "hallucinations") and cybersecurity vulnerabilities (e.g., remote code execution or unauthorized system access).
- The perceived difficulty of AI "stochasticity" (non-determinism) is often an engineering choice; exposing pseudo-random number generator (PRNG) seeds would make AI bugs more reproducible than traditional software race conditions.
- Existing CVE numbering authority (CNA) rules already adequately cover AI scenarios, including insecure default configurations (Rule 4.1.4) and vulnerabilities in hosted services (SaaS).

## Notable Quotes
- "AI systems are software systems. Also big surprise... I have gotten a surprisingly large amount of awakened eye movement and gasps when I say this sentence."
- "Models and data sets are just like libraries and configuration files."
- "If your regular engineers are writing way more code with AI and they already don't have a good CI/CD pipeline, you now have just introduced a vulnerability fountain."
- "A vulnerability does not require a fix for a CVE to be issued... It's not like this is 'oh my gosh, we've got to change the operational rules.'"
- "AI doesn't have new problems in the naming space... naming is hard in predictable and reasonable ways."

## Takeaways
- Formally integrate AI development teams into existing PSIRT and product security workflows rather than allowing them to operate in a "shadow IT" or research-only silo.
- Utilize Package URLs (purls) to track AI models as dependencies within SBOMs to enable automated vulnerability matching and asset management.
- Require AI vendors and internal developers to provide a supported security update plan before deployment to comply with modern decommissioning mandates.
- Educate AI engineers on the "CNA Operational Rules" to ensure they understand that exploitability, regardless of fix availability or retraining time, often warrants a CVE.
